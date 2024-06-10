import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
import pandas as pd

level = "純三階"
audio_path = f"wav_file\{level}.wav"
freq_ranges = [(595,605)]

y, sr = librosa.load(audio_path, sr=None)

Y = fft(y)
freqs = np.fft.fftfreq(len(Y), 1/sr)
amplitudes = np.abs(Y)

data = {
    "Frequency (Hz)": freqs[:len(freqs)//2],
    "Absolute Amplitude (a.u.)": amplitudes[:len(amplitudes)//2]
}
data = pd.DataFrame(data)

data = data[data["Frequency (Hz)"] < 1000]

top5 = data.nlargest(30, 'Absolute Amplitude (a.u.)')

filtered_top5 = []
for freq in top5["Frequency (Hz)"]:
    if not any(np.abs(np.array(filtered_top5) - freq) < 5):
        filtered_top5.append(freq)

plt.plot(data["Frequency (Hz)"], data["Absolute Amplitude (a.u.)"], label='Frequency Spectrum')
for freq in filtered_top5:
    amplitude = data[data["Frequency (Hz)"] == freq]["Absolute Amplitude (a.u.)"].values[0]
    plt.scatter(freq, amplitude, color='red')
    plt.text(freq, amplitude, f'{freq:.1f} Hz', fontsize=9, ha='center')

plt.title("Frequency Spectrum with Top 5 Peaks")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Absolute Amplitude (a.u.)")
plt.legend()
plt.show()

filtered_Y = np.zeros_like(Y)

for low_freq, high_freq in freq_ranges:
    indices = np.where((freqs >= low_freq) & (freqs <= high_freq))[0]
    filtered_Y[indices] = Y[indices]

filtered_audio = ifft(filtered_Y)

plt.figure(figsize=(14, 5))
plt.plot(y, label='Original Audio')
plt.plot(filtered_audio.real, label='Filtered Audio')
plt.legend()
plt.show()

sf.write(f'wav_file\level-{level}.wav', filtered_audio.real, sr)