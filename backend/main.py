import sys
import os
import cv2
import numpy as np
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
import io

# Add the parent directory to sys.path to allow importing utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.hand_tracking as ht

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize HandTracking
track = ht.HandTracking(min_detection_confidence=0.8, min_tracking_confidence=0.8)

@app.post("/process_image")
async def process_image(file: UploadFile = File(...)):
    # Read image file
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Flip image horizontally (mirror effect)
    flip_image = cv2.flip(img, 1)

    # Track hands
    track.find_hand(flip_image)
    track.find_finger_tips(
        flip_image,
        finger_list=None,
        show_connected=True,
        show_landmarks=True,
        draw_tips=False,
        hand_id_list=[0, 1]
    )
    
    # Count fingers
    finger_up_dict = track.is_finger_up(flip_image, hand_id_list=[0, 1])
    total = sum(finger_up_dict.get('0', [])) + sum(finger_up_dict.get('1', []))
    
    # Draw count on image
    cv2.putText(flip_image, "{}".format(total), (flip_image.shape[1] - 150, 150),
                cv2.FONT_HERSHEY_PLAIN, 7, (0, 0, 255), 6)

    # Encode image back to JPEG
    _, encoded_img = cv2.imencode('.jpg', flip_image)
    return StreamingResponse(io.BytesIO(encoded_img.tobytes()), media_type="image/jpeg")
