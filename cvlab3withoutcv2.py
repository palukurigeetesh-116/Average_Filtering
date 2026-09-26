import numpy as np
import cv2
import matplotlib.pyplot as plt

def average_filter(image,kernel_size):
    pad=kernel_size//2
    padded=np.pad(image,pad,mode='constant')
    output=np.zeros_like(image)
    kernel=np.ones((kernel_size,kernel_size))/(kernel_size*kernel_size)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            region=padded[i:i+kernel_size,j:j+kernel_size]
            output[i,j]=np.sum(region*kernel)
    return output

img=cv2.imread('car.jpeg',0)

if img is None:
    print("Image not found")
else:
    sigma=15
    noise=np.random.normal(0,sigma,img.shape)
    noisy_img=img+noise
    noisy_img=np.clip(noisy_img,0,255).astype(np.uint8)

    blur3=average_filter(noisy_img,3)
    blur5=average_filter(noisy_img,5)
    blur7=average_filter(noisy_img,7)

    plt.figure(figsize=(12,8))

    plt.subplot(2,3,1)
    plt.imshow(img,cmap='gray')
    plt.title("Original")
    plt.axis("off")

    plt.subplot(2,3,2)
    plt.imshow(noisy_img,cmap='gray')
    plt.title("Noisy Image")
    plt.axis("off")

    plt.subplot(2,3,3)
    plt.imshow(blur3,cmap='gray')
    plt.title("3x3 Average Filter")
    plt.axis("off")

    plt.subplot(2,3,4)
    plt.imshow(blur5,cmap='gray')
    plt.title("5x5 Average Filter")
    plt.axis("off")

    plt.subplot(2,3,5)
    plt.imshow(blur7,cmap='gray')
    plt.title("7x7 Average Filter")
    plt.axis("off")

    plt.tight_layout()
    plt.show();