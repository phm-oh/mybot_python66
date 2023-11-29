from windowCapture import *
import cv2  as cv
from myClassbot import *
from time import time
from pyautogui import click


windows = WindowCapture('WHACK EM ALL - Play this Game Online for Free Now! | Poki - Profile 1 - Microsoft​ Edge')
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
    search = Classbot(screen,'image/nose_case1.jpg')
    point = search.search(debug=True,mytext="Icon",acc=0.5 )
    
    #ทำตอนต่อเกมแล้ว ติดตั้ง pyautoguiclick  py -m pip install autogui
    for myclick in point:
        click(x=myclick[0],y=myclick[1])
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllwindows()
        break