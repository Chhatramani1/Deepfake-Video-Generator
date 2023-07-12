# Deepfake-Video-Generator

This repository contains a Python script for automatically generating deepfake videos with celebrity faces. The script allows users to choose any celebrity and merge their face onto different video clips, creating realistic and convincing deepfake content. It includes advanced algorithms and techniques to seamlessly blend the faces and adjust for lighting and facial expressions.

## Requirements

To run the script, you need to have the following dependencies installed:

- Python 3
- OpenCV
- dlib
- NumPy
- imutils

You can install these dependencies by running the following command:

```
pip install opencv-python dlib numpy imutils
```

In addition, you need to download the pre-trained face detection model `shape_predictor_68_face_landmarks.dat` from the [dlib website](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2) and place it in the project directory.

## Usage

1. Clone this repository to your local machine or download the script file (`deepfake_generator.py`) directly.

2. Prepare the input video and celebrity face image:
   - Create or obtain an input video file (e.g., `input_video.mp4`) on which you want to apply the deepfake effect.
   - Choose a celebrity face image (e.g., `celebrity_face.jpg`) that you want to replace the faces in the input video with. Make sure the image has a clear and forward-facing view of the celebrity's face.

3. Update the script:
   - Replace the `input_video.mp4` and `celebrity_face.jpg` with your own files.
   - Modify any other settings or parameters in the script according to your requirements.

4. Run the script:
   - Open a terminal or command prompt.
   - Navigate to the project directory.
   - Run the following command:

     ```
     python deepfake_generator.py
     ```

   - The script will start processing the video frames, detect faces, perform the face swap with the celebrity face, and display the resulting deepfake video in a separate window.
   - Press `q` to stop the script and close the video window.

## Disclaimer

Please use this script responsibly and ethically. Deepfake technology can be misused, leading to privacy concerns and potential harm to individuals. Respect the privacy and rights of others when creating and sharing deepfake content. Be mindful of the potential consequences and adhere to applicable laws and regulations.

## License

This project is licensed under the [MIT License](LICENSE).

