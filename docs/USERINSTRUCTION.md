# Loading the tool into Maya

## Instruction on how to load in the tool, pre-requisits etc. into Maya

First download the code from github and put somewhere on your PC.

Edit the [mod file](../ControllersLibrary.mod) to point to your path so to where the module is located on your machine:

for me it is located in /home/s5128983/RiggingToolsPipelineAndTD so the mod file looks like this:

```
+ ControllersLibrary 1.0 /home/s5128983/RiggingToolsPipelineAndTD/pipelineandtd22-patipocz/
XBMLANGPATH +:= icons
MAYA_SCRIPT_PATH +:= /home/s5128983/RiggingToolsPipelineAndTD/pipelineandtd22-patipocz/
PYTHON_PATH +:= /home/s5128983/RiggingToolsPipelineAndTD/pipelineandtd22-patipocz/
```
You will also need to find and edit Maya.env file (on Linux for maya 2020 it is probably located in /maya/2020/). 
Add the line pointing to your module. For me it's:
```
MAYA_MODULE_PATH=/home/s5128983/RiggingToolsPipelineAndTD/pipelineandtd22-patipocz/
```
Replace the path with the path where your module is located.

Open Maya

After the module has been properly imported into Maya which can be checked by listing all the imported modules: 
```
cmds.moduleInfo(listModules=True)
```
The tool is ready to use and can be opened using this script:

```
import mayaWindow

#use line below to reload the window if needed
reload(mayaWindow)

# opens the window
mayaWindow.controllersLibWindow()

```
This script is also saved into [runScript.py](../runScript.py)

For quick access to the tool it is best to add this script to shelf.

*! If the icons do not load or something is wrong with the module loading them, a way around it is copying the icons into **/prefs/icons** folder so for me it's **maya/2020/prefs/icons*** as this is the place maya looks for icons, however the module should work

## How to use the Controller Library Tool?
1. Open the tool window using runScript above.
2. Input values/parameter for your chosen controller type in appropriate section.
3. Press the button with the icon of the controller you want to create.
4. Optional: Select the created controller in the scene and press auto offset grouping button to group it under a transformation node. Now you can scale it, rotate it and place anywhere in the scene and parent/constraint it when necessary using the group so without changing values of the controller attributes (they remain zeros).



