from windowCapture import *
import cv2  as cv
from myClassbot import *
from time import time
from pyautogui import click


windows = WindowCapture('Duck Hunt 🕹️ Play on CrazyGames - Profile 1 - Microsoft​ Edge')
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
    search = Classbot(screen,'image/duck1.png')
    duck1 = search.search(debug=True,mytext="Icon",acc=0.7 )
    
    #ทำตอนต่อเกมแล้ว ติดตั้ง pyautoguiclick  py -m pip install autogui
    for myclick in duck1:
        click(x=myclick[0],y=myclick[1])
        
        
        
    screen = windows.screenshot()
    search = Classbot(screen,'image/duck2.png')
    duck2 = search.search(debug=True,mytext="Icon",acc=0.7 )
    
    #ทำตอนต่อเกมแล้ว ติดตั้ง pyautoguiclick  py -m pip install autogui
    for myclick in duck2:
        click(x=myclick[0],y=myclick[1])    
        
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllwindows()
        break