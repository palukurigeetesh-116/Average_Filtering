import cv2
import matplotlib.pyplot as plt
import numpy as np

def show_comparison(original, blur3, blur5, blur7):
   
    plt.figure(figsize=(12, 10))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Grayscale Image')
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.imshow(blur_3x3, cmap='gray')
    plt.title('Average Filter (3×3)')
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.imshow(blur_5x5, cmap='gray')
    plt.title('Average Filter (5×5)')
    plt.axis('off')
    
    plt.subplot(2, 2, 4)
    plt.imshow(blur_7x7, cmap='gray')
    plt.title('Average Filter (7×7)')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()
img = cv2.imread('e_1.jpg', 0)

if img is None:
    print("Error: Image not found.")
else:
    kernel_3x3 = np.ones((3, 3), np.float32) / 9
    kernel_5x5 = np.ones((5, 5), np.float32) / 25
    kernel_7x7 = np.ones((7, 7), np.float32) / 49

    blur_3x3 = cv2.filter2D(img, -1, kernel_3x3)
    blur_5x5 = cv2.filter2D(img, -1, kernel_5x5)
    blur_7x7 = cv2.filter2D(img, -1, kernel_7x7)

    cv2.imwrite("blur_3x3.jpg", blur_3x3)
    cv2.imwrite("blur_5x5.jpg", blur_5x5)
    cv2.imwrite("blur_7x7.jpg", blur_7x7)

    show_comparison(img, blur_3x3, blur_5x5, blur_7x7)