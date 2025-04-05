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

### ✋ 2.4 Manual Input Support
- Users can override the AI decisions and manually set traffic light durations.

---

## ⚙️ 3. Installation

### 🧱 3.1 Prerequisites

Ensure Python 3.x is installed. Then, install all dependencies:

## 📦 3.2 Setting Up YOLO Model

Download the pre-trained YOLO model (e.g., YOLOv5 weights) and place it in the `models/` directory.

---

## ▶️ 4. Usage

Run the main script:


