# Program : display_image
# Description : display an image onscreen
# Date : 01/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import cv2
import numpy as np


def display_image(title: str, image_path: str) -> None:
    image_result = open("images/seed.png", "r")

    # Variable
    image: np.ndarray = cv2.imread(image_path)

    image = cv2.resize(image, (640, 640))
    cv2.imshow(title, image)
    cv2.setWindowProperty(title, cv2.WND_PROP_TOPMOST, 1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


    return None