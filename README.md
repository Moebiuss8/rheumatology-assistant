# Rheumatology Assistant

A web application to assist rheumatologists with probability calculations and reference management.

## Features

- Pre-test and post-test probability calculations
- Reference management for rheumatological conditions
- Voice transcription support
- Interactive normogram visualization

## Project Structure

The project is divided into two main parts:

- Backend (Flask)
- Frontend (React)

## Setup

### Backend

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Create a .env file with your API keys

4. Run the server:
```bash
python app.py
```

### Frontend

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm start
```

## Testing

Run backend tests:
```bash
cd backend
python -m pytest
```

## License

MIT
