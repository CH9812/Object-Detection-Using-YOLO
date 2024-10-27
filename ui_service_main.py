# ui_backend.py
from flask import Flask, request, render_template, jsonify
import os
import json
from ai_backend import AIDetector


app = Flask(__name__, static_folder='output')
ai_detector = AIDetector()

UPLOAD_FOLDER = 'upload_image'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    # Render the upload form
    return render_template("index.html")
    return render_template("index.html", detection_data=data, detected_image=detected_image_filename, json_path=json_path)


@app.route("/predict_img", methods=["POST"])
def predict_img():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    f = request.files['file']
    filepath = os.path.join(UPLOAD_FOLDER, f.filename)
    f.save(filepath)

    file_extension = f.filename.rsplit('.', 1)[1].lower()
    if file_extension not in ['jpg', 'jpeg', 'png']:  # Support for multiple formats
        return jsonify({"error": "Only JPG and PNG files are supported"}), 400

    # Get JSON output and detected image path from AI backend
    json_path, detected_image_path = ai_detector.predict_image(filepath)
    

    # Load JSON data to return as response
    with open(json_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Ensure the detected image path is accessible for rendering
    detected_image_filename = os.path.basename(detected_image_path)
    
    return render_template("index.html", detection_data=data, detected_image=detected_image_filename)

    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    
    

    

