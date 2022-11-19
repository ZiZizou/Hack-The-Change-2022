from fastai.vision.all import * 
import os
import pathlib
temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath

model_path = os.path.join(os.getcwd(),'waste_class_model.pkl')
learn = load_learner(model_path)
result = learn.predict(os.path.join(os.getcwd(), "diapers.jpg"))
print(result)