''' 
trying other options for the lollipop gimbal situation no luck so far 
because it will always have a gimbal eventually or you will not get the amount of circles you want 
cuz every even input of horizontal circles will end up on 90 eventually so if I use if to delete it 
then the artist doesn't get the amount of circles they wanted 

'''


## lollipopController
radiusLolli = 2.0
numberOfVerticalCircles = 2
angleVertical = 360.0/(numberOfVerticalCircles*2.0)
#print angle

for x in xrange(numberOfVerticalCircles):
    cmds.circle( nr=(1, 0, 0), r=radiusLolli, n="verticalCircleLolli_00#")[0]
    cmds.rotate (0, angleVertical*x, 0)
    
    
numberOfHorizontalCircles = 2
angleHorizontal = 360/(numberOfHorizontalCircles*2)
print angleHorizontal

for y in xrange(numberOfHorizontalCircles):
    cmds.circle( nr=(0, 1, 0), r=radiusLolli, n="horizontalCircleLolli_00#")[0]
    for angle in xrange(0,360,angleHorizontal):
        print angle
        cmds.rotate(angle*y, 0, 0)   
    
#lolliStick
#cmds.snapMode( curve=True )
stickLength = 10
stickBegin = -radiusLolli
stickEnd = -(stickBegin + stickLength)
lolliStick = cmds.curve( n='lolliStick', d=1, p=[(0, stickBegin, 0), (0, stickEnd, 0)] )