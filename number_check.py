from PIL import Image 
import pytesseract 
import cv2


img = cv2.imread('data2.png')
print(pytesseract.image_to_string('data2.png'))

