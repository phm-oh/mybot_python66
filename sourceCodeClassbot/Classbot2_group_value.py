import cv2 as cv
import numpy as np

class Classbot :
    def __init__(self,main_img,temp_img):
        self.mainimg = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        

    def search(self)  :
        result =   cv.matchTemplate(self.mainimg,self.temp_img,cv.TM_CCOEFF_NORMED)

        _,maxvalue,_,maxloc = cv.minMaxLoc(result)

        acc = 0.95
            
        locations = np.where(result >= acc)  
        locations = list(zip(*locations[::-1])) 

        # print(locations) 

        height =self.temp_img.shape[0]
        width =self.temp_img.shape[1]

        rectangle = []
        for loc in locations:
            rect = [int(loc[0]),int(loc[1]),width,height]
            rectangle.append(rect)
            rectangle.append(rect)
        # print(rectangle)
        rex,weights = cv.groupRectangles(rectangle,groupThreshold=1,eps=0.5)
        # print(rex)
        exit
        print(len(rex)) 
        if len(rex):
            for (x,y,w,h) in rex:
                # print(x,y,w,h)
                topleft = (x,y)
                bottomright = ( x+w , y+h )
                # print(topleft)
                print(bottomright)
                cv.rectangle(self.mainimg,topleft,bottomright,color=(255,0,255),thickness=2 , lineType=cv.LINE_8)  

        cv.imshow('result',self.mainimg)
        cv.waitKey()
        cv.destroyAllWindows()
        exit
            

mybot = Classbot('image/Screenshot3test.jpg','image/box.jpg')    
mybot.search()        