# OpenCV Camera Rectangle Detector
This script utilizes the OpenCV library to access a camera device, such as a webcam, and detect rectangles in real-time video frames. However, it can be easily modified to work with any other camera. It allows you to dynamically add rectangles to the video feed by pressing the 'A' key. The script calculates the optimal number of rectangles that can fit in the frame based on its size.

## Features:
* Real-time video processing from the webcam or any other camera
* Adding rectangles to the frame
* Automatic positioning of rectangles based on available space
* Keyboard input for user interaction
* Modular functions for drawing rectangles and calculating positions

## Potential Applications:
* Object detection: Modify the code to perform real-time object detection using pre-trained models like YOLO or SSD.
* Face detection and recognition: Integrate face detection and recognition algorithms for identification and personalized experiences.
* Augmented Reality (AR): Overlay virtual objects or effects onto the webcam feed for interactive AR experiences.
* Pose estimation: Detect and track human poses in real-time, visualizing joints or providing visual feedback.
* Motion detection and tracking: Track moving objects by comparing consecutive frames, visualizing them with rectangles.
* Gesture recognition: Recognize hand gestures in real-time, visualizing them or providing user feedback.
* Human-Computer Interaction: Create interactive systems where user actions or gestures control applications or games.
  
## Prerequisites
* Python installed on your machine
* OpenCV library installed (pip install opencv-python)
  
## Usage
#### 1. Clone the repository to your local machine.
#### 2. Open the script file OpenCV-Camera-Rectangle-Detector.py in a text editor or integrated development environment (IDE) of your choice.
#### 3. Customize the following parameters based on your requirements:

* frame_width and frame_height:
  These parameters initialize the desired width and height of the video frame. You can modify these values to adjust the size of the displayed video frame.

* rectangle_width and rectangle_height:
  These parameters initialize the width and height of the rectangles that will be drawn on the video frame. Adjust these values to change the size of the rectangles.

* initial_gap_between_rectangles_height and initial_gap_between_rectangles_width:
  These parameters set the initial gap (in pixels) between the rectangles in the vertical and horizontal directions, respectively. Modify these values to change the initial spacing between the rectangles.

* gap_to_frame_sides_height and gap_to_frame_sides_width:
  These parameters determine the gap (in pixels) between the rectangles and the sides of the frame in the vertical and horizontal directions, respectively. Adjust these values to define the spacing between the rectangles and the frame edges.
  
#### 4. Make sure you have a webcam connected to your machine.
#### 5. Run the script by executing the following command:
`python OpenCV-Camera-Rectangle-Detector.py`
#### 6. A new window will open showing the webcam feed with any detected rectangles.
#### 7. Press the 'A' key to add a rectangle to the video feed.
#### 8. Press the 'Q' key to quit the script and close the windows.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
If you would like to contribute to this project, you can fork the repository and create a pull request with your changes. Please follow the contributing guidelines and adhere to the code of conduct.

Contact
If you have any questions or suggestions, feel free to contact the project maintainer at rana.shk.nz@gmail.com
