from sklearn.svm import LinearSVC
import numpy as np 
import cv2 as cv
import PIL

class Model:

    def __init__(self):
        self.model = LinearSVC()

    def train_model(self, counters):
        img_list = np.array([])
        class_list = np.array([])

        for i in range(1, counters[0]):
            img = cv.imread(f'1/frame{i}.jpg')[:,:,0]
            img = img.reshape(16800)