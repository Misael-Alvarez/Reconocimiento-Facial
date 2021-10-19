import cv2 as cv
capturaVideo=cv.VideoCapture(1) # 0 interna / 1 externa
if not capturaVideo.isOpenend():
    print('No se encontro una camara')
    exit()
while True:
    tipocamara,camara = capturaVideo.read()
    grises = cv.cvtColor(camara,cv.COLOR_BGR2GRAY) # Mostrar camara de python en escalas de grises
    cv.imshow("Camara",camara)
    if cv.waitKey(1)==ord('q'):
        break
capturaVideo.release()
cv.destroyAllWindows()