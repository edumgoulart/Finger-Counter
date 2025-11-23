# Finger Counter Project

A real-time hand tracking and finger counting application using MediaPipe and OpenCV, with both desktop and web interfaces.

## Features

- **Real-time hand tracking** using MediaPipe
- **Finger counting** for up to 2 hands simultaneously
- **Desktop application** with OpenCV display
- **Web interface** with FastAPI backend and modern HTML/CSS/JS frontend
- **Live webcam processing** with visual feedback

## Attribution

This project uses and adapts MIT-licensed code from the open-source repository:

**MediaPipe-Project** — https://github.com/pranjalchanda08/MediaPipe-Project

Original code created and maintained by Pranjal Chanda.  
The original MIT License is preserved in the `LICENSE` file.

Additional modifications by **Eduardo Goulart (2025)**.

## Installation

### 1. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

### 2. Install dependencies

**Linux:**
```bash
pip install -r requirement_linux.txt
```

**Windows:**
```bash
pip install -r requirement_win.txt
```

## Usage

### Desktop Application

Run the finger counter with OpenCV display:

```bash
python project/finger_counter.py
```

- Press `Q` to quit

### Web Interface

#### 1. Start the backend server

```bash
uvicorn backend.main:app --reload --port 8000
```

Or using the virtual environment:

```bash
.venv/bin/uvicorn backend.main:app --reload --port 8000
```

#### 2. Open the frontend

Open `frontend/index.html` in your web browser, or run:

```bash
xdg-open frontend/index.html  # Linux
# or
open frontend/index.html  # Mac
# or
start frontend/index.html  # Windows
```

#### 3. Use the interface

1. Click **"Start Camera"** to begin
2. Allow webcam access when prompted
3. The interface will show your webcam feed with hand tracking overlays and finger count
4. Click **"Stop Camera"** to end the session

## Project Structure

```
FingerCountProject/
├── backend/
│   └── main.py              # FastAPI backend server
├── frontend/
│   └── index.html           # Web interface
├── project/
│   └── finger_counter.py    # Desktop application
├── utils/
│   └── hand_tracking.py     # Hand tracking module
├── gallery/                 # Sample images/videos
├── requirement_linux.txt    # Linux dependencies
├── requirement_win.txt      # Windows dependencies
└── README.md
```

## Technologies

- **MediaPipe** - Hand tracking and landmark detection
- **OpenCV** - Image processing and display
- **FastAPI** - Web backend framework
- **HTML/CSS/JavaScript** - Web frontend

## License

MIT License - See `LICENSE` file for details.