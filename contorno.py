import cv2 
imagen = cv2.imread('contorno.jpg') # Imprimimos imagen
grises = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY) # Convertir imagen a escala de grises
_,umbral = cv2.threshold(grises,100,255,cv2.THRESH_BINARY) # Modificar la escala de grieses de la imagen
contorno, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagen,contorno,-1,(251,63,52),3) # Reconocimiento de contornos

#Mostrar
cv2.imshow('imagen original',imagen)
cv2.imshow('imagen grises',grises)
cv2.imshow('imagen umbral',umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()
