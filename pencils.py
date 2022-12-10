import matplotlib.pyplot as plt
import cv2
import pathlib

pensils = 0
pensils_all = []
for i in range(1, 13):
    path = pathlib.Path(f"/Users/svetaparilova/Downloads/images/img ({i}).jpg")
    im = cv2.imread(str(path))
    im2 = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im2 = cv2.GaussianBlur(im2, (215,235), 0)
    _, thresh = cv2.threshold(im2, 140, 190, 0)
    contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    areas = []
    for i, contour in enumerate(contours):
        if i != 0:
            areas.append(cv2.contourArea(contour, True))
    for i in areas:
        if (i<500000) and (i>300000):
            pensils+=1
    pensils_all.append(pensils)
print('Count of pencils on all photos: ', pensils_all[-1])