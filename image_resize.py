# Program : image_resize
# Description : Resize the image for the prediction
# Date : 01/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import cv2
import numpy as np


def image_resize(image: np.ndarray, width: int = None, height: int = None, inter: int = cv2.INTER_AREA) -> np.ndarray:

    dimension = None
    ratio: float
    (current_height, current_width) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        ratio = height / float(current_height)
        dimension = (int(current_width * ratio), height)

    else:
        ratio = width / float(current_width)
        dimension = (width, int(current_height * ratio))

    return cv2.resize(image, dimension, interpolation=inter)