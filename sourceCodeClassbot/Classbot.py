import cv2 as cv
import numpy as np

class Classbot :
    def __init__(self,main_img,temp_img):
        self.mainimg = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        

    def search(self)  :
        result =   cv.matchTemplate(self.mainimg,self.temp_img,cv.TM_CCOEFF_NORMED)
        _,maxvalue,_,maxloc = cv.minMaxLoc(result)
        print(maxvalue)
        print(maxloc)

        threshold = 0.9

        if maxvalue >= threshold:
            topleft = maxloc
            print(self.temp_img.shape)
            
            #ระบุความกว้างความสูง
            height = self.temp_img.shape[0]
            width = self.temp_img.shape[1]
            
            #กำหนดตำแหน่งที่จะวาดรูปสี่เหลี่ยม
            buttomright = (topleft[0]+width,topleft[1]+height)

            #วาดรูปสี่เหลี่ยม 
            cv.rectangle(self.mainimg,topleft,buttomright,color=(97,189,92) , thickness=4, lineType= cv.LINE_4)

            
            #ใส่ตัวหนังสือ
            font = cv.FONT_ITALIC
            #ตำแหน่ง
            position = (topleft[0]+30,topleft[1]-5)
            fontsize = 0.5
            color = (255,0,255)
            cv.putText(self.mainimg,"TEST",position,font,fontsize,color,thickness=2)

            cv.imshow('result',self.mainimg)
            cv.waitKey()
            cv.destroyAllWindows()

mybot = Classbot('image/peple.jpg','image/temp.jpg')    
mybot.search()        