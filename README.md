# Diophantine Approximation Suite

An open-source Python toolkit for generating simple continued fractions, computing rational convergents $p_n / q_n$, verifying Dirichlet approximation bounds, and exploring the Diophantine approximation spectrum through Hurwitz's theorem.

---

## Overview

The **Diophantine Approximation Suite** provides tools for exploring how real numbers are approximated by rationals. The suite implements finite and infinite continued fraction expansions, handles floating-point precision issues alongside exact symbolic rational arithmetic, and evaluates how close convergents get to theoretical approximation limits.

### Key Features
* **Floating-Point Drift Correction**: Employs integer snapping and relative tolerance checking (`1e-9`) to resolve precision drift in floating-point computations.
* **Exact Rational Support**: Supports Python's `fractions.Fraction` and `int` types using exact modular arithmetic (Euclidean algorithm).
* **Dirichlet Inequality Evaluation**: Verifies whether convergents satisfy $\vert{}x - p_n/q_n\vert{} < 1/q_n^2$.
* **Hurwitz Constant & Spectrum Analysis**: Calculates scaled approximation errors $q^2 \cdot \vert{}x - p_n/q_n\vert{}$ to analyze badly approximable numbers and demonstrate the unique extremality of the Golden Ratio ($\phi$).

---

## Mathematical Foundations

### 1. Continued Fractions
Any real number $x$ can be expressed as a simple continued fraction:
$$x = a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{a_3 + \ddots}}} = [a_0; a_1, a_2, a_3, \dots]$$
where $a_0 \in \mathbb{Z}$ and $a_i \in \mathbb{Z}^+$ for $i \ge 1$.

### 2. Convergent Recurrence Relations
The $n$-th rational convergent $C_n = \frac{p_n}{q_n}$ is computed using second-order linear recurrence equations:
$$p_n = a_n p_{n-1} + p_{n-2}$$
$$q_n = a_n q_{n-1} + q_{n-2}$$
with initial seed conditions:
* $p_{-1} = 1, \quad p_{-2} = 0$
* $q_{-1} = 0, \quad q_{-2} = 1$

### 3. Dirichlet's Approximation Theorem
For any irrational number $x$, there exist infinitely many rational fractions $p/q$ satisfying:
$$\left\vert{} x - \frac{p}{q} \right\vert{} < \frac{1}{q^2}$$

### 4. Hurwitz's Theorem & Badly Approximable Numbers
Hurwitz's theorem sharpens Dirichlet's bound, showing that for every irrational $x$, there exist infinitely many convergents such that:
$$\left\vert{} x - \frac{p}{q} \right\vert{} < \frac{1}{\sqrt{5} \, q^2}$$
The scaled error metric $q^2 \cdot \vert{}x - p/q\vert{}$ approaches an upper bound of $\frac{1}{\sqrt{5}} \approx 0.447214$. Numbers whose partial quotients are small and bounded (most notably $\phi = [1; 1, 1, \dots]$) reach this maximum, making them the hardest real numbers to approximate rationally.

---

## Directory Architecture

```text
Diophantine_Suite/
│
├── module1_cf_generator.py    # Generates partial quotients and continued fractions formatting
├── module2_convergents.py     # Computes p/q pairs and tests Dirichlet bounds
├── module3_spectrum.py        # Evaluates badly approximable numbers & Hurwitz limits
├── main.py                    # Master demonstration script
└── README.md                  # Project documentation
```

## Modules

### module1_cf_generator.py
Implements the continued fraction algorithm from scratch, computing partial quotients for rational, quadratic irrational, and transcendental numbers.

### module2_convergents.py
Computes rational convergents from continued fraction expansions using the fundamental recurrence relations, and checks each convergent against Dirichlet's approximation theorem.

### module3_spectrum.py
Compares how "badly approximable" different irrational numbers are by examining their partial quotients, and numerically verifies Hurwitz's theorem, showing why the golden ratio is the hardest irrational number to approximate by rationals.

## Usage

Run `main.py` to see a complete demonstration:

```bash
python main.py
```

## Requirements

No installation needed. Uses only the built-in `math` module for Python.

## Author

* **Ekene Atuchukwu** - *Initial development and algorithm implementation* - [@Ekene-Atuchukwu](https://github.com/Ekene-Atuchukwu)

This is my first Python repository! If you notice any bugs or have ideas on how to optimize the numerical logic, please open an issue or reach out.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 Ekene Atuchukwu

Copyright (c) 2026 Ekene Atuchukwu
