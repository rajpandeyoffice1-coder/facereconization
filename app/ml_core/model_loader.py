from insightface.app import FaceAnalysis
import os

_app = None

def load_models():
    global _app
    if _app is None:
        model_root = os.path.expanduser("~/.insightface/models")

        _app = FaceAnalysis(
            name="antelopev2",
            root=model_root,
            providers=["CPUExecutionProvider"]   # 🔥 CPU ONLY
        )

        _app.prepare(ctx_id=-1, det_size=(224, 224))  # smaller = faster

        print("✅ InsightFace CPU models loaded")

    return _app