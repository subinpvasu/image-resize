import cv2
import glob

images = glob.glob("*.jpg")
for img in images:
    print(img)
    im = cv2.imread(img)
    res = cv2.resize(im,(120,100))
    cv2.imshow("Hey", res)
    cv2.imwrite("resized"+img, res)
