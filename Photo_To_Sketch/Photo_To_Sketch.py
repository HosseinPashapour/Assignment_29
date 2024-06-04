import cv2 

img  = cv2.imread("Input\person.jpg" )
img = cv2.resize(img , [570 , 480])
img = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)


inverted  = cv2.bitwise_not(img)
blur = cv2.GaussianBlur(inverted , (21,21) , 0 , 0 )
final = cv2.divide(img,255-blur,scale=256)


cv2.imshow("Hilari_Sketch" , final)
cv2.imwrite("Output/Hilari.jpg" , final)
cv2.waitKey()