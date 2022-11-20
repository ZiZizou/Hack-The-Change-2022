from fastai.vision.all import *
from pathlib import Path

def loadClassifier():
    model_path = Path('./models')
    learn = load_learner('./models/waste_class_model.pkl')
    return learn

def predict(image, classifier):
    image_path = Path('./'+image)
    return classifier.predict(image_path)[2].tolist()