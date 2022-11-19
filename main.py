from model import *
import time
from ultrasonic import objectDetection
from cam_cv2 import *
import RPi.GPIO as GPIO		#import GPIO modulea
from app import isRecyclable

if __name__ == '__main__':

	learn = loadClassifier()  #load the model in the learn variable
	cam_capture = camInit()  #load capture into the code
	filename = "image.jpg"  #constant filename for saving image to be classified
	print("Initializing operations...")
    sampleNum = 3
	recycle_avg = 0
	organic_avg = 0
	non_recycle_avg = 0
	GPIO.setmode(GPIO.BOARD)	#pin numbers are as specified on the board

    #led/transistor1 gpio setup
	GPIO.setup(LEDbin1, GPIO.OUT)
    #led/transistor2 gpio setup
	GPIO.setup(LEDbin2, GPIO.OUT)
    #led/transistor3 gpio setup
	GPIO.setup(LEDbin3, GPIO.OUT)
    #led/transistor4 gpio setup
	GPIO.setup(LEDbin4, GPIO.OUT)
  
	try:
		while(True):
	        #take picture
			if(objectDetection()):
				print("taking pics...")
				for x in range(sampleNum):
					clickPicture(cam_capture, filename)
					prediction = predict(filename, learn)
					recycle_avg += prediction[2]
					organic_avg += prediction[1]
					non_recycle_avg += prediction[0]

				recycle_avg /= sampleNum
				organic_avg /= sampleNum
				non_recycle_avg /= sampleNum

                barcode_result = "00"
                barcode_counter = 0
                while(barcode_result=="00" and barcode_counter<50):
                    barcode_result = read_barcodes(cam_capture)
                    barcode_counter++
                print(barcode_result)
                #make call to api and send barcode result

				if(recycle_avg > organic_avg and recycle_avg > non_recycle_avg):
					print("Waste is recyclable")

					if(barcode_result != "00"):
						recylableRebateResult = isRecyclable(barcode_result[1:])
						if(recylableRebateResult):
							GPIO.output(LEDbin1, GPIO.LOW)
							GPIO.output(LEDbin2, GPIO.HIGH)
							GPIO.output(LEDbin3, GPIO.LOW)
							GPIO.output(LEDbin4, GPIO.LOW)
						else:
							GPIO.output(LEDbin1, GPIO.LOW)
							GPIO.output(LEDbin2, GPIO.LOW)
							GPIO.output(LEDbin3, GPIO.HIGH)
							GPIO.output(LEDbin4, GPIO.LOW)							


				elif(organic_avg > recycle_avg and organic_avg > non_recycle_avg):
					print("Waste is organic")
					GPIO.output(LEDbin1, GPIO.HIGH)
					GPIO.output(LEDbin2, GPIO.LOW)
					GPIO.output(LEDbin3, GPIO.LOW)
					GPIO.output(LEDbin4, GPIO.LOW)
				elif(non_recycle_avg > recycle_avg and non_recycle_avg > organic_avg):
					print("Waste is non recyclable")
					GPIO.output(LEDbin1, GPIO.LOW)
					GPIO.output(LEDbin2, GPIO.LOW)
					GPIO.output(LEDbin3, GPIO.LOW)
					GPIO.output(LEDbin4, GPIO.HIGH)


  
	except KeyboardInterrupt:
		print("Operation stopped by User")
		motor_exit()
		GPIO.cleanup()
		exitCam(cam_capture)
