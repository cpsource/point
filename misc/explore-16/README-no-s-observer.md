Yes! You can perform **relative velocity calculations** between moving observers without explicitly involving the stationary observer \( S \) as a reference frame. Special relativity allows us to combine velocities **directly between two moving frames** using the **relativistic velocity addition formula**.

---

## **Relativistic Velocity Addition (No \( S \))**

The **relativistic velocity addition formula** for two frames \( A \) and \( B \) is:
\[
v_{\text{rel}} = \frac{v_A + v_B}{1 + \frac{v_A v_B}{c^2}},
\]
where:
- \( v_A \): Velocity of frame \( A \) relative to \( B \)'s frame.
- \( v_B \): Velocity of \( B \)'s frame relative to a third observer (can be implicit).
- \( c \): Speed of light.

This formula works without requiring a stationary observer \( S \) as a baseline. Velocities are combined **sequentially** and directly between frames.

---

## **Generalizing for \( n \)-Layers of Motion**

If you have:
1. Elephant \( E_1 \) running at \( v_1 \) relative to the next elephant \( E_2 \),
2. Elephant \( E_2 \) running at \( v_2 \) relative to \( E_3 \),
3. \( \dots \)
4. Elephant \( E_n \) running at \( v_n \) relative to \( E_{n-1} \),

The **relative velocity between two elephants** \( E_k \) (at layer \( k \)) and \( E_{k+1} \) (at layer \( k+1 \)) can be combined sequentially.

Let’s generalize the process for combining velocities recursively:

---

### **Recursive Formula for Nested Velocities**
If \( v_1 \) is the velocity of \( E_1 \) relative to \( E_2 \), and \( v_2 \) is the velocity of \( E_2 \) relative to \( E_3 \), then:

1. Combine \( v_1 \) and \( v_2 \):
   \[
   v_{\text{combined}, 2} = \frac{v_1 + v_2}{1 + \frac{v_1 v_2}{c^2}}.
   \]

2. Use \( v_{\text{combined}, 2} \) to combine with \( v_3 \):
   \[
   v_{\text{combined}, 3} = \frac{v_{\text{combined}, 2} + v_3}{1 + \frac{v_{\text{combined}, 2} v_3}{c^2}}.
   \]

3. Repeat this process for \( n \)-layers of velocities:
   \[
   v_{\text{combined}, n} = \frac{v_{\text{combined}, n-1} + v_n}{1 + \frac{v_{\text{combined}, n-1} v_n}{c^2}}.
   \]

This gives the relative velocity **directly** without needing \( S \).

---

## **Relative Velocity Between Two Observers**

Suppose we have two observers:
- \( k \) riding with Elephant \( E_n \),
- \( k_1 \) riding with Elephant \( E_{n_1} \).

### Steps to Find \( v_{\text{rel}} \):
1. Start with the velocity \( v_k \) for \( E_n \) and \( v_{k_1} \) for \( E_{n_1} \), each relative to the previous observer (or elephant).
2. Use the relativistic subtraction formula to find their relative velocity:
   \[
   v_{\text{rel}} = \frac{v_k - v_{k_1}}{1 - \frac{v_k v_{k_1}}{c^2}}.
   \]

This accounts for:
- **The direction of motion** (e.g., velocities \( v_k \) and \( v_{k_1} \) may have opposite signs).
- **Relativistic effects** (preventing \( v_{\text{rel}} \) from exceeding \( c \)).

---

## **Example Without \( S \): Two Moving Elephants**

### Given:
- Elephant \( E_1 \) moves at \( v_1 = 0.6c \) relative to Elephant \( E_2 \),
- Elephant \( E_2 \) moves at \( v_2 = 0.5c \) relative to Elephant \( E_3 \).

We calculate the velocity of \( E_1 \) relative to \( E_3 \):

1. Combine \( v_1 \) and \( v_2 \) (sequentially):
\[
v_{\text{combined}} = \frac{v_1 + v_2}{1 + \frac{v_1 v_2}{c^2}}.
\]
Substitute \( v_1 = 0.6c \) and \( v_2 = 0.5c \):
\[
v_{\text{combined}} = \frac{0.6c + 0.5c}{1 + \frac{(0.6c)(0.5c)}{c^2}}.
\]
Simplify:
\[
v_{\text{combined}} = \frac{1.1c}{1 + 0.3} = \frac{1.1c}{1.3} \approx 0.846c.
\]

Thus, the **velocity of \( E_1 \) relative to \( E_3 \)** is approximately \( 0.846c \).

---

## **Summary**

- You can **remove \( S \)** and compute velocities directly between moving observers using the relativistic velocity addition formula.
- Combine velocities **recursively**:
   \[
   v_{\text{combined}, n} = \frac{v_{\text{combined}, n-1} + v_n}{1 + \frac{v_{\text{combined}, n-1} v_n}{c^2}}.
   \]
- Use **relativistic subtraction** to calculate the velocity between any two observers \( k \) and \( k_1 \):
   \[
   v_{\text{rel}} = \frac{v_k - v_{k_1}}{1 - \frac{v_k v_{k_1}}{c^2}}.
   \]

This approach keeps everything **relative** between the moving frames and avoids depending on an absolute stationary observer \( S \). Let me know if you'd like me to write a Python script for these calculations! 🚀

