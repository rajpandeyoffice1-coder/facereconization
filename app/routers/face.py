from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.image import base64_to_image
from app.ml_core.embedder import extract_embedding
from app.ml_core.matcher import match_faces
from app.storage.mongo import faces

router = APIRouter()

class RegisterReq(BaseModel):
    examId: str
    imageBase64: str

class VerifyReq(BaseModel):
    examId: str
    imageBase64: str


@router.post("/register")
def register_face(req: RegisterReq):
    try:
        img = base64_to_image(req.imageBase64)
        if img is None:
            return {"status": "error", "reason": "invalid_image"}

        emb, status = extract_embedding(img)

        if status != "ok":
            return {"status": status}

        faces.update_one(
            {"examId": req.examId},
            {"$set": {"embedding": emb}},
            upsert=True
        )

        return {"status": "ok"}

    except Exception as e:
        print("REGISTER ERROR:", e)
        return {"status": "error", "reason": str(e)}


@router.post("/verify")
def verify_face(req: VerifyReq):
    try:
        doc = faces.find_one({"examId": req.examId})
        if not doc:
            return {"status": "no_reference"}

        ref_emb = doc["embedding"]

        img = base64_to_image(req.imageBase64)
        if img is None:
            return {"status": "error", "reason": "invalid_image"}

        live_emb, status = extract_embedding(img)

        if status != "ok":
            return {"status": status}

        match_status, score = match_faces(live_emb, ref_emb)

        return {
            "status": match_status,
            "score": round(score, 3)
        }

    except Exception as e:
        print("VERIFY ERROR:", e)
        return {"status": "error", "reason": str(e)}
