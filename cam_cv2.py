import cv2	#import the cv2 library
from barcode import read_barcodes

#camInit
#does : reinitializes the camera
#requires : nothing
#returns : returns capture object
def camInit():
	#open camera
	cap = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L)

	#set dimensions
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)
	return cap

#clickPicture
#does : takes a picture using cap object and writes to ./fileName.jpg
#requires : capture object and fileName
#returns : nothing
def clickPicture(cap, fileName):
	ret, frame = cap.read()
	cv2.imwrite(fileName , frame)

def getBarCodes(cap):
    ret,frame = cap.read()
    barcode = "00"
    if(ret):
        barcode = read_barcodes(frame)
    return barcode

#exitCam
#does : releases capture object. Will need to call camInit fot a new capture object after this
#requires : nothing
#returns : nothing
def exitCam(cap):
	cap.release()