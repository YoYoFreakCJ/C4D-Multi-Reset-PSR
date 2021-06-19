![Demonstration](https://i.imgur.com/JzaFiHY.gif)

# Introduction
Have you ever wanted to reset position, scale and rotation for multiple objects with a single click? Well now you can! And you won't even loose your object selection!

This is a Cinema 4D python script which modifies any object so it can reset PSR for other objects upon selection. My primary use case is during character rigging.

Tested with Cinema 4D R23.

# Installation
1. Download the script into your script folder at:
%APPDATA%\MAXON\Maxon Cinema 4D *your release*\library\scripts
2. Restart your Cinema 4D if it was open.

# How To Use
## Setup

![Setup](https://i.imgur.com/b8LcjMI.gif)

1. Select the object which you'd like to make the reset button.
2. Execute the script "Multi-Reset PSR".
- By either selecting it from the Extensions -> User Scripts menu or by finding it using the Commander (Ctrl/Cmd + C).
3. Drag objects into the Include list.
- This also works with Selection Objects.
4. Enable the Interaction tag.

## Modify Include List

![Modify](https://i.imgur.com/UShEkFf.gif)

Since you can't select the object anymore once you enable the Interaction tag you can't modify the include list with this tag enabled. So just disable the Interaction tag and you're free to modify the Include list to your hearts content.

# F.A.Q.

> Clicking the reset object does not reset the objects in the Include list. What do?

Enable the Interaction tag.

> I can not select the reset object and can therefore not edit the Include list. What do?

Disable the Interaction tag.

> Why didn't you use this other totally obvious way I'd like to tell you about?

Because I didn't know about it. But please do tell, I'm always looking for better ways to do my stuff.

# Disclaimer
I'm fairly certain it won't mess your scene up but I still can't promise anything. The script is rather small and pretty straight forward so take a look for yourself if you like.

Please be harsh with your critique, that's the only way I can learn.
