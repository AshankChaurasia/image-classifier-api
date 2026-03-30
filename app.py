from flask import Flask,request ,jsonify
import os
from model import predict

app=Flask(__name__)

UPLOAD_FOLDER="uploads"

ALLOWED_EXTENSIONS={"jpeg","jpg","png","webp","webp"}

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

def allowed_files(filename):
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/predict",methods=["POST"])
def classify():


    if "image" not in request.files:
        return jsonify({"error":"No image provided"}),400
    
    file= request.files["image"]
    
    if not allowed_files(file.filename):
        return jsonify({"error": "File type not allowed"}), 400
    
    path =os.path.join(UPLOAD_FOLDER,file.filename)
    
    file.save(path)

    result =predict(path)
    
    return jsonify(result)


@app.route("/",methods=["GET"])
def home():
    return jsonify({"message":"Image Classifier API is running "})

if __name__ == "__main__":
    app.run(debug=True)