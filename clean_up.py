import cv2
import numpy as np


# creer une function de néttoyage pour que les images puisse etre traiter et avoir un filtre et une rotation
def clean_up(image, deg):
    cv2.namedWindow('image')
    # cv2.createTrackbar('val', 'image', 0, 255, nothing) 
    # cv2.createTrackbar('threshold', 'image', 0, 100, nothing)
    img = cv2.imread(image)  
    
    print(img)

    while True:
        height, width = img.shape[:2]
        (cX, cY) = (width // 2, height // 2)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        for i in range(height):
            for j in range(width):
                if np.random.randint(2) == 0:
                    gray[i, j] = min(gray[i, j] + np.random.randint(0,1), 255) # adding noise to image and setting values > 255 to 255. 
                else:
                    gray[i, j] = max(gray[i, j] - np.random.randint(0,1), 0) # subtracting noise to image and setting values < 0 to 0.
        cv2.imshow('Original', img)
        cv2.imshow('image', gray)
        
        M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
        rotated = cv2.warpAffine(gray, M, (width, height))
        
        cv2.imshow('rotate', rotated)

        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
    
clean_up('image/allan/p-0.png', 3)