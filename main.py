
import cv2
import numpy as np

def main():
    img = cv2.imread('images/1.jpg')
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()