import cv2
import numpy as np

main_decoration = cv2.imread("input\pic_background.png").astype(np.float32)
new_forground = cv2.imread("input\pic_foreground.png").astype(np.float32)
mask = cv2.imread("input\pic_room_mask.png") / 255

result = np.multiply(new_forground, mask)
result = np.add(result, np.multiply(main_decoration, 1-mask)).astype(np.uint8)


cv2.imshow('Room with New Floor',result)
cv2.imwrite("output/Virtual_Decoration.jpg", result)
cv2.waitKey()