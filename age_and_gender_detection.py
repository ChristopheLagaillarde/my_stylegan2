# Program : age_and_gender_detection
# Description : detect age and gender in an image
# Date : 26/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

import cv2
import numpy as np
from get_faces import get_faces
from get_gender_predictions import get_gender_predictions
from get_age_predictions import get_age_predictions
from image_resize import image_resize


def predict_age_and_gender(input_path: str) -> str:

    # Variables
    frame_width: int = 1280
    gender_list: list = ['Male', 'Female']
    age_intervals: list = ['(0, 2)', '(4, 6)', '(8, 12)', '(15, 20)',
                           '(25, 32)', '(38, 43)', '(48, 53)', '(60, 100)']
    label: str
    img: np.ndarray = cv2.imread(input_path)
    frame: np.ndarray = img.copy()

    if frame.shape[1] > frame_width:
        frame = image_resize(frame, width=frame_width)
    faces: list = get_faces(frame)

    for i, (start_x, start_y, end_x, end_y) in enumerate(faces):
        face_img: np.ndarray = frame[start_y: end_y, start_x: end_x]
        age_preds: np.ndarray = get_age_predictions(face_img)
        gender_preds: np.ndarray = get_gender_predictions(face_img)
        i: np.intc = gender_preds[0].argmax()
        gender: str = gender_list[i]
        gender_confidence_score: np.float32 = gender_preds[0][i]
        i = age_preds[0].argmax()
        age: str = age_intervals[i]
        age_confidence_score: np.float32 = age_preds[0][i]
        label = f"{gender}-{gender_confidence_score*100:.1f}%, {age}-{age_confidence_score*100:.1f}%"
        cv2.destroyAllWindows()

        return label
