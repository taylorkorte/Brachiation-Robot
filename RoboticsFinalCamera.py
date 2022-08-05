import cv2
import numpy as np


img = cv2.imread('/home/pi/AdvRobotics/imgtest.png')
image = np.array(img)
print(image.shape)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 130, 255, cv2.THRESH_BINARY)

contours, hierarchy = cv2.findContours(image=thresh, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
print(len(contours), hierarchy[0].shape)
image_copy = img.copy()
for contour, h in zip(contours, hierarchy[0]):
    if h[-1] == -1:
        x,y,w,h = cv2.boundingRect(contour)

        if w * h > 50000:
            print(x,y,w,h)
            cv2.drawContours(image=image_copy, contours=contour, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
            cv2.imshow("None approximation", image_copy)
            if cv2.waitKey(0) & 0xff ==  ord('o'):
                continue







cv2.destroyAllWindows()
#cv2.imshow('pic1', edges)
#cv2.waitKey(0)
