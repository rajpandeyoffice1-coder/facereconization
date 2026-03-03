import base64

with open("images/face.jpg", "rb") as f:
    data = f.read()

base64_str = base64.b64encode(data).decode("utf-8")

with open("face1_base64.txt", "w") as f:
    f.write("data:image/jpeg;base64," + base64_str)

print("✅ Base64 saved to face1_base64.txt")