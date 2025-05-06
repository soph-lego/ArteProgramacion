#Sophia Leñero Gómez A01639462
import cv2
import numpy as np
import easyocr

lector = easyocr.Reader(['es'])

placa1 = cv2.imread("C:\\Users\\sophi\\Desktop\\TEC\\semanaTecProgra\\placa_q.jpg")
placa2 = cv2.imread("C:\\Users\\sophi\\Desktop\\TEC\\semanaTecProgra\\placa_2.jpg")

def leerPlaca(placa):
    #ponemos a escala de grises
    gris = cv2.cvtColor(placa, cv2.COLOR_BGR2GRAY)
    
    #le ponemos rudio
    _, mask = cv2.threshold(gris, 130, 255, cv2.THRESH_BINARY_INV)

    #filtro gaussiano
    blur = cv2.GaussianBlur(mask, (13, 13), 0)

    #para facilitarle al OCR 
    invertida = cv2.bitwise_not(blur)

    #TEXTO!
    resultados = lector.readtext(invertida)
    soloTexto = [texto for _, texto, conf in resultados if conf > 0.5]
    letras = [texto for _, texto, conf in resultados if conf > 0.5]
    print("Texto filtrado:", "".join(letras))
    cv2.imshow("Imagen procesada", invertida)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
leerPlaca(placa1)
leerPlaca(placa2)
