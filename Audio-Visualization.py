import pyaudio
import numpy as np
import matplotlib.pyplot as plt
import struct
import time
from tkinter import TclError

# Constants
CHUNK = 1024 * 2             # Samples per frame
FORMAT = pyaudio.paInt16     # 16-bit signed integers
CHANNELS = 1                 # Mono audio
RATE = 44100                 # Sampling rate in Hz

# Create matplotlib figure and axis
fig, ax = plt.subplots(1, figsize=(15, 7))

# Create a PyAudio instance
p = pyaudio.PyAudio()

# List available input devices
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')
for i in range(0, numdevices):
    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
        print("Input Device id", i, "-", p.get_device_info_by_host_api_device_index(0, i).get('name'))

# Ask user to select input device
audio_input = input("\n\nSelect input by Device id: ")

# Open the audio stream
stream = p.open(
    input_device_index=int(audio_input),
    format=FORMAT,
    channels=CHANNELS,
    rate=RATE,
    input=True,
    output=True,
    frames_per_buffer=CHUNK
)

# X-axis for plotting (sample indices)
x = np.arange(0, 2 * CHUNK, 2)
line, = ax.plot(x, np.random.rand(CHUNK), '-', lw=2)

# Configure the plot
ax.set_title('AUDIO WAVEFORM')
ax.set_xlabel('Samples')
ax.set_ylabel('Volume')
ax.set_ylim(0, 255)
ax.set_xlim(0, 2 * CHUNK)
plt.setp(ax, xticks=[0, CHUNK, 2 * CHUNK], yticks=[0, 128, 255])
plt.show(block=False)

print('stream started')

# Frame rate measurement
frame_count = 0
start_time = time.time()

# Main loop
while True:
    try:
        # Read raw audio data from stream
        data = stream.read(CHUNK)

        # Unpack to 16-bit signed integers
        data_int = struct.unpack(str(CHUNK) + 'h', data)

        # Convert to int32 to avoid overflow, then normalize to 0–255
        data_np = np.array(data_int, dtype=np.int32)
        data_np = ((data_np + 32768) / 256).astype(np.uint8)

        # Update plot
        line.set_ydata(data_np)
        fig.canvas.draw()
        fig.canvas.flush_events()
        frame_count += 1

    except TclError:
        frame_rate = frame_count / (time.time() - start_time)
        print('\nstream stopped')
        print('average frame rate = {:.0f} FPS'.format(frame_rate))
        break

# Clean up
stream.stop_stream()
stream.close()
p.terminate()
