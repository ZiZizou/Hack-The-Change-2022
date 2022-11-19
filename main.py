from model import *
import time
from ultrasonic import objectDetection
from cam_cv2 import *


if __name__ == '__main__':

	learn = loadClassifier()  #load the model in the learn variable
	cam_capture = camInit()  #load capture into the code
	filename = "image.jpg"  #constant filename for saving image to be classified
	print("Initializing operations...")
    sampleNum = 3
	recycle_avg = 0
	organic_avg = 0
	non_recycle_avg = 0

    #led/transistor1 gpio setup
    #led/transistor2 gpio setup
    #led/transistor3 gpio setup
    #led/transistor4 gpio setup
  
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

				if(recycle_avg > organic_avg and recycle_avg > non_recycle_avg):
					print("Waste is recyclable")


				elif(organic_avg > recycle_avg and organic_avg > non_recycle_avg):
					print("Waste is organic")



				elif(non_recycle_avg > recycle_avg and non_recycle_avg > organic_avg):
					print("Waste is non recyclable")

                barcode_result = "00"
                barcode_counter = 0
                while(barcode_result=="00" and barcode_counter<50):
                    barcode_result = read_barcodes(cam_capture)
                    barcode_counter++
                print(barcode_result)
                #make call to api and send barcode result


  
	except KeyboardInterrupt:
		print("Operation stopped by User")
		motor_exit()
		GPIO.cleanup()
		exitCam(cam_capture)
