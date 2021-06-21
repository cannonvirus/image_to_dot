
import cv2
import numpy as np
from PIL import Image

import os
import natsort
import re

path_dir = 'Y:/DL_data_big/EdgeFarm_pig/poly_extract/누끼/'
file_list = os.listdir(path_dir)
sorted_list = natsort.natsorted(file_list)

f = open('answer.txt','a')


answer_sheet = []

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print("마우스 이벤트 발생, x:", x ," y:", y)
        # cv2.circle(img,(x,y),100,(255,0,0),-1)
        answer_sheet.append([x,y])

want_number = [100,200]

for idx, file_naming in enumerate(sorted_list):
    numbering = int(re.split('_', file_naming)[0])
    if numbering >= want_number[0] and numbering <= want_number[1]:
        print("NUMBER : {}".format(numbering))
        

        while(1):
            path = path_dir + file_naming
            image_pil = Image.open(path)
            img = np.array(image_pil)
            cv2.namedWindow('image')
            cv2.setMouseCallback('image', draw_circle)
            cv2.imshow('image',img)
            if cv2.waitKey(20) & 0xFF == 27:
                if len(answer_sheet) == 3:
                    f.write(str(answer_sheet)+"\n")
                    f.flush()
                    answer_sheet = []
                    break
                else:
                    cv2.destroyAllWindows()
                    answer_sheet = []
        cv2.destroyAllWindows()









