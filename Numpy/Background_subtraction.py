import numpy as np
from google . colab . patches import cv2_imshow
import cv2

bg1_image = cv2. imread ('Numpy\Img\Backgroud Image.png' , 1)
bg1_image = cv2. resize ( bg1_image , (678 , 381) )

ob_image = cv2 . imread ('Numpy\Img\Object Image.jpg', 1)
ob_image = cv2 . resize ( ob_image , (678 , 381) )

bg2_image = cv2. imread ('Numpy\Img\Target Background Image.jpg', 1)
bg2_image = cv2. resize ( bg2_image , (678 , 381) )
