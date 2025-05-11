"""
Sophia Leñero Gómez A01639462
Texto Callejero
"""
import cv2
import numpy as np
import easyocr

lector = easyocr.Reader(['es'])

graffiti1 = cv2.imread("C:\\Users\\sophi\\Desktop\\TEC\\evidencia1_arte_progra_slg\\luchaAbandona.jpg")
graffiti2 = cv2.imread("C:\\Users\\sophi\\Desktop\\TEC\\evidencia1_arte_progra_slg\\trains.jpg")
graffiti3 = cv2.imread("C:\\Users\\sophi\\Desktop\\TEC\\evidencia1_arte_progra_slg\\muroSuenos.jpg")

def graffitiLeer(graffiti):
    #escala de grises
    gris = cv2.cvtColor(graffiti, cv2.COLOR_BGR2GRAY)
    gris = cv2.equalizeHist(gris)

    #umbral adaptativo en vez de fijo
    mask = cv2.adaptiveThreshold(
        gris, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY_INV, 11, 2
    )

    #filtro gaussiano
    blur = cv2.GaussianBlur(mask, (13, 13), 0)
    #filtro para el OCR 
    invertida = cv2.bitwise_not(blur)

    resultados=lector.readtext(invertida)
    #para AR sobre la imagen og
    imagen_ar=graffiti.copy()

    for (bbox, texto, conf) in resultados:
        if conf > 0.3: #nivel de confianza del texto 
            # overlay semitransparente para poner el texto ahi!
            puntos = np.array([bbox[0], bbox[1], bbox[2], bbox[3]], dtype=np.int32)
            overlay = imagen_ar.copy()
            cv2.fillPoly(overlay, [puntos], color=(0, 0, 0))
            alpha = 0.5 #para marcar que tan fuerte esta el overlay
            cv2.addWeighted(overlay, alpha, imagen_ar, 1 - alpha, 0, imagen_ar)

            # Calcular punto para texto (mitad superior del bbox)
            centro = np.mean(puntos, axis=0).astype(int)
            x_texto, y_texto = centro[0], centro[1] - 10

            #para el texto del overlay
            cv2.putText(imagen_ar, texto, (x_texto, y_texto), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 0, 0), 3, cv2.LINE_AA)  # sombra negra
            cv2.putText(imagen_ar, texto, (x_texto, y_texto), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (255, 255, 255), 1, cv2.LINE_AA)  # texto blanco

    return imagen_ar

resultado1 = graffitiLeer(graffiti1)
resultado2 = graffitiLeer(graffiti2)
resultado3 = graffitiLeer(graffiti3)

# Mostrar imágenes
cv2.imshow("Graffiti 1", resultado1)
cv2.imshow("Graffiti 2", resultado2)
cv2.imshow("Graffiti 3", resultado3)

# Esperar a que se presione una tecla
cv2.waitKey(0)
cv2.destroyAllWindows()


