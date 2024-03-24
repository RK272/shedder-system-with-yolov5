Shedder System with YOLOv5
This system is designed to detect hands and trigger an alert if a hand crosses a specified line drawn on the screen. It's intended to protect hands from machinery by automatically detecting hand movements and using a microcontroller to power off the machine if a hand crosses the boundary line.

Technology Used
YOLOv5 for object detection
Flask, OpenCV for the web application
Annotation and labeling tools like LabelImg
Installation
Make sure you have Python 3.11 installed on your system.
Clone this repository to your local machine.
bash
Copy code
git clone https://github.com/RK272/shedder-system-with-yolov5.git
Navigate to the project directory.
bash
Copy code
cd shedder-system-with-yolov5
Install the required Python packages using pip.
bash
Copy code
pip install -r requirements.txt
Download the pre-trained YOLOv5 model best.pt from the link provided or train your own model using Colab.
Usage
Run the Flask application.
bash
Copy code
python app.py
Access the web interface at http://localhost:5000 in your browser.
Follow the on-screen instructions to draw a line and interact with the system.
Additional Notes
Make sure to configure the microcontroller integration as per your hardware setup.
Customize the alert mechanism and actions as needed for your application.
Credits
YOLOv5: GitHub Repository
Flask: Official Website
OpenCV: Official Documentation
LabelImg: GitHub Repository
Feel free to customize and add more details to the README as per your project's requirements and specifications.







