from insightface.app import FaceAnalysis
import os
import shutil

_app = None

def load_models():
    global _app

    if _app is not None:
        return _app

    model_root = os.path.expanduser("~/.insightface/models")
    model_path = os.path.join(model_root, "buffalo_l")

    try:
        # 🔥 If model folder exists but corrupted, remove it
        if os.path.exists(model_path):
            print("🧹 Cleaning existing model folder...")
            shutil.rmtree(model_path)

        _app = FaceAnalysis(
            name="buffalo_l",
            root=model_root,
            providers=["CPUExecutionProvider"]
        )

        _app.prepare(ctx_id=-1, det_size=(224, 224))

        print("✅ InsightFace CPU models loaded successfully")

    except Exception as e:
        print("❌ Model loading failed:", str(e))
        raise RuntimeError(f"Model loading failed: {e}")

    return _app