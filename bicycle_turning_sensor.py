#Importing microbit's main libraries:
from microbit import * 


#Executing the instructions while moving:
while True:
    
    ##Getting current position from the built-in accelerometer:
    gesture = accelerometer.get_x()

    if gesture > 450:
        display.show(Image.ARROW_E, loop=False, delay=50) #Showing an right arrow when turning to the right side 
    
    elif gesture < -450:
        display.show(Image.ARROW_W, loop=False, delay=50) #Showing a left arrow when turning to the left side
        
    else:
        display.show(Image.NO) #If none of the conditions above are satisfied, the device will show a cross (staying still)


### Known basic problems:
    ##1: The device does not show anything while staying still. (solved)
    ##2:            does not show a cross                     . You have to configure the condition for 
    ### accelerometer to be with no moving. (solved)


### Advanced problems:
    ##1: We have to turn bicycle too much for the device to show the arrows. (partially solved)
    
            ## Solution: 
               # Maybe if we get just the x axis position and calibrate it firstly be 1g,
               # we can put inside the if condition a slight change to its value. 
                
               # We still have the calibration problem. Fixing the gesture value to specific ones should work wonderfully.

    
