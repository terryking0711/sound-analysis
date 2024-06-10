import numpy as np
import librosa
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
import pandas as pd

# 音訊檔案路徑
audio_path = r"C:\Users\terry\OneDrive\桌面\財報爬蟲\physcis_research\wav_file\example.wav"

# 定義要移除的多個頻率範圍
freq_ranges_to_remove = [(0, 25000)]

# 載入音訊檔案
y, sr = librosa.load(audio_path, sr=None)

# 執行 FFT
Y = fft(y)
freqs = np.fft.fftfreq(len(Y), 1/sr)
amplitudes = np.abs(Y)

# 建立 DataFrame 存儲頻率和振幅數據
data = {
    "Frequency (Hz)": freqs[:len(freqs)//2],
    "Absolute Amplitude (a.u.)": amplitudes[:len(amplitudes)//2]
}
data = pd.DataFrame(data)

# 過濾頻率低於 1000 Hz 的數據
data = data[data["Frequency (Hz)"] < 1000]

# 找到前30個相對強度最高者的頻率
top30 = data.nlargest(30, 'Absolute Amplitude (a.u.)')

# 篩選出相差小於5的頻率，只保留一個
filtered_top30 = []
for freq in top30["Frequency (Hz)"]:
    if not any(np.abs(np.array(filtered_top30) - freq) < 5):
        filtered_top30.append(freq)

# 繪製頻譜圖並標出前30個相對強度最高的頻率
plt.plot(data["Frequency (Hz)"], data["Absolute Amplitude (a.u.)"], label='Frequency Spectrum')
for freq in filtered_top30:
    amplitude = data[data["Frequency (Hz)"] == freq]["Absolute Amplitude (a.u.)"].values[0]
    plt.scatter(freq, amplitude, color='red')
    plt.text(freq, amplitude, f'{freq:.1f} Hz', fontsize=9, ha='center')

plt.title("Frequency Spectrum with Top 30 Peaks")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Absolute Amplitude (a.u.)")
plt.legend()
plt.show()

# 初始化過濾後的頻譜
filtered_Y = Y.copy()

# 移除多個頻率範圍
for low_freq, high_freq in freq_ranges_to_remove:
    # 找到範圍內的頻率索引
    indices = np.where((freqs >= low_freq) & (freqs <= high_freq))[0]
    # 移除頻譜中的這些頻率
    filtered_Y[indices] = 0

# 執行 IFFT 得到過濾後的音訊
filtered_audio = ifft(filtered_Y)

# 繪製原始音訊和過濾後音訊的波形圖
plt.figure(figsize=(14, 5))
plt.plot(y, label='Original Audio')
plt.plot(filtered_audio.real, label='Filtered Audio')
plt.legend()
plt.show()

# 將過濾後的音訊寫入新的 wav 檔案
sf.write('physcis_research\wav_file\converted.wav', filtered_audio.real, sr)
