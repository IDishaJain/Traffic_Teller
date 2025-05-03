from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  # Import CORS
import os
import subprocess
import json  # Import the json module
from werkzeug.utils import secure_filename

app = Flask(__name__, static_folder='uploads')
CORS(app)  # Enable CORS for all routes

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov'}
OUTPUT_VIDEO_NAME = 'out.mp4'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def process_video(input_path, output_path):
    """
    Processes the video using the vehicle detection script and saves the output.
    """
    try:
        command = ['python', './Programs/main.py', '--input_video', input_path, '--output_video', output_path]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout
        errors = result.stderr
        if errors:
            print(f"Error from main.py: {errors}")
        try:
            data = json.loads(output)  # Attempt to parse JSON output from main.py
        except json.JSONDecodeError:
            data = {'output': output}  # If not JSON, return raw output
        return data, errors
    except subprocess.CalledProcessError as e:
        print(f"CalledProcessError: {e.stderr}")
        return None, e.stderr
    except Exception as e:
        print(f"Exception during processing: {str(e)}")
        return None, str(e)

@app.route('/upload-video', methods=['POST'])  # Consistent route name
def upload_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video file provided'}), 400
    file = request.files['video']
    if file.filename == '':
        return jsonify({'error': 'No video file selected'}), 400
    if file and allowed_file(file.filename):
        input_filename = secure_filename(file.filename)
        input_filepath = os.path.join(app.config['UPLOAD_FOLDER'], input_filename)
        output_filepath = os.path.join(app.config['UPLOAD_FOLDER'], OUTPUT_VIDEO_NAME)
        file.save(input_filepath)

        output_data, errors = process_video(input_filepath, output_filepath)

        if errors:
            return jsonify({'error': f'Error processing video: {errors}'}), 500

        return jsonify({
            'message': 'Video processed successfully',
            'data': output_data,
            'video_url': f'/uploads/{OUTPUT_VIDEO_NAME}'
        }), 200
    return jsonify({'error': 'Invalid file format'}), 400

@app.route('/get-results', methods=['GET'])  # Separate route for results
def get_results():
    try:
        with open('results.json', 'r') as f:  # Load results from file
            results = json.load(f)
        return jsonify(results), 200
    except FileNotFoundError:
        return jsonify({'error': 'Results not found'}), 404
    except Exception as e:
        return jsonify({'error': f'Error fetching results: {str(e)}'}), 500

@app.route('/uploads/<filename>')
def serve_uploaded_video(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True, port=8000)