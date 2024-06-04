import cv2
import numpy as np

person_1 = cv2.imread("Input/person_1.jpg")
person_2 = cv2.imread("Input/person_2.jpg")

# person_1=cv2.cvtColor(person_1,cv2.COLOR_BGR2GRAY)
# person_2=cv2.cvtColor(person_2,cv2.COLOR_BGR2GRAY)

resized_person_1 = cv2.resize(person_1, (person_2.shape[1], person_2.shape[0]))

resized_person_1 = resized_person_1.astype(np.float32)
person_2 = person_2.astype(np.float32)

morph_25_person_1 = (resized_person_1 * 0.25) + (person_2 * 0.75)
morph_50_person_1 = (resized_person_1 * 0.5) + (person_2 * 0.5)
morph_75_person_1 = (resized_person_1 * 0.75) + (person_2 * 0.25)

morph_25_person_1 = morph_25_person_1.astype(np.uint8)
morph_50_person_1 = morph_50_person_1.astype(np.uint8)
morph_75_person_1 = morph_75_person_1.astype(np.uint8)


combined_image = np.concatenate(
    (person_1 ,morph_75_person_1 ,morph_50_person_1,morph_25_person_1, person_2),
    axis=1
)

cv2.imwrite("Output/combined_image.jpg", combined_image)
