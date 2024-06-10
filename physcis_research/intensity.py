import numpy as np
import matplotlib.pyplot as plt
import wave

# File paths
file_paths = [
    r"wav_file\level-純三階.wav",
    r"wav_file\level-1.wav",
    r"wav_file\level-2.wav",
    r"wav_file\level-3.wav",
    r"wav_file\level-4.wav",
    r"wav_file\level-沒風扇.wav",
]

# Function to calculate the intensity of a wav file
def calculate_intensity(file_path):
    with wave.open(file_path, 'r') as wav_file:
        frames = wav_file.readframes(-1)
        amplitude = np.frombuffer(frames, dtype=np.int16)
        intensity = np.sum(np.square(amplitude)) / len(amplitude)
    return intensity

# Calculate intensities for all files
intensities = [calculate_intensity(file_path) for file_path in file_paths]

# Plotting the intensities
plt.figure(figsize=(10, 6))
plt.bar(range(len(intensities)), intensities, color='skyblue')
plt.xlabel('Audio Files')
plt.ylabel('Intensity')
plt.title('Comparison of Audio File Intensities')
plt.xticks(range(len(intensities)), ['only-fan', 'level-1', 'level-2', 'level-3', 'level-4',"only-600Hz"])
plt.show()
