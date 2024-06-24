
Electromyography (EMG) is a critical tool in understanding muscle activity through the electrical signals generated during muscle contractions. Analyzing specific frequency bands within EMG signals provides insights into muscle fatigue, movement disorders, and neuromuscular diseases. This article outlines a method for isolating frequency bands from EMG data and calculating the power within these bands using digital signal processing techniques.


Electromyography (EMG) measures electrical activity produced by skeletal muscles. Analyzing the frequency content of EMG signals aids in diagnosing and understanding various muscular and neurological conditions. Frequency band analysis is particularly useful in identifying muscle fatigue and evaluating neuromuscular function. This paper presents a detailed methodology for isolating different frequency bands from EMG signals and calculating the power of each band, providing a quantitative measure of the activity within those bands.


Preprocessing EMG data involves several steps to prepare the raw signals for analysis:

Bandpass Filtering: Remove noise and unwanted frequencies. A bandpass filter with cutoffs typically between 20 Hz and 450 Hz is applied to isolate the frequency range relevant to muscle activity.

Rectification: Convert the signal to its absolute value to facilitate the subsequent analysis steps.

Normalization: Scale the data to a consistent range if needed, which is especially important for comparing signals from different sources or individuals.


Frequency band isolation involves defining specific bands of interest within the EMG signal’s frequency spectrum. Commonly studied bands include:

Delta (0.5–4 Hz)
Theta (4–8 Hz)
Alpha (8–13 Hz)
Beta (13–30 Hz)
Gamma (30–100 Hz)
Each band correlates with different physiological and pathological states of the muscles and central nervous system.

To analyze the frequency content, the Power Spectral Density (PSD) of the signal is computed using the Fast Fourier Transform (FFT) or Welch’s method. Welch’s method is preferred due to its robustness against noise and its ability to provide an average estimate of the PSD over time.


Bandpower is calculated by integrating the PSD over the frequency range of each band. The Welch method is used to estimate the PSD, and the power within each band is computed using numerical integration.

Code used can be found as eeg.py in this repository


The bandpower function integrates the PSD over specified frequency bands, giving a quantitative measure of power within each band. This method allows for an objective comparison of muscle activity across different frequency ranges, aiding in the diagnosis and monitoring of muscular and neurological conditions.


Applying the methodology to typical EMG data reveals distinct power contributions across different frequency bands. For instance, higher bandpower in the Gamma range (30–100 Hz) might indicate increased muscle activity or potential neuromuscular disorders, whereas higher power in the Beta range (13–30 Hz) can relate to motor control processes.

The bandpower calculation provides a powerful tool for analyzing the frequency components of EMG signals. It aids in identifying patterns related to muscle fatigue, motor control, and neurological conditions. By isolating and quantifying power in specific frequency bands, clinicians and researchers can better understand the underlying mechanisms of muscle activity and dysfunction.



