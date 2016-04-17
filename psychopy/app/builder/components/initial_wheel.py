from psychopy import visual, core  # import some libraries from PsychoPy
from scipy.io import loadmat
import random

#create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

#building the colorwheel: you build 180 wedges, each take up two degree space (they range from 2x to 2x+2)
#for their color you call the array/dictionary/file that stores the colormatrix from Matlab
#you draw the wedges inside the loop but update the window outside the loop? 

my_matrix= loadmat('./colormatrix.mat')

my_colormatrix=my_matrix['colormatrix']

#parameters that users will be able to define, for now arbitrary values

#size of the wheel
my_size = [16,16]

#size of the inner disc
center_size = [11, 11]

#the angle at which the progam starts building the wheel
start=random.randint(1, 360)

for x in xrange (0, 180):
    
    colorwheel = visual.RadialStim(win=mywin, units='deg', size=my_size, radialCycles=0, angularCycles=0,
        radialPhase=0, angularPhase= 0, ori= start, texRes = 50, angularRes=300, visibleWedge=(0, 360-2*x),
        color= tuple(my_colormatrix[x-1]), colorSpace='rgb255', contrast=1.0, opacity=1.0, depth=0, 
        rgbPedestal=(0, 0, 0), interpolate=False)
    colorwheel.draw()
    x=x+1
   
middle_circle = visual.RadialStim(win=mywin, units='deg', size= center_size, radialCycles=0, angularCycles=0,
        radialPhase=0, angularPhase= 0, ori= start, texRes = 50, angularRes=300, visibleWedge=(0, 360),
        color= (126,126,126), colorSpace='rgb255', contrast=1.0, opacity=1.0, depth=0, 
        rgbPedestal=(0, 0, 0), interpolate=False)
middle_circle.draw()

mywin.update()  

#pause, so you get a chance to see it!
core.wait(5.0)