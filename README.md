# 🚦 Smart Traffic Management System

An AI-powered traffic control solution that dynamically manages traffic signals based on real-time vehicle detection using YOLO.

---

## 📌 1. Overview

The **Smart Traffic Management System** is an intelligent traffic control system that dynamically adjusts signal timings using computer vision. Leveraging the YOLO (You Only Look Once) object detection algorithm, it monitors traffic density in each lane and optimizes green light durations in real time.

---

## 🚀 2. Features

### ✅ 2.1 Dynamic Traffic Light Adjustment
- YOLO-based vehicle detection to count cars per lane.
- Automatically adjusts green light duration based on real-time vehicle density.

### 🎥 2.2 Real-Time Video Processing
- Supports live webcam feeds and pre-recorded traffic videos.
- Continuously detects vehicles and recalculates signal durations.

### 🖥️ 2.3 Tkinter GUI Interface
- User-friendly interface to monitor and control the system.
- Displays live traffic stats, allows toggling between automatic and manual modes.


---

## ⚙️ 3. Installation

### 🧱 3.1 Prerequisites

Ensure Python 3.x is installed. Then, install all dependencies:

## 📦 3.2 Setting Up YOLO Model

Download the pre-trained YOLO model (e.g., YOLOv8 weights) and place it in the `models/` directory.

---

## ▶️ 4. Usage

Run the main script:

5. Project Structure
graphql
Copy
Edit
SmartTrafficManagement/
│
├── src/                # Core scripts for detection and traffic control
├── gui/                # GUI implementation using Tkinter
├── models/             # YOLO model files (weights and configs)
├── config/             # Configuration files for YOLO and traffic logic
├── data/               # Sample traffic videos
├── main.py             # Main entry point for the application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
⚙️ 6. Technical Implementation

🚗 6.1 Vehicle Detection (YOLO-based)
Utilizes YOLOv5 for fast and accurate vehicle detection.

Performs frame-by-frame analysis to compute vehicle density per lane.

The function Calculate_traffic_timing calculates the green light timing for four lanes based on the number of vehicles detected in each lane. Here's a breakdown of how it works, plus a cleaned-up version with comments and enhancements:

🔍 Function Explanation
Inputs:

lane1, lane2, lane3, lane4: Number of vehicles in each respective lane.

root: The Tkinter root window (which is destroyed when the function is called, likely to switch to a new window).

Logic:

If a lane has more than 5 vehicles, each vehicle above 5 adds threshold_timing seconds (default is 5 sec) to the base time of 30 sec.

Cap: No lane gets more than 120 seconds of green light.

🖱️ 6.3 GUI Control System
Built using Tkinter

Displays:

Lane-wise vehicle count

Recommended green light times

Allows manual override of signal durations

🌐 7. Future Enhancements
🔌 IoT integration for real-world deployment with physical traffic lights

🧠 Reinforcement learning for more adaptive and intelligent signal control

🚑 Emergency vehicle and pedestrian detection for prioritization



