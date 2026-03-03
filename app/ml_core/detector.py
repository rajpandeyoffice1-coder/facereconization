from app.ml_core.model_loader import load_models


model = load_models()


def detect_faces(image):
    return model.get(image)