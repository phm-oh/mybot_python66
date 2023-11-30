from time import time
from windowCapture import *
from magicClassbot import *
import cv2  as cv


from pyautogui import click


windows = WindowCapture('LDPlayer')
looptime = time()
   

while True:
    screen = windows.screenshot()
    search = Classbot(screen)
    # point = search.search(debug=True , mytext='x' ,acc=0.7)
    # search.getColor(176,604)   
    search.getColor(170,573)
    # print(search.getColor(297,301,"0xC3C3C3") ) 
    
    if search.getColor(297,301,"0xC3C3C3") :
        print('found black color')
    else : 
        print('not found black color')  
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllwindows()
        break
    
    
