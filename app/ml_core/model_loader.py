from insightface.app import FaceAnalysis
import os

_app = None

def load_models():
    global _app

    # If already loaded, return it
    if _app is not None:
        return _app

    try:
        model_root = os.path.expanduser("~/.insightface/models")

        _app = FaceAnalysis(
            name="buffalo_l",  # 🔥 lighter & safer for Railway
            root=model_root,
            providers=["CPUExecutionProvider"]  # CPU only
        )

        # Smaller detection size = lower memory usage
        _app.prepare(
            ctx_id=-1,
            det_size=(224, 224)
        )

        print("✅ InsightFace CPU models loaded successfully")

    except Exception as e:
        print("❌ Failed to load InsightFace model:", str(e))
        raise RuntimeError(f"Model loading failed: {e}")

    return _app