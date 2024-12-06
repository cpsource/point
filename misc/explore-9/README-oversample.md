Yes, that's correct! According to the **Nyquist-Shannon Sampling Theorem** in information theory, to accurately represent a wave, you need to sample it at least **twice the highest frequency present in the signal**. Here's why and how it works:

---

### **1. The Nyquist-Shannon Sampling Theorem**
The theorem states:
- A signal with a maximum frequency of \(f_{\text{max}}\) can be perfectly reconstructed if it is sampled at a rate \(f_s\) (sampling frequency) that is at least twice \(f_{\text{max}}\):
  \[
  f_s \geq 2 f_{\text{max}}
  \]
- \(f_s\): Sampling frequency (number of samples per second).
- \(f_{\text{max}}\): Maximum frequency of the signal, also known as the **Nyquist frequency**.

---

### **2. Why 2x Sampling is Necessary**
To understand this, consider the following:

#### **2.1. Representing a Wave**
- A sine wave has two critical pieces of information in each cycle:
  - Its **peak** (positive or negative).
  - Its **zero-crossing** or phase shift.

If you sample a wave less than twice per cycle, you won’t capture these features accurately, leading to **aliasing**.

#### **2.2. Aliasing**
- If the sampling rate is too low (\(f_s < 2f_{\text{max}}\)), different signals (or frequencies) can become indistinguishable after sampling. This phenomenon is called **aliasing**, where higher frequencies "fold" back and appear as lower frequencies.

---

### **3. Example: Sampling a Wave**
Suppose you have a signal with a maximum frequency of \(f_{\text{max}} = 1 \, \mathrm{Hz}\):
- To sample it accurately, you need at least \(f_s = 2 \, \mathrm{Hz}\).
- If you sample at \(f_s < 2 \, \mathrm{Hz}\), the wave might appear distorted, as its peaks and valleys won’t align correctly with the sampling points.

---

### **4. Practical Considerations**
#### **Oversampling**
- In real-world applications, signals are often sampled at rates higher than \(2f_{\text{max}}\) to allow for imperfections in filters or reconstruction methods (e.g., CDs sample at \(44.1 \, \mathrm{kHz}\) to cover human hearing up to \(20 \, \mathrm{kHz}\)).

#### **Discrete Representation**
- Once sampled, the signal is stored as a series of discrete values. Proper sampling ensures that these values can reconstruct the original signal exactly, assuming ideal conditions.

---

### Summary
To represent a wave accurately, you must sample it at least **twice the highest frequency** present in the signal. This ensures no loss of information and prevents aliasing, enabling perfect reconstruction of the original wave.

