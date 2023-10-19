import cv2 as cv
import numpy as np

class Classbot :
    def __init__(self,main_img,temp_img):
        self.mainimg = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        

    def search(self)  :
        result =   cv.matchTemplate(self.mainimg,self.temp_img,cv.TM_CCOEFF_NORMED)

        _,maxvalue,_,maxloc = cv.minMaxLoc(result)

        acc = 0.9
            
        locations = np.where(result >= acc)  
        locations = list(zip(*locations[::-1])) 

        print(locations) 

        if locations:
            height =self.temp_img.shape[0]
            width =self.temp_img.shape[1]
            
            for loc in locations:
                # print(loc)
                bottomright = (loc[0]+width,loc[1]+height)
                cv.rectangle(self.mainimg,loc,bottomright,color=(0, 255, 0) , thickness=4, lineType= cv.LINE_4)
                #ใส่ตัวหนังสือ
                font = cv.FONT_ITALIC
                #ตำแหน่ง
                position = (loc[0]+30,loc[1]-5)
                fontsize = 0.5
                color = (255,0,255)
                cv.putText(self.mainimg,"TEST",position,font,fontsize,color,thickness=2)
            cv.imshow('result',self.mainimg)
            cv.waitKey()
            cv.destroyAllWindows()


mybot = Classbot('image/Screenshot3test.jpg','image/box.jpg')    
mybot.search()        