from app.ml_core.detector import detect_faces
import cv2

def extract_embedding(image):
    faces = detect_faces(image)

    if faces is None or len(faces) == 0:
        return None, "no_face"

    if len(faces) > 1:
        return None, "multiple_faces"

    face = faces[0]

    # bounding box size check (too far)
    x1, y1, x2, y2 = map(int, face.bbox)
    w = x2 - x1
    h = y2 - y1

    if w < 60 or h < 60:
        return None, "too_far"

    # blur check
    face_crop = image[y1:y2, x1:x2]
    gray = cv2.cvtColor(face_crop, cv2.COLOR_BGR2GRAY)
    blur_val = cv2.Laplacian(gray, cv2.CV_64F).var()

    if blur_val < 60:
        return None, "blurry"

    return face.embedding.tolist(), "ok"
