
import cv2 as cv 
import numpy as np
# print(cv)
# print(np)

# read img
main_img = cv.imread('image/peple.jpg',cv.IMREAD_ANYCOLOR)
temp_img = cv.imread('image/temp.jpg',cv.IMREAD_ANYCOLOR)
# print(temp_img)
# print(main_img)
# print(type(temp_img))
# print(type(main_img))


result = cv.matchTemplate(main_img,temp_img,cv.TM_CCOEFF_NORMED)
# print(result)

# min,max,minloc,maxloc = cv.minMaxLoc(result)
_,maxvalue,_,maxloc = cv.minMaxLoc(result)

print(maxvalue)

print(maxloc)
threshold = 0.9

if maxvalue >= threshold:
    topleft = maxloc
    print(temp_img.shape)
    
    #ระบุความกว้างความสูง
    height = temp_img.shape[0]
    width = temp_img.shape[1]
     
    #กำหนดตำแหน่งที่จะวาดรูปสี่เหลี่ยม
    buttomright = (topleft[0]+width,topleft[1]+height)

     #วาดรูปสี่เหลี่ยม 
    cv.rectangle(main_img,topleft,buttomright,color=(97,189,92) , thickness=4, lineType= cv.LINE_4)

    
    #ใส่ตัวหนังสือ
    font = cv.FONT_ITALIC
    #ตำแหน่ง
    position = (topleft[0]+30,topleft[1]-5)
    fontsize = 0.5
    color = (255,0,255)
    cv.putText(main_img,"TEST",position,font,fontsize,color,thickness=2)

    cv.imshow('result',main_img)
    cv.waitKey()
    cv.destroyAllWindows()


