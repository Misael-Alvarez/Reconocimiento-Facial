from cv2 import cv2
import numpy as np

valorGauss=1 
valorKernel=7
original=cv2.imread('pesosmex.jpg')
gris=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY) # Escala de grises
gauss=cv2.GaussianBlur(gris, (valorGauss,valorGauss), 0) # Descenfoque
canny=cv2.Canny(gauss, 60,100) # Contornos de la moneda
kernel=np.ones((valorKernel,valorKernel),np.uint8) # trabajar matrices con enteros de 8 bites 
cierre=cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel) # Cierre de los contornos

contornos, jerarquía=cv2.findContours(cierre.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print("monedas encontradas: {}".format(len(contornos))) 
cv2.drawContours(original, contornos, -1, (0,0,255),2)
#Mostrar resultados
#cv2.imshow("Grises",gris)
#cv2.imshow("Gauss",gauss)
#cv2.imshow("canny",canny)
#cv2.imshow("cierre",cierre)

cv2.imshow("Resultado", original)
cv2.waitKey(0)