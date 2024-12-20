# Eye Blink Detection and Alert System

This project detects when a person's eyes are closed for a certain period (5 seconds) and plays an alarm sound with a text message ("في حاجة، انك هتنام، اصحي!"). It uses a webcam to capture video frames and analyze eye aspect ratio (EAR) to determine eye closure.

## Features
- Detects eye closure using the Eye Aspect Ratio (EAR) method.
- Plays an alarm sound when eyes are closed for 5 seconds.
- Displays a message on the screen to alert the user.
- Uses `OpenCV`, `dlib`, `pygame`, and `scipy`.

## Dependencies

The following Python libraries are required to run this project:

- `opencv-python`: For capturing video frames and processing images.
- `dlib`: For detecting facial landmarks and analyzing the eyes.
- `pygame`: For playing the alarm sound.
- `scipy`: For calculating distances between eye landmarks.

### Install Dependencies

To install the necessary libraries, create a virtual environment and install the dependencies from the `requirements.txt` file:

```bash
# Create a virtual environment (optional)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install required dependencies
pip install -r requirements.txt
