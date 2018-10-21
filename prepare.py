path = 'C:\\Users\\akash\\Pictures\\Sign-Language-Digits-Dataset-master\\Dataset\\'
import os
from PIL import Image

for i in range(3):
    for filename in os.listdir(path + str(i)):
        if filename != "":
            image_obj = Image.open(path + str(i) + "\\" + filename).convert('L')
            rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
            rotated_image.save(path + "grayscale\\" + str(i) + "\\r_" + filename)
            image_obj.save(path + "grayscale\\" + str(i) + "\\" + filename)

for filename in os.listdir(path + "invalid"):
        if filename != "":
            image_obj = Image.open(path + "invalid" + "\\" + filename).convert('L')
            rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
            rotated_image.save(path + "grayscale\\" + "invalid" + "\\r_" + filename)
            image_obj.save(path + "grayscale\\" + "invalid" + "\\" + filename)