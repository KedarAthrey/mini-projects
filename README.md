Electroencephalography (EEG) measures electrical activity in the brain using electrodes placed on the scalp. EEG signals provide insights into brain function and are used in various applications, including clinical diagnosis, neuroscience research, and brain-computer interfacing. A critical aspect of EEG analysis is the extraction of different bandpowers from EEG data and the computation of spectral density. This article explores the methodologies for extracting bandpowers from EEG data and computing spectral density, highlighting their importance and applications.

<h1>Types of Bands</h1>
EEG signals are typically decomposed into different frequency bands, each associated with distinct neural processes:<br>
<br>

Delta (0.5-4 Hz): Dominant during deep sleep and in pathological conditions such as brain injuries.<br>
Theta (4-8 Hz): Related to drowsiness, light sleep, and certain cognitive tasks such as memory encoding.<br>
Alpha (8-13 Hz): Associated with relaxed wakefulness and is most prominent in the posterior regions of the brain when the eyes are closed.<br>
Beta (13-30 Hz): Linked to active thinking, concentration, and motor activity.<br>
Gamma (30-100 Hz): Associated with high-level cognitive functions, including perception and consciousness.<br>

<h1>Methods for Bandpower Extraction</h1>
<h2>1. Fourier Transform</h2>
The Fourier Transform (FT) is a mathematical technique that converts a time-domain signal into its constituent frequencies. In EEG analysis, the Discrete Fourier Transform (DFT) or its efficient computation, the Fast Fourier Transform (FFT), is commonly used to obtain the power spectral density (PSD) of the signal.

<h3>a.Preprocessing</h3> EEG data is often preprocessed to remove artifacts such as eye blinks and muscle movements. Common preprocessing steps include filtering, segmentation, and artifact rejection.<br>
<h3>b.Windowing</h3>: EEG data is typically divided into overlapping segments or windows to enhance the frequency resolution and reduce spectral leakage.<br>
<h3>c.FFT Computation</h3> The FFT is applied to each windowed segment to compute the PSD. The PSD is then averaged over all segments to obtain the overall PSD.<br>
The power in each frequency band is calculated by integrating the PSD within the band’s frequency range.

<h2>2. Wavelet Transform</h2>
The Wavelet Transform (WT) provides a time-frequency representation of the signal, making it suitable for analyzing non-stationary signals like EEG. Unlike the FT, the WT can capture both frequency and temporal information.

<h3>a.Selection of Wavelet</h3> The choice of wavelet function affects the analysis. Commonly used wavelets in EEG analysis include the Morlet and Daubechies wavelets.<br>
<h3>b.Decomposition</h3> The EEG signal is decomposed into different scales, each corresponding to a specific frequency band.
Energy Computation: The power in each frequency band is obtained by calculating the energy of the wavelet coefficients within that band.<br>
<h2>3. Hilbert-Huang Transform</h2>
The Hilbert-Huang Transform (HHT) is a non-linear and non-stationary signal processing technique that combines Empirical Mode Decomposition (EMD) and Hilbert Spectral Analysis (HSA).<br>

<h3>a.EMD Decomposition</h3> The EEG signal is decomposed into a set of Intrinsic Mode Functions (IMFs) using EMD. Each IMF represents a specific oscillatory mode.<br>
<h3>b.Hilbert Transform</h3>The Hilbert Transform is applied to each IMF to obtain the instantaneous frequency and amplitude.<br>
<h3>c.Power Computation:</h3> The power in each frequency band is computed using the Hilbert spectrum, which represents the energy distribution in the time-frequency plane.<br>

<h2>Computation of Power Spectral Density</h2>
PSD = F{x(t)}<sup>2</sup>/T <br>
where F is the Fourier Transform of signal x(t) and T is the total duration<br>
__Welch’s Method:__ A common method for estimating the PSD is Welch’s method, which involves dividing the signal into overlapping segments, applying a window function to each segment, computing the periodogram, and averaging the periodograms.
<h2>Applications</h2>
Clinical Diagnosis: Bandpower analysis is used to detect abnormalities such as epilepsy, sleep disorders, and brain injuries.
Cognitive Research: Analysis of EEG bandpowers provides insights into cognitive processes such as attention, memory, and learning.
Brain-Computer Interfaces (BCIs): Bandpower features are employed in BCIs for controlling external devices through neural signals.
<h2>Code</h2>
can be found [here] (https://github.com/KedarAthrey/mini-projects/blob/eegdata/main.py).
<h2>Sources</h2>
Niedermeyer, E., & da Silva, F. L. (2004). Electroencephalography: Basic Principles, Clinical Applications, and Related Fields. Lippincott Williams & Wilkins.<br>
Oken, B. S., & Chiappa, K. H. (1986). Short-term variability in EEG frequency analysis. Electroencephalography and Clinical Neurophysiology, 63(4), 353-367.<br>
Cooley, J. W., & Tukey, J. W. (1965). An algorithm for the machine calculation of complex Fourier series. Mathematics of Computation, 19(90), 297-301.<br>
Daubechies, I. (1990). The wavelet transform, time-frequency localization and signal analysis. IEEE Transactions on Information Theory, 36(5), 961-1005.<br>
Huang, N. E., Shen, Z., & Long, S. R. (1998). The empirical mode decomposition and the Hilbert spectrum for nonlinear and non-stationary time series analysis. Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences, 454(1971), 903-995.<br>
