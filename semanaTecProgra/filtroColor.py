#Sophia Leñero Gómez A01639462
import cv2 as cv
import numpy as np

#Importamos la imagen y la pasamos a HSV
bolas = cv.imread("C:\\Users\\sophi\\Desktop\\TEC\\semanaTecProgra\\pelotas.jpg")
bolasHSV = cv.cvtColor(bolas, cv.COLOR_BGR2HSV)

#rango de azul!!
lowerYellow = np.array([20, 100, 100])
upperYellow = np.array([30, 255, 255])

#creamos la máscara!!
mask = cv.inRange(bolasHSV, lowerYellow, upperYellow)
result = cv.bitwise_and(bolas, bolas, mask=mask)

cv.imshow("imagen original:", bolas)
cv.imshow("imagen con filtro:", result)
cv.waitKey(0)
cv.destroyAllWindows()