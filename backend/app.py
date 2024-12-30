from flask import Flask
from flask_cors import CORS
from routes.probabilities import probabilities_bp
from routes.references import references_bp
from routes.transcription import transcription_bp

app = Flask(__name__)
CORS(app)

# Register blueprints
app.register_blueprint(probabilities_bp, url_prefix='/api/probabilities')
app.register_blueprint(references_bp, url_prefix='/api/references')
app.register_blueprint(transcription_bp, url_prefix='/api/transcription')

if __name__ == '__main__':
    app.run(debug=True)