import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
    
# 設置SimHei字體
plt.rcParams['font.sans-serif'] = ['SimHei']  # 替換為你系統中的中文字體
plt.rcParams['axes.unicode_minus'] = False  # 避免負號顯示問題

# Read all the wav files
filenames = [
    'wav_file\level-1.wav',
    'wav_file\level-2.wav',
    'wav_file\level-3.wav',
    'wav_file\level-4.wav',
    'wav_file\level-沒風扇.wav',
    'wav_file\level-純三階.wav'
]

data = []

for file in filenames:
    rate, audio = wav.read(file)
    amplitude = np.mean(np.abs(audio))
    intensity = np.mean(audio ** 2)
    decibel = 20 * np.log10(amplitude)
    data.append({
        'File': file.split('/')[-1],
        'Amplitude': amplitude,
        'Intensity': intensity,
        'Decibel': decibel
    })

# Create a DataFrame
df = pd.DataFrame(data)

# Plotting
fig, axes = plt.subplots(3, 1, figsize=(10, 18))

df.plot(kind='bar', x='File', y='Amplitude', ax=axes[0], legend=False, color='skyblue')
axes[0].set_ylabel('Amplitude')
axes[0].set_title('Amplitude of WAV Files')

df.plot(kind='bar', x='File', y='Intensity', ax=axes[1], legend=False, color='lightgreen')
axes[1].set_ylabel('Intensity')
axes[1].set_title('Intensity of WAV Files')

df.plot(kind='bar', x='File', y='Decibel', ax=axes[2], legend=False, color='lightcoral')
axes[2].set_ylabel('Decibel (dB)')
axes[2].set_title('Decibel of WAV Files')

plt.tight_layout()
plt.show()
