import cv2

image = cv2.imread('mei.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale', gray_image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
