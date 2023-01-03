numberOfHorizontalCircles=5
radiusLolli = 5
horizontalCircleName ="horizon_00#"

class CircleRange:
    def __init__(self, num_circles):
        self.increment = 90/float(num_circles)
        self.angle = 0.0
        
    def __iter__(self):
        return self
        
    def next(self):
        if self.angle < 90.0:
            angle = self.angle
            self.angle += self.increment
            return angle
        else:
            raise StopIteration

negateAngle = False
angleMultipler = 1


for angle in CircleRange(numberOfHorizontalCircles):
    print(angle)
    if negateAngle:
        angleMultipler = -1
    else :
        angleMultipler = 1

    negateAngle = not negateAngle
    
    horizontalCircle = cmds.circle(nr=(0, 1, 0), r=radiusLolli, n=horizontalCircleName)[0]
    cmds.rotate(angle * angleMultipler, 0, 0)
