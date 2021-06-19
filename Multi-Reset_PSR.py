"""Name-US: Multi-Reset PSR
Description: Modifies any object so it can reset PSR for any other object upon selection.
"""

import c4d
from c4d import gui

userDataGroupName = "Include"
userDataPropertyName = "Include"

def main():
    baseObj = doc.GetActiveObject()

    userDataId = createUserData(baseObj)
    createInteractionTag(baseObj, userDataId)

    doc.SetActiveObject(baseObj)

def createUserData(baseObj):
    group = createUserDataGroup(baseObj)

    userData = c4d.GetCustomDatatypeDefault(c4d.CUSTOMDATATYPE_INEXCLUDE_LIST)
    userData[c4d.DESC_NAME] = userDataPropertyName
    userData[c4d.DESC_SHORT_NAME] = userDataPropertyName
    userData[c4d.DESC_CUSTOMGUI] = c4d.CUSTOMGUI_INEXCLUDE_LIST
    userData[c4d.IN_EXCLUDE_FLAG_NUM_FLAGS] = 1
    userData[c4d.IN_EXCLUDE_FLAG_INIT_STATE] = 1
    userData[c4d.DESC_PARENTGROUP] = group

    createdUserData = baseObj.AddUserData(userData)

    userDataId = createdUserData[1].id

    return userDataId

def createUserDataGroup(baseObj):
    group = c4d.GetCustomDatatypeDefault(c4d.DTYPE_GROUP)
    group[c4d.DESC_NAME] = userDataGroupName
    group[c4d.DESC_SHORT_NAME] = userDataGroupName
    group[c4d.DESC_TITLEBAR] = 1
    group[c4d.DESC_PARENTGROUP] = c4d.DescID(0)

    return baseObj.AddUserData(group)

def createInteractionTag(baseObj, userDataId):
    c4d.CallCommand(100004788, 50066) # New Interaction Tag

    tag = baseObj.GetFirstTag()

    tag[c4d.INTERACTIONTAG_ENABLE] = 0
    tag[c4d.INTERACTIONTAG_SCRIPT_LANGUAGE] = 1
    tag[c4d.INTERACTIONTAG_SCRIPT_PY] = "# #######################################################\r\n#                        IMPORTANT\r\n# The object which holds this interaction tag must have\r\n# a user data property of type In-/Exclusion. Enter the\r\n# ID of this property into the following variable.\r\n# #######################################################\r\ninclusionUserDataId = " + str(userDataId) + "\r\n\r\nimport c4d\r\nfrom c4d import gui\r\n\r\nselectionObjectType = 5190\r\nundoCommand = 12105\r\nresetPsrCommand = 1019940\r\ndeselectAllCommand = 100004767\r\n\r\ndef onSelect():\r\n    # Remember the currently selected object because the next line will deselect it.\r\n    tagParent = doc.GetActiveObject()\r\n\r\n    # Undo the selection action to re-activate the previous selection.\r\n    c4d.CallCommand(undoCommand) # Undo\r\n\r\n    # Remember the previous selection so it can be restored once this script is at its end.\r\n    previousSelection = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)\r\n\r\n    # Loop through the objects to reset .\r\n    objectsToReset = tagParent[c4d.ID_USERDATA, inclusionUserDataId]\r\n    for i in range(objectsToReset.GetObjectCount()):\r\n        objectToReset = objectsToReset.ObjectFromIndex(doc, i)\r\n\r\n        doc.SetActiveObject(objectToReset)\r\n\r\n        # If the object is a selection object, restore the selection.\r\n        if objectToReset.GetType() == selectionObjectType:\r\n            c4d.CallButton(objectToReset, c4d.SELECTIONOBJECT_RESTORE)\r\n\r\n        c4d.CallCommand(resetPsrCommand) # Reset PSR\r\n\r\n    # Restore previous selection.\r\n    selectExclusively(previousSelection)\r\n\r\ndef selectExclusively(objectsToSelect):\r\n    c4d.CallCommand(deselectAllCommand) #Deselect All\r\n\r\n    for i in range(len(objectsToSelect)):\r\n        doc.SetActiveObject(objectsToSelect[i], i == 0 if c4d.SELECTION_NEW else c4d.SELECTION_ADD)\r\n"

# Execute main()
if __name__=='__main__':
    main()