from windowCapture import *
import cv2  as cv
from myClassbot import *
windows = WindowCapture('vdo')
# print(windows)
screen = windows.screenshot()
# print(screen)
# print(screen)
# cv.imshow('test',screen)
# cv.waitKey()
# cv.destroyAllWindows()

#start bot
search = Classbot(screen,'image/target3.jpg')
point = search.search(debug=True)