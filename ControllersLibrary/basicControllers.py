''' Basic Controllers to be wrapped into functions that can have some user input and be called by the UI '''
# input will need to take things as sizes radiuses number of curves and subdivs let's say 
# colour overrite for both outliner and controller itself left right colour
# would be great if it took in some naming template thing 
# and if it was able to slightly downsize each controller down the hierarchy


import maya.cmds as cmds
import math
###############################################################
### CIRCULAR CONTROLLERS
###############################################################


## simple circle controller script

circleCtrlName = "circleCtrl_00#"
#placeholder radius to be swaped for user input
radius = 5
circleCtrl = cmds.circle( nr=(1, 0, 0), r=radius, n=circleCtrlName)[0]
cmds.delete(circleCtrl, constructionHistory = True)
#freeze transforms
cmds.makeIdentity(circleCtrl, apply=True, t=1, r=1, s=1, n=2 )
print circleCtrl

#group? auto offset?

#######################################################################

## tubeController

# create two (or more????) circles and join with lines
radiusOne = 5
radiusTwo = 10
circleOne = cmds.circle( nr=(1, 0, 0), r=radiusOne, n="tubeCircleOne")[0]
circleTwo = cmds.circle( nr=(1, 0, 0), r=radiusTwo, n="tubeCircleTwo")[0]

cmds.move(-10, 0, 0, [circleOne], relative = True, objectSpace=True, worldSpaceDistance=True) 

# join the circles with lines (have a way to choose number of curves maybe???) maybe use curveOnSurface


## taperedTubeController:

# change radius of one circle and angle of lines in between accordingly (snapping to curve?)

########################################################################

## lollipopController
lollipopCtrlName="lollipopCtrl_00#"
lollipopCtrl = cmds.group(em=True, name=lollipopCtrlName)
circleList = []
print LollipopCtrl



radiusLolli = 2.0
numberOfVerticalCircles = 5
angleVertical = 360.0/(numberOfVerticalCircles*2.0)
#print angle

verticalCircleName = lollipopCtrl+"verticalCircleLolli_00#"


for x in xrange(numberOfVerticalCircles):
    verticalCircle = cmds.circle( nr=(1, 0, 0), r=radiusLolli, n=verticalCircleName)[0]
    cmds.rotate (0, angleVertical*x, 0)
    print verticalCircle
    #delete history
    cmds.delete(verticalCircle, constructionHistory = True)
    #freeze transforms
    cmds.makeIdentity(verticalCircle, apply=True, t=1, r=1, s=1, n=2 )
    circleList.append(verticalCircle)
    
numberOfHorizontalCircles = 5
angleHorizontal = 360.0/(numberOfHorizontalCircles*2.0)
print angleHorizontal

horizontalCircleName = lollipopCtrl+"horizontalCircleLolli_00#"

for y in xrange(numberOfHorizontalCircles):
    horizontalCircle = cmds.circle( nr=(0, 1, 0), r=radiusLolli, n=horizontalCircleName)[0]
    if angleHorizontal*y == 90.0 :
        cmds.delete()
        #pass
    else:
        cmds.rotate (angleHorizontal*y, 0, 0)
    #delete history
    cmds.delete(horizontalCircle, constructionHistory = True)
    #freeze transforms
    cmds.makeIdentity(horizontalCircle, apply=True, t=1, r=1, s=1, n=2 )    
    circleList.append(horizontalCircle)
    
print circleList
cmds.parent(circleList, lollipopCtrl)
    
#lolliStick
#cmds.snapMode( curve=True )
stickLength = 10
stickBegin = -radiusLolli
stickEnd = -(stickBegin + stickLength)
stickName = lollipopCtrl+'lolliStick_00#'
lolliStick = cmds.curve( n=stickName, d=1, p=[(0, stickBegin, 0), (0, stickEnd, 0)] )
cmds.parent(lolliStick, lollipopCtrl)
stickShapeOld = cmds.listRelatives(lolliStick,ad=True, type='shape')
print lollipopCtrl
print stickShapeOld
stickShape = cmds.rename(stickShapeOld, lolliStick + "Shape")
print stickShape

#list components parent shapes under the main group cleanup groups
lolliComponents = cmds.listRelatives(lollipopCtrl, ad=True, type='shape')
print lolliComponents

cmds.select(lolliComponents, r=True)
cmds.select(lollipopCtrl, add=True, adn=False)
cmds.parent(relative=True, shape=True)

### Cleanup Code to delete empty groups from  https://polycount.com/discussion/71520/maya-script-delete-empty-groups 

#not the best way to loop it but list relatives causes name clashes etc 

for t in xrange(2):
    deleteList = []
    transforms =  cmds.ls(type='transform')
    for tran in transforms:
        if cmds.nodeType(tran) == 'transform':
            children = cmds.listRelatives(tran, ad=True) 
            if children == None:
                print '%s, has no childred' %(tran)
                deleteList.append(tran)
    if len(deleteList) > 0:            
       cmds.delete(deleteList)

###end of code from polycount.com

#delete history
cmds.delete(lollipopCtrl, constructionHistory = True)
#freeze transforms
cmds.makeIdentity(lollipopCtrl, apply=True, t=1, r=1, s=1, n=2 )

#center pivot at the end of the stick if stick exists
cmds.move(0, stickEnd, 0, lollipopCtrl+".scalePivot", lollipopCtrl+".rotatePivot", absolute=True)

#cmds.snapMode( curve=False )      

#delete history (like in rectangle and circle)
#freeze transforms
#everything under one transform node maybe center pivot at the end of lolli stick

####################################################
### RECTANGULAR CONTROLLERS
####################################################

#simple rectangular controller

rectangleCtrlName = "rectangleCtrl_00#"
print rectangleCtrlName
rectangleWidth = 6
rectangleHeight = 3

# create squares 

rectangleCtrl = cmds.nurbsSquare(n=rectangleCtrlName, nr=(1, 0, 0), d=1, c=(0, 0, 0), sl1=rectangleWidth, sl2=rectangleHeight )


#delete history
cmds.delete(rectangleCtrl[0], constructionHistory = True)
#freeze transforms
cmds.makeIdentity(rectangleCtrl[0], apply=True, t=1, r=1, s=1, n=2 )

#rename the children of squareCtrl to prevent naming errors
print rectangleCtrl
babySquares = cmds.listRelatives(rectangleCtrl[0],ad=True, type='shape')
print babySquares

for baby in babySquares:
    print baby
    newBaby = cmds.rename(baby,rectangleCtrl[0]+baby)
    print newBaby

    
babies = cmds.listRelatives(rectangleCtrl[0],ad=True, type='shape')
print rectangleCtrl
print babies
    
cmds.select(babies, r=True)
cmds.select(rectangleCtrl[0], add=True, adn=False)
cmds.parent(relative=True, shape=True)
    


#delete history
cmds.delete(rectangleCtrl[0], constructionHistory = True)
#freeze transforms
cmds.makeIdentity(rectangleCtrl[0], apply=True, t=1, r=1, s=1, n=2 )


###Code to delete empty groups from  https://polycount.com/discussion/71520/maya-script-delete-empty-groups 
for t in xrange(2):
    deleteList = []
    transforms =  cmds.ls(type='transform')
    for tran in transforms:
        if cmds.nodeType(tran) == 'transform':
            children = cmds.listRelatives(tran, ad=True) 
            if children == None:
                print '%s, has no childred' %(tran)
                deleteList.append(tran)
    if len(deleteList) > 0:            
       cmds.delete(deleteList)


####################################################

## simpleBoxController

## trapezoidalBoxController

# maybe it can be one with ability to change parameters aka change the size of the square

####################################################
##squareLolliCtrl

#empty group
squareLolliCtrl = cmds.group(em=True, name=squareLolliCtrlName)
squareList = []
print squareLolliCtrl

squareLolliCtrlName = "squareLolliCtrl_00#"
print squareLolliCtrlName

squareCtrlName = squareLolliCtrl+"squareCtrl_00#"
print squareCtrlName
squareSide = 3
angleVertical = [0,90,0]
angleHorizontal = [0,0,90]

# create squares 
for x in xrange(3):
    squareCtrl = cmds.nurbsSquare(n=squareCtrlName, nr=(1, 0, 0), d=1, c=(0, 0, 0), sl1=squareSide, sl2=squareSide )
    cmds.rotate(45,angleVertical[x],angleHorizontal[x])
    #delete history
    cmds.delete(squareCtrl, constructionHistory = True)
    #freeze transforms
    cmds.makeIdentity(squareCtrl[0], apply=True, t=1, r=1, s=1, n=2 )
    
    #rename the children of squareCtrl to prevent naming errors
    print squareCtrl
    babySquares = cmds.listRelatives(squareCtrl[0],ad=True, type='shape')
    print babySquares
    
    for baby in babySquares:
        newBaby = cmds.rename(baby,squareCtrl[0] + baby)
        print newBaby
    
    squareList.append(squareCtrl[0])
    #print squareList
    
# append to group/parent
cmds.parent(squareList, squareLolliCtrl)
    
babies = cmds.listRelatives(squareLolliCtrl,ad=True, type='shape')
print squareLolliCtrl
print babies

#for baby in babies:
#    print baby
#    newBaby = cmds.rename(baby, "squareShape_00")
#    print newBaby
    
cmds.select(babies, r=True)
cmds.select(squareLolliCtrl, add=True, adn=False)
cmds.parent(relative=True, shape=True)
    


#delete history
cmds.delete(squareLolliCtrl, constructionHistory = True)
#freeze transforms
cmds.makeIdentity(squareLolliCtrl, apply=True, t=1, r=1, s=1, n=2 )



#stick or no stick find a way to choose

#lolliStick
#cmds.snapMode( curve=True )
stickLength = 10
stickBegin = -((squareSide*math.sqrt(2))/2)
print stickBegin
stickEnd = -(stickBegin + stickLength)
squareStickName = squareLolliCtrl+'squareLolliStick'
lolliStick = cmds.curve( n=squareStickName, d=1, p=[(0, stickBegin, 0), (0, stickEnd, 0)] )

#parent grp then shape under the grp and delete empty
cmds.parent(lolliStick, squareLolliCtrl)
stickShapeOld = cmds.listRelatives(lolliStick,ad=True, type='shape')
print squareLolliCtrl
print stickShapeOld
stickShape = cmds.rename(stickShapeOld, lolliStick + "Shape")
print stickShape
    
cmds.select(stickShape, r=True)
cmds.select(squareLolliCtrl, add=True, adn=False)
cmds.parent(relative=True, shape=True)


### Cleanup Code to delete empty groups from  https://polycount.com/discussion/71520/maya-script-delete-empty-groups 

#not the best way to loop it but list relatives causes name clashes etc 

for t in xrange(2):
    deleteList = []
    transforms =  cmds.ls(type='transform')
    for tran in transforms:
        if cmds.nodeType(tran) == 'transform':
            children = cmds.listRelatives(tran, ad=True) 
            if children == None:
                print '%s, has no childred' %(tran)
                deleteList.append(tran)
    if len(deleteList) > 0:            
       cmds.delete(deleteList)

###end of code from polycount.com

#center pivot at the end of the stick if stick exists
cmds.move(0, stickEnd, 0, squareLolliCtrl+".scalePivot", squareLolliCtrl+".rotatePivot", absolute=True)

# idk if I need to delete history again and freeze transforms but other than tht DONE

####################################################
### OTHER CONTROLLERS
####################################################
# FK/IK switch controller

#generate curve from text input
FKIKSwitchCurve = cmds.textCurves(n="FK_IKSwitchCtrl", f='Arial', t='FK/IK')

print FKIKSwitchCurve[0]

#delete history
cmds.delete(FKIKSwitchCurve, constructionHistory = True)
#freeze transforms
cmds.makeIdentity(FKIKSwitchCurve, apply=True,n=2 )

# rename curve groups into their parents names, then shapes into thir parents name + shape
relatives = cmds.listRelatives(FKIKSwitchCurve, c=True)
print relatives

letterCurvesList = []
for relative in relatives:
    letterShape = cmds.listRelatives(relative, ad=True, type='shape')
    print letterShape
    letterShapeName = relative+"Shape"
    letterCurve = cmds.rename(letterShape, letterShapeName)
    print letterCurve
    letterCurvesList.append(letterCurve)
    
print letterCurvesList


print FKIKSwitchCurve[0]

# make it all into one transform node
cmds.parent(letterCurvesList, FKIKSwitchCurve[0], relative=True, shape=True)  

### Cleanup Code to delete empty groups from  https://polycount.com/discussion/71520/maya-script-delete-empty-groups 

#not the best way to loop it but list relatives causes name clashes etc 

for t in xrange(2):
    deleteList = []
    transforms =  cmds.ls(type='transform')
    for tran in transforms:
        if cmds.nodeType(tran) == 'transform':
            children = cmds.listRelatives(tran, ad=True) 
            if children == None:
                print '%s, has no childred' %(tran)
                deleteList.append(tran)
    if len(deleteList) > 0:            
       cmds.delete(deleteList)

###end of code from polycount.com

FKIKSwitchCtrl = cmds.rename(FKIKSwitchCurve[0],"FK_IKSwitchCtrl_00#")
print FKIKSwitchCtrl

# custom attributes

#lock and hide attributes
cmds.setAttr(FKIKSwitchCtrl+".tx", lock=True, keyable=False, channelBox=False)
cmds.setAttr(FKIKSwitchCtrl+".ty", lock=True, keyable=False, channelBox=False)
cmds.setAttr(FKIKSwitchCtrl+".tz", lock=True, keyable=False, channelBox=False)
cmds.setAttr(FKIKSwitchCtrl+".rx", lock=True, keyable=False, channelBox=False)
cmds.setAttr(FKIKSwitchCtrl+".ry", lock=True, keyable=False, channelBox=False)
cmds.setAttr(FKIKSwitchCtrl+".rz", lock=True, keyable=False, channelBox=False)
cmds.setAttr(FKIKSwitchCtrl+".sx", lock=True, keyable=False, channelBox=False)
cmds.setAttr(FKIKSwitchCtrl+".sy", lock=True, keyable=False, channelBox=False)
cmds.setAttr(FKIKSwitchCtrl+".sz", lock=True, keyable=False, channelBox=False)

####NEEDS FIXING TO ADD ATTRIBUTE TO A VALID OBJECT, ALSO FIX STUFF ABOVE SO IT IS NOT NAME BASED SO YOU CAN HAVE MULTIPLE CTRLRS
cmds.select(FKIKSwitchCtrl, r=True)
##add the switch attribute thing
cmds.addAttr(ln="FK_IK_Switch",nn="FK_IK_Switch", at="enum", en="FK:IK:")
cmds.setAttr(FKIKSwitchCtrl+".FK_IK_Switch", keyable=True)


####################################################
#customTextCtrl

customTextCtrlName = "userGaveNameCtrl_00#"
customTextInput = "PEW PEW"
chooseFont = 'FreeSans'

#generate curve from text input
customTextCurve = cmds.textCurves(n="customTextCtrl", f=chooseFont, t=customTextInput)

print customTextCurve[0]

#delete history
cmds.delete(customTextCurve, constructionHistory = True)
#freeze transforms
cmds.makeIdentity(customTextCurve, apply=True,n=2 )

# rename curve groups into their parents names, then shapes into thir parents name + shape
relatives = cmds.listRelatives(customTextCurve, c=True)
print relatives

letterCurvesList = []
letterShapesList = []
for relative in relatives:
    letterShapes = cmds.listRelatives(relative, ad=True, type='shape')
    #print letterShape
    for l in letterShapes:
        print l
        
        #letterShapesList.append(l)
        #print letterShapesList
        
    #for s in letterShapesList:
        #print s
        letterShapeName = "customTextCtrl" + relative+l
        letterCurve = cmds.rename(l, letterShapeName)
        print letterCurve
        letterCurvesList.append(letterCurve)
            
    
print letterCurvesList


print customTextCurve[0]

# make it all into one transform node
cmds.parent(letterCurvesList, customTextCurve[0], relative=True, shape=True)  

### Cleanup Code to delete empty groups from  https://polycount.com/discussion/71520/maya-script-delete-empty-groups 

#not the best way to loop it but list relatives causes name clashes etc 

for t in xrange(2):
    deleteList = []
    transforms =  cmds.ls(type='transform')
    for tran in transforms:
        if cmds.nodeType(tran) == 'transform':
            children = cmds.listRelatives(tran, ad=True) 
            if children == None:
                print '%s, has no childred' %(tran)
                deleteList.append(tran)
    if len(deleteList) > 0:            
       cmds.delete(deleteList)

###end of code from polycount.com

customTextCtrl = cmds.rename(customTextCurve[0],customTextCtrlName)
print customTextCtrl


####################################################

# COG or Base arrows controller

# eye controller

# hands controller

# cone controller
