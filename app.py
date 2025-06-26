from flask import Flask, request, send_from_directory, jsonify
from flask_cors import CORS
import os
import uuid
from filters import apply_filter  # This imports the function to apply filters

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests from frontend

# === Use absolute path to the 'static/processed' folder ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROCESSED_FOLDER = os.path.join(BASE_DIR, 'static', 'processed')

# Create the folder if it doesn't exist
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Generate a unique filename for the uploaded image
    filename = str(uuid.uuid4()) + ".png"
    file_path = os.path.join(PROCESSED_FOLDER, filename)

    # Save the uploaded image temporarily
    file.save(file_path)

    # Get the selected filter type from the frontend
    filter_type = request.form.get('filter')

    # Apply the selected filter to the image
    filtered_image_path = apply_filter(file_path, filter_type)

    # Return the filtered image's filename to the frontend
    return jsonify({'filename': os.path.basename(filtered_image_path)})


@app.route('/processed/<filename>', methods=['GET'])
def get_processed_image(filename):
    return send_from_directory(PROCESSED_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
