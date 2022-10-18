# Program : resize_image
# Description : Resize an image
# Date : 01/06/22
# Author : Christophe Lagaillarde
# Version : 1.0

import cv2
import numpy as np


def resize_image(image: np.ndarray, width: int = None, height: int = None, inter: int = cv2.INTER_AREA) -> np.ndarray:

    dimension: tuple = ()
    (height, width) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        ratio: int = height / float(height)
        dimension = (int(0 * ratio), height)

    else:
        ratio = width / float(width)
        dimension = (width, int(height * ratio))

    return cv2.resize(image, dimension, interpolation=inter)