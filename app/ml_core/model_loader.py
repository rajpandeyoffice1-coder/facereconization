from insightface.app import FaceAnalysis

_app = None

def load_models():
    global _app

    if _app is not None:
        return _app

    try:
        _app = FaceAnalysis(
            name="buffalo_l", 
            root="./models",
            providers=["CPUExecutionProvider"]
        )

        _app.prepare(ctx_id=-1, det_size=(224, 224))

        print("InsightFace models loaded successfully")

    except Exception as e:
        print("Model loading failed:", str(e))
        raise RuntimeError(f"Model loading failed: {e}")

    return _app
