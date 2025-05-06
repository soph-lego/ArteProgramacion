#Sophia Leñero Gómez A01639462
import cv2
import numpy as np
import random

def agregar_ruido_salt_pepper(img, cantidad=0.2):
    row, col = img.shape
    num_pixels_sal = int(cantidad * row * col / 2)
    num_pixels_pimienta = int(cantidad * row * col / 2)

    #pixeles blancos
    for _ in range(num_pixels_sal):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord, x_coord] = 255

    #pixeles negros 
    for _ in range(num_pixels_pimienta):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord, x_coord] = 0

    return img

img = cv2.imread("C:/Users/sophi/Desktop/TEC/semanaTecProgra/machape.jpg", cv2.IMREAD_GRAYSCALE)
img_ruido = agregar_ruido_salt_pepper(img.copy(), cantidad=0.2)

imgGauss=cv2.GaussianBlur(img_ruido, (5, 5), 0)
imgAV=cv2.blur(img_ruido, (3, 3))

imgGaussColor = cv2.cvtColor(imgGauss, cv2.COLOR_GRAY2BGR)
imgAVColor = cv2.cvtColor(imgAV, cv2.COLOR_GRAY2BGR)

# Mostrar imagen con ruido
cv2.imshow("Imagen con ruido sal y pimienta", img_ruido)
cv2.imshow("Imagen con filtro de gauss", imgGaussColor)
cv2.imshow("Imagen con filtro av", imgAVColor)
cv2.waitKey(0)
cv2.destroyAllWindows()
