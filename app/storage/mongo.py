from pymongo import MongoClient


client = MongoClient("mongodb+srv://rajpandeyoffice1_db_user:Skf3AFFZagRvFsvm@mepsc.5cmxwbn.mongodb.net/?appName=MEPSC")
db = client["face_ml"]
faces = db["faces"]