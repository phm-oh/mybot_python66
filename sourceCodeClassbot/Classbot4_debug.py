import cv2 as cv
import numpy as np

class Classbot :
    def __init__(self,main_img,temp_img):
        self.mainimg = cv.imread(main_img,cv.IMREAD_ANYCOLOR)
        self.temp_img = cv.imread(temp_img,cv.IMREAD_ANYCOLOR)
        
   #เพิ่มการ ดีบัค
    def search(self , acc=0.9 ,debug=False)  :
        result =   cv.matchTemplate(self.mainimg,self.temp_img,cv.TM_CCOEFF_NORMED)

        _,maxvalue,_,maxloc = cv.minMaxLoc(result)

        acc = 0.95
            
        locations = np.where(result >= acc)  
        locations = list(zip(*locations[::-1])) 

        

        height =self.temp_img.shape[0]
        width =self.temp_img.shape[1]

        rectangle = []
        for loc in locations:
            rect = [int(loc[0]),int(loc[1]),width,height]
            rectangle.append(rect)
            rectangle.append(rect)
        

        point = []
        rex,weights = cv.groupRectangles(rectangle,groupThreshold=1,eps=0.5)
       
        exit
        
        if len(rex):
            for (x,y,w,h) in rex:
                #แก้ไขส่วนนี้ 
                topleft = (x,y)
                bottomright = ( x+w , y+h )
                centerX = x + int(w /2 )
                centerY = y + int(h /2)
                point.append((centerX,centerY))

                if debug:
                    cv.rectangle(self.mainimg,topleft,bottomright,color=(255,0,255),thickness=2 , lineType=cv.LINE_8) 
                    cv.drawMarker(self.mainimg,(centerX,centerY),color=(0,222,255),thickness=2,markerSize=50,markerType=cv.MARKER_DIAMOND)
                
        else:
            print("ไม่เจอรูปภาพ")

        if debug: 
           print(point)
           cv.imshow('result',self.mainimg)
           cv.waitKey()
           cv.destroyAllWindows()
        return point
            

mybot = Classbot('image/Screenshot3test.jpg','image/box.jpg')    
mypoint = mybot.search(debug=True)  
# print(mypoint) 
# for myclick in mypoint:
#     print(myclick)