from app.ml_core.model_loader import load_models

_model = None

def get_model():
    global _model
    if _model is None:
        _model = load_models()
    return _model

def detect_faces(image):
    model = get_model()
    return model.get(image)