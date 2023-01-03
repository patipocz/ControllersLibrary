import maya.cmds as cmds

def debug() :
    print("debug")

def createCircleCtrl(circleCtrlName = "circleCtrl_00#", radius = 5):
        
    '''
    This function creates a circle controller with provided radius and controller name.
    '''

    circleCtrl = cmds.circle( nr=(1, 0, 0), r=radius, n=circleCtrlName)[0]
    cmds.delete(circleCtrl, constructionHistory = True)
    #freeze transforms
    cmds.makeIdentity(circleCtrl, apply=True, t=1, r=1, s=1, n=2 )
    #print circleCtrl
