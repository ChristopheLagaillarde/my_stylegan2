# Program : get_faces
# Description : Found the human face in an image
# Date : 26/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

import cv2
import numpy as np


def get_faces(frame: np.ndarray, confidence_threshold: float = 0.5) -> list:

    # Variables
    face_proto: str = "weights/deploy.prototxt.txt"
    face_model: str = "weights/res10_300x300_ssd_iter_140000_fp16.caffemodel"
    face_net: cv2.dnn_Net = cv2.dnn.readNetFromCaffe(face_proto, face_model)
    blob: np.ndarray = cv2.dnn.blobFromImage(frame, 1.0, (300, 300), (104, 177.0, 123.0))
    faces: list = []

    face_net.setInput(blob)
    output: np.ndarray = np.squeeze(face_net.forward())

    for i in range(output.shape[0]):
        confidence: np.ndarray = output[i, 2]

        if confidence > confidence_threshold:
            box: np.ndarray = output[i, 3:7] * \
                np.array([frame.shape[1], frame.shape[0],
                         frame.shape[1], frame.shape[0]])
            start_x, start_y, end_x, end_y = box.astype(int)
            start_x, start_y, end_x, end_y = start_x - \
                10, start_y - 10, end_x + 10, end_y + 10

            start_x: int = 0 if start_x < 0 else start_x
            start_y: int = 0 if start_y < 0 else start_y
            end_x: int = 0 if end_x < 0 else end_x
            end_y: int = 0 if end_y < 0 else end_y
            faces.append((start_x, start_y, end_x, end_y))

    return faces
