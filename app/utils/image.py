import base64
import cv2
import numpy as np


def base64_to_image(base64_str):
    data = base64.b64decode(base64_str.split(",")[1])
    arr = np.frombuffer(data, np.uint8)
    return cv2.imdecode(arr, cv2.IMREAD_COLOR)