import cv2

image = cv2.imread('mei.jpg')
cv2.imshow('Image', image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()

