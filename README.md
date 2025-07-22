
<img width="824" height="612" alt="image" src="https://github.com/user-attachments/assets/f957f248-b0c1-41a4-b024-403383e7e8c8" />




# 🎧 Real-Time Audio Waveform Visualizer

Experience your voice come to life — this real-time audio waveform visualizer captures live microphone input and beautifully animates it using Python. It's perfect for audio projects, educational demos, or simply exploring the science of sound!


---

## 🚀 Project Overview

This project uses **PyAudio**, **NumPy**, and **Pygame** to capture real-time microphone input and visualize the audio waveform as it flows. The waveform dynamically reacts to any sound, creating a simple and effective audio feedback loop that you can build upon or use in your own creative applications.

---

## 🧩 Features

- 🎙️ **Real-Time Microphone Capture** – Captures live audio using your device's input source.
- 📊 **Waveform Visualization** – Converts live audio samples into a flowing waveform using `pygame`.
- 💡 **Interactive Input Selection** – Lets you choose from available input devices.
- 🖥️ **Minimal UI** – Simple, clean waveform viewer window for easy monitoring.
- 🧪 **Modular Code** – Easy to expand with more features like frequency visualization, audio recording, etc.

---

## 🔧 Requirements

Before you run the project, make sure you have **Python 3.8+** installed. You’ll also need the following Python libraries:

### 📦 Install via `requirements.txt`

```bash
pip install -r requirements.txt

Or install them manually:
pip install numpy pygame pyaudio
```


# 🛠️ How to Run the Project
1.Clone this repository
git clone https://github.com/CodeWithNirmalya/Real-Time-Audio-Waveform-Visualizer.git
cd Real-Time-Audio-Waveform-Visualizer

### 2.Run the Python script
python Audio-Visualization.py

### 3.Select the input device


## 📁 Project Structure:
### 📁 Real-Time-Audio-Waveform-Visualizer/
├── Audio-Visualization.py                    # Main Python script
├── README.md                    # Full project documentation


## 🧠 How It Works (Behind the Scenes)
▪️ PyAudio is used to stream audio input from your selected microphone.

▪️ Audio samples are captured in real-time and converted into numerical arrays using NumPy.

▪️ Pygame renders these values into a visual waveform on the screen, updating continuously to reflect new input.

▪️ Data is normalized and shifted to make it suitable for display as pixel values.



## 🎯 Use Cases
▪️ 🎧 Build a real-time visualizer for your music or podcast recording.

▪️ 📈 Demonstrate waveform properties in educational settings.

▪️ 🧪 Prototype audio-based projects like voice assistants or signal processors.

▪️ 🎨 Use it as a creative coding experiment or UI component for your audio app.


