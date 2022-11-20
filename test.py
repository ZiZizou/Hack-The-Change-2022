from fastai.vision.all import * 
import os
from cam_cv2 import *
#import pathlib
#temp = pathlib.PosixPath
#pathlib.PosixPath = pathlib.WindowsPath
camera = camInit()
model_path = os.path.join(os.getcwd(),'./models/waste_class_model_2.pkl')
clickPicture(camera,"test.jpg")
learn = load_learner(model_path)
result = learn.predict(os.path.join(os.getcwd(), "test.jpg"))
barcode_result = "00"
barcode_counter = 0
while(barcode_result=="00" and barcode_counter<50):
    barcode_result = read_barcodes(camera)
    barcode_counter = barcode_counter + 1
print(barcode_result)
print(result)
exitCam(camera)