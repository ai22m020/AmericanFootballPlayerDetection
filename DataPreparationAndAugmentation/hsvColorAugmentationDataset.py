import cv2 as cv
import numpy as np
from os import listdir
from os.path import isfile, join
from PIL import Image

# Purpose of this class is to create augmented hsv images.
# 3 Koordinated: Farbwert, Farbsättigung und Hellwert statt RGB

folders = ["../American-Football-Player/test/images"
          #,"../American-Football-Player/valid/images",
           #"../American-Football-Player/train/images"
           ]
for folder in folders:
    onlyfiles = [f for f in listdir(folder) if join(folder, f)]
    for fileName in onlyfiles:
        newLines = []
        img = cv.imread(folder+'/'+fileName)
        hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        cv.imwrite("../American-Football-Player-HSV/train/images/"+fileName, hsv)

# Tried to filter out green -> hard to filter out only the grass and not the players, especially when they have
# green jersey


# img = cv.imread("playerAug.jpg")
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
#
# # lower_green = np.array([36,0,0])
# # upper_green = np.array([86,255,255])
#
# # mask = cv.inRange(hsv, lower_green, upper_green)
#
# # mask_inv = cv.bitwise_not(mask)
#
# # res = cv.bitwise_and(img, img, mask=mask_inv)
# # cv.namedWindow("res", cv.WINDOW_NORMAL)
# cv.namedWindow("hsv", cv.WINDOW_NORMAL)
# # cv.imshow("res", res)
# cv.imshow("hsv", hsv)
#
# if cv.waitKey(0):
#     cv.destroyAllWindows()