import cv2
import numpy as np
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = Image.open('imgtest.jpg')
img.load()
i = pytesseract.image_to_string(img)
print(i)

with open('magic.txt', mode = 'w') as file:
    file.write(i)
    print('> see the magic file')
