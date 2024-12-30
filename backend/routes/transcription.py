from flask import Blueprint, request, jsonify
import whisper
from utils.config import config

transcription_bp = Blueprint('transcription', __name__)

@transcription_bp.route('/', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
        
    try:
        # Save temporary file
        temp_path = 'temp_audio'
        file.save(temp_path)
        
        # Load Whisper model and transcribe
        model = whisper.load_model('base')
        result = model.transcribe(temp_path)
        
        # Clean up
        os.remove(temp_path)
        
        return jsonify({'transcription': result['text']})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500