## rectangular controller
rectangleCtrlName = "rectangleCtrl_00#"
rectangleWidth = 2
rectangleHeight = 3

# create degree 1 square 
rectangleCtrl = cmds.nurbsSquare(n=rectangleCtrlName, nr=(1, 0, 0), d=1, c=(0, 0, 0), sl1=rectangleWidth, sl2=rectangleHeight )

#orientation so it can be a rhombus / kite 

#delete history
cmds.delete(rectangleCtrl, constructionHistory = True)
#freeze transforms
cmds.makeIdentity(rectangleCtrl[0], apply=True, t=1, r=1, s=1, n=2 )

babies = cmds.listRelatives(rectangleCtrl[0],ad=True, type='shape')
print rectangleCtrl
print babies

newBabies = []

for baby in babies:
    newBaby = cmds.rename(baby,rectangleCtrl[0] + baby)
    print newBaby
    newBabies.append(baby)

print newBabies

cmds.select(newBabies, r=True)
cmds.select(rectangleCtrl[0], add=True, adn=False)
cmds.parent(relative=True, shape=True)



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

##################################################




##the other

#empty group


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
