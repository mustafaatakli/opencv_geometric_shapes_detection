import cv2
import numpy as np

image = cv2.imread("sekil.PNG")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    k_sayisi = cv2.approxPolyDP(contour, 0.04 * cv2.arcLength(contour, True), True)
    x, y, w, h = cv2.boundingRect(k_sayisi)
    ar = w / float(h)

    if len(k_sayisi) == 3:
        sekil = ("Ucgen")
    elif len(k_sayisi) == 4:
        if ar >= 0.95 and ar <= 1.05:
            sekil = "Kare"
        else:
            sekil = "Dikdortgen"
    else:
        sekil  = "Daire"

    cv2.putText(image, sekil , (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("Geometrik-Sekiller", image)
cv2.waitKey(0)
cv2.destroyAllWindows()