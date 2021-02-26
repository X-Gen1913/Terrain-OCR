import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('img.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))  # ...//printing data in image as a string

##...Detecting characters
print(pytesseract.image_to_boxes(img))
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])  # Cordinates(x.y) and dimensions(width and height) of the box
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)

cv2.imshow('Result', img)  # display image with boxes
cv2.waitKey(0)
