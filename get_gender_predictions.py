# Program : get_gender_predictions
# Description : Tell the gender of a face picture
# Date : 26/05/22
# Auteur : Christophe Lagaillarde
# Version : 1.0

import numpy as np
import cv2


def get_gender_predictions(face_img: np.ndarray) -> np.ndarray:

    # Variables
    gender_model: str = 'weights/deploy_gender.prototxt'
    gender_proto: str = 'weights/gender_net.caffemodel'
    gender_net: cv2.dnn_Net = cv2.dnn.readNetFromCaffe(gender_model, gender_proto)
    model_mean_values: tuple = (78.4263377603, 87.7689143744, 114.895847746)
    blob: np.ndarray = cv2.dnn.blobFromImage(
        image=face_img, scalefactor=1.0, size=(227, 227),
        mean=model_mean_values, swapRB=False, crop=False
    )

    gender_net.setInput(blob)

    return gender_net.forward()
