import os
import cv2
import numpy as np

def ReduceNoise(file_path):
    images_path = os.listdir(file_path)

    images = []
    for image_path in images_path:
        image = cv2.imread(file_path + '/' + image_path)
        image = image.astype(np.float32)
        images.append(image)

    result = np.zeros(image.shape)
    for image in images:
        result += image

    result = result / len(images)
    result = result.astype(np.uint8)

    return result

result_1 = ReduceNoise('input/1')
result_2 = ReduceNoise('input/2')
result_3 = ReduceNoise('input/3')
result_4 = ReduceNoise('input/4')

row , col , band = result_1.shape
result = np.zeros((row*2 , col*2, band))

result[:row,:col,:] = result_1
result[:row,col:,:] = result_2
result[row:,:col,:] = result_3
result[row:,col:,:] = result_4


cv2.imwrite('output/black_hole_without_noise.jpg',result)
cv2.waitKey()