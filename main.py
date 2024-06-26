import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
import seaborn as sns
from scipy.integrate import simps
sns.set(font_scale=1.2)


# extract EEG from file
data_file = r"C:\Users\Admin\PycharmProjects\PostmanNeuroT1\eeg-data.txt"
sfreq = 100
win = 4
# load EEG
eeg_data = np.loadtxt(data_file)
time = np.arange(eeg_data.size) / sfreq

# get psd using welch
frequencies, psd = welch(eeg_data, fs=sfreq, nperseg=sfreq*win)
freqres = frequencies[1] - frequencies[0]

freq_bands = {
    'Delta': (1, 4),
    'Theta': (4, 8),
    'Alpha': (8, 13),
    'Beta': (13, 30)
}

# get absolute bandpower
bandpower = {}
for band, (f_low, f_high) in freq_bands.items():
    idx_band = np.where((frequencies >= f_low) & (frequencies <= f_high))
    band_power = simps(psd[idx_band], dx=freqres)
    bandpower[band] = band_power

# get total power & relative bandpower
total_power = simps(psd, frequencies)
relative_bandpower = {band: power / total_power for band, power in bandpower.items()}
max_band = max(relative_bandpower, key=relative_bandpower.get)

print("Absolute Bandpower:")
for band, power in bandpower.items():
    print(f"{band}: {power:.4f} µV^2")

print("\nRelative Bandpower:")
for band, power in relative_bandpower.items():
    print(f"{band}: {power:.4f}")
print(f"\nThe frequency band with the highest relative bandpower is: {max_band.capitalize()}")
# Plot psd
plt.figure(figsize=(8, 4))
plt.plot(frequencies, psd, color='k', lw=2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Power Spectral Density (µV^2/Hz)')
plt.title('Power Spectral Density')
plt.grid(True)
plt.show()
