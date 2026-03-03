import numpy as np

def cosine_similarity(v1, v2):
    v1, v2 = np.array(v1), np.array(v2)
    return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

def match_faces(live_emb, ref_emb):
    score = cosine_similarity(live_emb, ref_emb)

    if score > 0.65:
        return "ok", score

    return "mismatch", score
