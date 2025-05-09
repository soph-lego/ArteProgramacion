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
        if conf > 0.5:
            # polígono de overlay
            puntos = np.array([bbox[0], bbox[1], bbox[2], bbox[3]], dtype=np.int32)

            #  overlay semitransparente
            overlay = imagen_ar.copy()
            cv2.fillPoly(overlay, [puntos], color=(0, 0, 0))
            alpha = 0.5
            cv2.addWeighted(overlay, alpha, imagen_ar, 1 - alpha, 0, imagen_ar)

            # Calcular punto para texto (mitad superior del bbox)
            centro = np.mean(puntos, axis=0).astype(int)
            x_texto, y_texto = centro[0], centro[1] - 10

            # Dibujar texto encima (bordes suaves tipo AR)
            cv2.putText(imagen_ar, texto, (x_texto, y_texto), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (255, 255, 255), 2, cv2.LINE_AA)  # sombra clara
            cv2.putText(imagen_ar, texto, (x_texto, y_texto), cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 0, 0), 1, cv2.LINE_AA) 

      

    """
    resultados = lector.readtext(invertida)
    soloTexto = [texto for _, texto, conf in resultados if conf > 0.5]
    letras = [texto for _, texto, conf in resultados if conf > 0.5]
    print("Texto filtrado:", "".join(letras))
    cv2.imshow("Imagen", invertida)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    """
    
graffitiLeer(graffiti1)
graffitiLeer(graffiti2)
graffitiLeer(graffiti3)
