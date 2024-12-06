When \(v > c\), the Lorentz factor \(\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}\) becomes **complex** because the term \(1 - v^2/c^2\) is negative, resulting in a square root of a negative number.

Let’s work this out step by step and examine what happens to energy under these conditions.

---

### **Lorentz Factor:**
The Lorentz factor is defined as:

\[
\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}
\]

When \(v > c\):
\[
1 - \frac{v^2}{c^2} < 0
\]

Let \(v = \kappa c\), where \(\kappa > 1\). Substituting this into the Lorentz factor:

\[
\gamma = \frac{1}{\sqrt{1 - \kappa^2}}
\]

Since \(1 - \kappa^2 < 0\), let:
\[
1 - \kappa^2 = -(\kappa^2 - 1)
\]

So:
\[
\gamma = \frac{1}{\sqrt{- (\kappa^2 - 1)}} = \frac{i}{\sqrt{\kappa^2 - 1}}
\]

Here, \(i = \sqrt{-1}\), making \(\gamma\) a complex number.

---

### **Relativistic Energy:**
The relativistic energy is given by:

\[
E = \gamma m_0 c^2
\]

Substituting the complex \(\gamma\):

\[
E = \frac{i m_0 c^2}{\sqrt{\kappa^2 - 1}}
\]

So, the energy becomes **complex**:
\[
E = i \frac{m_0 c^2}{\sqrt{\kappa^2 - 1}}
\]

---

### **Implications:**
1. **Imaginary Energy**:
   - If \(v > c\), the energy \(E\) becomes imaginary (\(i \cdot\) real value), suggesting that such speeds are not physically meaningful for particles with rest mass (\(m_0 > 0\)).

2. **Interpretation**:
   - A complex energy implies that the classical concepts of energy and momentum break down. This supports the fact that no object with rest mass can travel faster than \(c\).

---

### **Example Calculation**:
Assume:
- \(v = 2c\) (\(\kappa = 2\)),
- \(m_0 = 1 \, \mathrm{kg}\),
- \(c = 3 \times 10^8 \, \mathrm{m/s}\).

1. Calculate \(\gamma\):
\[
\gamma = \frac{i}{\sqrt{\kappa^2 - 1}} = \frac{i}{\sqrt{4 - 1}} = \frac{i}{\sqrt{3}}
\]

2. Calculate \(E\):
\[
E = \gamma m_0 c^2 = \frac{i m_0 c^2}{\sqrt{3}}
\]

Substitute values:
\[
E = \frac{i (1) (3 \times 10^8)^2}{\sqrt{3}}
\]
\[
E = \frac{i (9 \times 10^{16})}{\sqrt{3}} \approx i \cdot 5.20 \times 10^{16} \, \mathrm{J}
\]

---

### **Conclusion**:
If \(v > c\), the Lorentz factor and energy become complex, which is a mathematical indication that such speeds are **not physically possible** for objects with mass. This aligns with the principles of relativity.

