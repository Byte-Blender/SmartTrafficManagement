Smart Traffic Management System

1. Overview

The Smart Traffic Management System is an AI-powered solution that dynamically controls traffic lights based on real-time vehicle detection. It uses YOLO (You Only Look Once) to detect vehicles and optimize green light durations per lane based on traffic density.

2. Features

2.1 Dynamic Traffic Light Adjustment

Uses YOLO-based car detection to analyze vehicle count in each lane.

Adjusts green light duration dynamically based on real-time traffic conditions.


2.2 Real-Time Video Processing

Supports live video feeds and recorded video for traffic analysis.

Detects vehicles in each lane and calculates optimal traffic signal durations.


2.3 Tkinter GUI Interface

A user-friendly graphical interface for controlling the system.

Displays live traffic statistics and allows users to switch between modes.


2.4 Manual Input Support

Users can override the automatic system to manually adjust signal timings.



---

3. Installation

3.1 Prerequisites

Ensure that you have Python 3.x installed. Then install the required dependencies:

pip install -r requirements.txt

3.2 Setting Up YOLO Model

Download the pre-trained YOLO model and place it inside the models/ directory.


---

4. Usage

1. Run the main script:

python main.py


2. Select video mode or manual mode via the Tkinter GUI.


3. The system will analyze traffic density and adjust signals accordingly.




---

5. Project Structure

SmartTrafficManagement/
│── src/                # Core scripts for traffic detection and signal control
│── gui/                # Tkinter GUI implementation
│── models/             # Pre-trained YOLO models
│── config/             # Configuration files for model and traffic settings
│── data/               # Sample traffic videos for testing
│── main.py             # Main execution script
│── requirements.txt    # List of dependencies
│── README.md           # Documentation


---

6. Technical Implementation

6.1 Vehicle Detection (YOLO-based)

Uses a pre-trained YOLOv5 model for real-time car detection.

Extracts vehicle count from each lane and assigns signal durations accordingly.


6.2 Traffic Light Optimization Algorithm

Calculates green light duration based on vehicle count:


T_{green} = \frac{N_{vehicles} \times T_{unit}}{Total\ Vehicles}

 = Number of vehicles in a lane

 = Base unit time per vehicle

 = Sum of all detected vehicles


6.3 GUI Control System

Built using Tkinter.

Displays vehicle count, recommended green light times, and allows manual override.



---

7. Future Enhancements

Integration with IoT-based traffic signal controllers for real-world deployment.

Implementation of reinforcement learning for more adaptive traffic control.

Adding pedestrian and emergency vehicle detection for priority control.



---

8. Contributing

Contributions are welcome!

1. Fork the repository.


2. Create a new branch for your feature (git checkout -b feature-name).


3. Commit changes (git commit -m "Added feature").


4. Push to GitHub and create a pull request.
