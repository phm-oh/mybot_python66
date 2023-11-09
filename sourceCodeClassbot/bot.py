from windowCapture import *
import cv2  as cv

windows = WindowCapture('Media Player')
# print(windows)
screen = windows.screenshot()
# print(screen)
# cv.imshow('test',screen)
# cv.waitKey()
# cv.destroyAllWindows()