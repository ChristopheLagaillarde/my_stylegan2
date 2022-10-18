# Program : gat_age_predictions
# Description : give an age to the face image
# Date : 26/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

import cv2
import numpy as np


def get_age_predictions(face_img: np.ndarray) -> np.ndarray:

    # variables
    model_mean_values: tuple = (78.4263377603, 87.7689143744, 114.895847746)
    age_model: str = 'weights/deploy_age.prototxt'
    age_proto: str = 'weights/age_net.caffemodel'
    age_net: cv2.dnn_Net = cv2.dnn.readNetFromCaffe(age_model, age_proto)
    blob: np.ndarray = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=model_mean_values, swapRB=False
    )

    age_net.setInput(blob)

    return age_net.forward()