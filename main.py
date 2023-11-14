from windowCapture import *
import cv2  as cv
from myClassbot import *
from time import time


windows = WindowCapture('LDPlayer')
# # print(windows)
# screen = windows.screenshot()
# # print(screen)
# # print(screen)
# # cv.imshow('test',screen)
# # cv.waitKey()
# # cv.destroyAllWindows()

# #start bot
# search = Classbot(screen,'image/chrome.jpg')
# point = search.search(debug=True,mytext="Icon" ,threshold=0.4)


# ------------ทำการวน Loop-----------------
looptime = time()
while True:
    screen = windows.screenshot()
    search = Classbot(screen,'image/aaa.jpg')
    point = search.search(debug=True,mytext="Icon" )
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllwindows()
        break