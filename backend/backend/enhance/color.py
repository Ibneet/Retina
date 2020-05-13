import cv2
import numpy as np
import os
from django.http import HttpResponse
from django.http import HttpResponseRedirect

class color:

    def __init__(self):
        self.IMG_SIZE = 50
        self.CURRENT = "{}/color/".format(os.getcwd())

        if os.path.exists('{}.meta'.format(self.CURRENT)):
            print('EXISTING MODEL LOADED!!!')
        else:
            print('MODEL NOT EXIST!!!')

    def Gray(self, image):
        img = cv2.imread(image,0)
        blur = cv2.GaussianBlur(img,(5,5),0)
        # blur = "hi"
        # img_decoded = cv2.imdecode(img_np, cv2.IMREAD_GRAYSCALE)
        # img = cv2.resize(img_np, (self.IMG_SIZE, self.IMG_SIZE))
        # img_stream = np.array(img)
        # img_stream_preprosessed = img_stream.reshape(self.IMG_SIZE, self.IMG_SIZE, 1)
        return HttpResponse(blur,content_type="image/png")
       