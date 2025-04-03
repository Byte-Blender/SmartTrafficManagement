<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Traffic Management System</title>
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; max-width: 800px; margin: auto; padding: 20px; }
        h1, h2, h3 { color: #333; }
        code { background: #f4f4f4; padding: 2px 5px; border-radius: 5px; }
        pre { background: #f4f4f4; padding: 10px; border-radius: 5px; overflow-x: auto; }
        ul { margin: 10px 0; padding-left: 20px; }
        .box { background: #f8f9fa; padding: 10px; border-left: 5px solid #007bff; margin-bottom: 10px; }
    </style>
</head>
<body>

    <h1>Smart Traffic Management System</h1>

    <p>The <strong>Smart Traffic Management System</strong> is an AI-powered solution that dynamically controls traffic lights based on real-time vehicle detection using <strong>YOLO (You Only Look Once)</strong>. It optimizes traffic flow by calculating green light durations based on vehicle density.</p>

    <h2>Features</h2>
    <ul>
        <li><strong>Real-Time Vehicle Detection:</strong> Uses YOLO for accurate vehicle counting.</li>
        <li><strong>Dynamic Signal Timing:</strong> Adjusts green light duration based on traffic density.</li>
        <li><strong>Tkinter GUI Interface:</strong> Provides a user-friendly control panel.</li>
        <li><strong>Manual Override Mode:</strong> Allows users to manually set signal durations.</li>
    </ul>

    <h2>Installation</h2>
    <h3>Prerequisites</h3>
    <p>Ensure <strong>Python 3.x</strong> is installed, then install dependencies:</p>
    <pre><code>pip install -r requirements.txt</code></pre>

    <h3>Setting Up YOLO Model</h3>
    <p>Download the <strong>pre-trained YOLO model</strong> and place it in the <code>models/</code> directory.</p>

    <h2>Usage</h2>
    <ol>
        <li>Run the main script:</li>
        <pre><code>python main.py</code></pre>
        <li>Select <strong>video mode</strong> or <strong>manual mode</strong> via the GUI.</li>
        <li>The system will analyze traffic density and adjust signals accordingly.</li>
    </ol>

    <h2>Project Structure</h2>
    <pre><code>
SmartTrafficManagement/
│── src/                # Core scripts for traffic detection and signal control
│── gui/                # Tkinter GUI implementation
│── models/             # YOLO model files
│── config/             # Configuration files
│── data/               # Sample traffic videos
│── main.py             # Main execution script
│── requirements.txt    # Dependencies
│── README.md           # Documentation
    </code></pre>

    <h2>How It Works</h2>
    <p><strong>1. Vehicle Detection:</strong> Uses <strong>YOLOv5</strong> to count vehicles in each lane.</p>
    <p><strong>2. Signal Optimization:</strong> Calculates green light duration using the formula:</p>
    <pre><code>T_green = (N_vehicles × T_unit) / Total_Vehicles</code></pre>
    <p><strong>3. GUI Control System:</strong> Displays real-time traffic stats and allows manual overrides.</p>

    <h2>Future Enhancements</h2>
    <ul>
        <li><strong>IoT Integration</strong> for smart traffic signal control.</li>
        <li><strong>Reinforcement Learning</strong> for advanced traffic optimization.</li>
        <li><strong>Emergency Vehicle & Pedestrian Detection</strong> for priority management.</li>
    </ul>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Follow these steps:</p>
    <ol>
        <li><strong>Fork</strong> the repository.</li>
        <li>Create a <strong>feature branch</strong> using: <code>git checkout -b feature-name</code></li>
        <li><strong>Commit changes:</strong> <code>git commit -m "Added feature"</code></li>
        <li><strong>Push</strong> to GitHub and create a <strong>pull request</strong>.</li>
    </ol>

    <h2>License</h2>
    <p>This project is licensed under the <strong>MIT License</strong>.</p>

    <hr>
    <p><strong>📌 Repository:</strong> <a href="https://github.com/Byte-Blender/SmartTrafficManagement">SmartTrafficManagement on GitHub</a></p>

</body>
</html>
