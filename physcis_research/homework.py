import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

data0 = pd.read_excel(r"fan\level-1-n.xls")
data1 = pd.read_excel(r"fan\level-2-n.xls")
data2 = pd.read_excel(r"fan\level-3-n.xls")
data3 = pd.read_excel(r"fan\level-4-n.xls")
data4 = pd.read_excel(r"fan\600Hz.xls")
data5 = pd.read_excel(r"fan\純三階.xls")

data0 = data0[data0["Frequency (Hz)"] < 800]
data1 = data1[data1["Frequency (Hz)"] < 800]
data2 = data2[data2["Frequency (Hz)"] < 800]
data3 = data3[data3["Frequency (Hz)"] < 800]
data4 = data4[data4["Frequency (Hz)"] < 800]
data5 = data5[data5["Frequency (Hz)"] < 800]

scaler = MinMaxScaler(feature_range=(0, 1))
data0["Absolute Amplitude (a.u.)"] = scaler.fit_transform(data0[["Absolute Amplitude (a.u.)"]])
data1["Absolute Amplitude (a.u.)"] = scaler.fit_transform(data1[["Absolute Amplitude (a.u.)"]])
data2["Absolute Amplitude (a.u.)"] = scaler.fit_transform(data2[["Absolute Amplitude (a.u.)"]])
data3["Absolute Amplitude (a.u.)"] = scaler.fit_transform(data3[["Absolute Amplitude (a.u.)"]])
data4["Absolute Amplitude (a.u.)"] = scaler.fit_transform(data4[["Absolute Amplitude (a.u.)"]])
data5["Absolute Amplitude (a.u.)"] = scaler.fit_transform(data5[["Absolute Amplitude (a.u.)"]])

closest_data0 = data0.iloc[(data0["Frequency (Hz)"] - 600).abs().argsort()[:1]]
closest_data1 = data1.iloc[(data1["Frequency (Hz)"] - 600).abs().argsort()[:1]]
closest_data2 = data2.iloc[(data2["Frequency (Hz)"] - 600).abs().argsort()[:1]]
closest_data3 = data3.iloc[(data3["Frequency (Hz)"] - 600).abs().argsort()[:1]]
closest_data4 = data4.iloc[(data4["Frequency (Hz)"] - 600).abs().argsort()[:1]]
closest_data5 = data5.iloc[(data5["Frequency (Hz)"] - 600).abs().argsort()[:1]]

plt.figure(figsize=(10, 6))
plt.plot(data0["Frequency (Hz)"], data0["Absolute Amplitude (a.u.)"], label='level 1 fan')
plt.plot(data1["Frequency (Hz)"], data1["Absolute Amplitude (a.u.)"], label='level 2 fan')
plt.plot(data2["Frequency (Hz)"], data2["Absolute Amplitude (a.u.)"], label='level 3 fan')
plt.plot(data3["Frequency (Hz)"], data3["Absolute Amplitude (a.u.)"], label='level 4 fan')
plt.plot(data4["Frequency (Hz)"], data4["Absolute Amplitude (a.u.)"], label='level 600 fan')
plt.plot(data5["Frequency (Hz)"], data5["Absolute Amplitude (a.u.)"], label='level only fan')

plt.scatter(closest_data0["Frequency (Hz)"], closest_data0["Absolute Amplitude (a.u.)"], color='red', zorder=5)
plt.scatter(closest_data1["Frequency (Hz)"], closest_data1["Absolute Amplitude (a.u.)"], color='red', zorder=5)
plt.scatter(closest_data2["Frequency (Hz)"], closest_data2["Absolute Amplitude (a.u.)"], color='red', zorder=5)
plt.scatter(closest_data3["Frequency (Hz)"], closest_data3["Absolute Amplitude (a.u.)"], color='red', zorder=5)
plt.scatter(closest_data4["Frequency (Hz)"], closest_data4["Absolute Amplitude (a.u.)"], color='red', zorder=5)
plt.scatter(closest_data5["Frequency (Hz)"], closest_data5["Absolute Amplitude (a.u.)"], color='red', zorder=5)

for i, row in closest_data0.iterrows():
    plt.annotate(f'({row["Frequency (Hz)"]:.2f}, {row["Absolute Amplitude (a.u.)"]:.2f})', 
                 (row["Frequency (Hz)"], row["Absolute Amplitude (a.u.)"]), 
                 textcoords="offset points", xytext=(0,10), ha='center')
for i, row in closest_data1.iterrows():
    plt.annotate(f'({row["Frequency (Hz)"]:.2f}, {row["Absolute Amplitude (a.u.)"]:.2f})', 
                 (row["Frequency (Hz)"], row["Absolute Amplitude (a.u.)"]), 
                 textcoords="offset points", xytext=(0,10), ha='center')
for i, row in closest_data2.iterrows():
    plt.annotate(f'({row["Frequency (Hz)"]:.2f}, {row["Absolute Amplitude (a.u.)"]:.2f})', 
                 (row["Frequency (Hz)"], row["Absolute Amplitude (a.u.)"]), 
                 textcoords="offset points", xytext=(0,10), ha='center')
for i, row in closest_data3.iterrows():
    plt.annotate(f'({row["Frequency (Hz)"]:.2f}, {row["Absolute Amplitude (a.u.)"]:.2f})', 
                 (row["Frequency (Hz)"], row["Absolute Amplitude (a.u.)"]), 
                 textcoords="offset points", xytext=(0,10), ha='center')
for i, row in closest_data4.iterrows():
    plt.annotate(f'({row["Frequency (Hz)"]:.2f}, {row["Absolute Amplitude (a.u.)"]:.2f})', 
                 (row["Frequency (Hz)"], row["Absolute Amplitude (a.u.)"]), 
                 textcoords="offset points", xytext=(0,10), ha='center')
for i, row in closest_data5.iterrows():
    plt.annotate(f'({row["Frequency (Hz)"]:.2f}, {row["Absolute Amplitude (a.u.)"]:.2f})', 
                 (row["Frequency (Hz)"], row["Absolute Amplitude (a.u.)"]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.title("Scaled FFT Spectrum Data")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Absolute Amplitude (a.u.)")
plt.legend()
plt.show()
