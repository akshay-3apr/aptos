import numpy as np
import pandas as pd
import os
import scipy as sp
# from functools import partial
from sklearn import metrics
from collections import Counter
import json
from PIL import Image
import requests, os
from io import BytesIO
from fastai import *
from fastai.vision import *
from sklearn.metrics import cohen_kappa_score
import fastai

class APTOS:

    def getLabel(self,pred,coef):
        label = ["No DR","Mild","Moderate","Severe","Proliferative DR"]
        ind = 0
        if pred < coef[0]:
            ind = 0
        elif pred >= coef[0] and pred < coef[1]:
            ind = 1
        elif pred >= coef[1] and pred < coef[2]:
            ind = 2
        elif pred >= coef[2] and pred < coef[3]:
            ind = 3
        else:
            ind = 4
        return label[ind]

    def predict(self,image):
        try:
            learn = load_learner('model')
            img = open_image(BytesIO(image))
            pred_class, pred_idx, outputs = learn.predict(img)
            label = APTOS().getLabel(pred_idx.item(),[0.504171,1.597531,2.416886,3.305622])
            return label
        except Exception as e:
            with open('predictLog.txt','w') as f:
                f.write(str(e))