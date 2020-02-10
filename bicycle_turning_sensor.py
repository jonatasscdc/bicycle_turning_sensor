# Add your Python code here. E.g.
from microbit import * 


##Getting current position from de built-in accelerometer
gesture = accelerometer.current_gesture()

#Executing the instructions while moving
while True:

    gesture = accelerometer.current_gesture()


    if gesture == 'right':
        display.show(Image.ARROW_E) #Showing an right arrow when turning to the right side 
    
    if gesture == 'left':
        display.show(Image.ARROW_W) #Showing a left arrow when turning to the left side
    

### Known basic problems:
    ##1: The device does not show anything while staying still. (solved)
    ##2:            does not show a cross                     . You have to configure the condition for 
    ### accelerometer to be with no moving. (issue)


### Advanced problems:
    ##1: We have to turn bicycle too much for the device to show the arrows. (issue)
            ## Solution: 
               # Maybe if we get just the x axis position and calibrate it firstly be 1g,
               # we can put inside the if condition a slight change to its value. 
