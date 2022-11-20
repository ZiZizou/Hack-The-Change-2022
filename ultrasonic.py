import RPi.GPIO as GPIO
import time

GPIO_TRIGGER_POS1 = 18
GPIO_ECHO_POS1 = 24


#GPIO_TRIGGER_POS3 = 29
#GPIO_ECHO_POS3 = 31

def ultrasonicInit():
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BOARD)
     
    #set GPIO Pins
     
    #set GPIO direction (IN / OUT) for object detection @ position 1
    GPIO.setup(GPIO_TRIGGER_POS1, GPIO.OUT)
    GPIO.setup(GPIO_ECHO_POS1, GPIO.IN)
    #set GPIO direction (IN / OUT) for object detection @ position 2
    # GPIO.setup(GPIO_TRIGGER_POS2, GPIO.OUT)
    # GPIO.setup(GPIO_ECHO_POS2, GPIO.IN)
    #set GPIO direction (IN / OUT) for object detection @ position 3
    # GPIO.setup(GPIO_TRIGGER_POS3, GPIO.OUT)
    # GPIO.setup(GPIO_ECHO_POS3, GPIO.IN)
    ##set GPIO direction (IN / OUT) for object detection @ position 4
    #GPIO.setup(GPIO_TRIGGER_POS4, GPIO.OUT)
    #GPIO.setup(GPIO_ECHO_POS4, GPIO.IN)

 
def objDetectionPos1(detection_threshold):

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER_POS1, 1)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER_POS1, 0)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO_POS1) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO_POS1) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    #distance here is measured in cm.
    #to return 'true' if the distance is less than or equal to 3cm... 
    if distance <= detection_threshold:
        return True
        
    return False


# def objDetectionPos2(detection_threshold):

#     # set Trigger to HIGH
#     GPIO.output(GPIO_TRIGGER_POS2, 1)
 
#     # set Trigger after 0.01ms to LOW
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER_POS2, 0)
 
#     StartTime = time.time()
#     StopTime = time.time()
 
#     # save StartTime
#     while GPIO.input(GPIO_ECHO_POS2) == 0:
#         StartTime = time.time()
 
#     # save time of arrival
#     while GPIO.input(GPIO_ECHO_POS2) == 1:
#         StopTime = time.time()
 
#     # time difference between start and arrival
#     TimeElapsed = StopTime - StartTime
#     # multiply with the sonic speed (34300 cm/s)
#     # and divide by 2, because there and back
#     distance = (TimeElapsed * 34300) / 2

#     #distance here is measured in cm.
#     #to return 'true' if the distance is less than or equal to 3cm... 
#     if distance <= detection_threshold:
#         return True
        
#     return False

# def objDetectionPos3(detection_threshold):

#     # set Trigger to HIGH
#     GPIO.output(GPIO_TRIGGER_POS3, 1)
 
#     # set Trigger after 0.01ms to LOW
#     time.sleep(0.00001)
#     GPIO.output(GPIO_TRIGGER_POS3, 0)
 
#     StartTime = time.time()
#     StopTime = time.time()
 
#     # save StartTime
#     while GPIO.input(GPIO_ECHO_POS3) == 0:
#         StartTime = time.time()
 
#     # save time of arrival
#     while GPIO.input(GPIO_ECHO_POS3) == 1:
#         StopTime = time.time()
 
#     # time difference between start and arrival
#     TimeElapsed = StopTime - StartTime
#     # multiply with the sonic speed (34300 cm/s)
#     # and divide by 2, because there and back
#     distance = (TimeElapsed * 34300) / 2

#     #distance here is measured in cm.
#     #to return 'true' if the distance is less than or equal to 3cm... 
#     if distance <= detection_threshold:
#         return True
        
#     return False
    

def objectDetection(detection_threshold):
    if(objDetectionPos1(detection_threshold)):
        return True
    return False
    
def GPIO_Clean():
    GPIO.cleanup()