import cv2

image = cv2.imread('mei.jpg')
edges = cv2.Canny(image, 100, 200)
cv2.imshow('Edges', edges)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
