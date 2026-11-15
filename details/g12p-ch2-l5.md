# RC Circuits and Capacitors in Circuits

The blinking light on a signal and the delay in a timer are set by the time constant R times C.

## Key ideas
- **Charging**: **Q = Q_max (1 - e^(-t / RC))**; **discharging**: **Q = Q0 e^(-t / RC)**.
- **Time constant tau = R C**.
- After **1 tau**: 63% charged (or 37% left).
- After **5 tau**: practically complete.
- A new capacitor acts like a **wire**; a charged one like an **open circuit**.
- Larger **R** or **C** means slower charging.

## Worked examples
**Example 1: Time constant.** R = 10 kilohm and C = 100 microfarad.
1. tau = R C = 10,000 x 100 x 10^-6.
2. tau = 1.0 s.

**Example 2: Charging.** How long to charge to about 63%?
1. That takes one time constant.
2. t = 1.0 s.

**Example 3: Discharge.** A capacitor at 10 V discharges. What is the voltage after one time constant?
1. V = V0 e^-1 = 10 x 0.368.
2. V = 3.7 V.

## Common mistakes
- Using microfarads as farads.
- Thinking the capacitor charges instantly.
- Confusing 63% (charging) with 37% (discharging).
