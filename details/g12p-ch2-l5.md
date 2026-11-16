# RC Circuits and Capacitors in Circuits

The blinking of a warning light, the delay in a timer and the flash of a camera all depend on a resistor and a capacitor working together. When a capacitor is connected to a battery through a resistor, it does not charge instantly. The charge builds up gradually, fast at first and then more slowly. The speed of this process is set by one number, the time constant, which is simply the product of the resistance and the capacitance.

## Key ideas

When a capacitor is charged through a resistor, the charge grows as Q = Q_max (1 - e^(-t / RC)). When it discharges through a resistor, the charge falls as Q = Q0 e^(-t / RC). The voltage across the capacitor follows the same shape, since V = Q / C. Here e is the base of natural logarithms, about 2.718. The exponential function describes any process in which the rate of change is proportional to what remains to be done, and it is common throughout physics.

The time constant is tau = R C. Its unit is the second, since ohms times farads is seconds. It tells how fast the process goes. After one time constant, a charging capacitor has reached 63 percent of its final charge, and a discharging one has fallen to 37 percent of its initial value. After 5 time constants the process is practically complete, with the capacitor at more than 99 percent of its final charge. A larger resistance or a larger capacitance makes the charging slower: a large R limits the current, and a large C needs more charge to fill.

Two special moments help in analyzing circuits. At the instant a switch is closed, an uncharged capacitor acts like a wire, because there is no voltage across it, so the current is at its maximum, equal to emf / R. After a long time, a charged capacitor acts like an open circuit, because its voltage equals the battery voltage and no current flows. The current in a charging circuit therefore decays from its maximum toward zero, also with the same time constant.

The idea explains the timing in many devices. A capacitor that charges slowly through a large resistor can switch a circuit on or off after a delay, and the flash of a camera is the quick discharge of a capacitor that was charged slowly.

## Worked examples

**Example 1: The time constant.** A resistor of 10 kilohm is connected with a capacitor of 100 microfarad. Find the time constant.
1. Convert the units: R = 10 000 ohm and C = 100 x 10^-6 F.
2. tau = R C = 10 000 x 100 x 10^-6.
3. The time constant is tau = 1.0 s.

**Example 2: Charging.** The same circuit is connected to a 12 V battery. Find the capacitor voltage after 1.0 s and after 5.0 s.
1. After one time constant, V = 12 x (1 - e^-1) = 12 x 0.632 = 7.6 V.
2. After five time constants, V = 12 x (1 - e^-5) = 12 x 0.993 = 11.9 V.
3. The capacitor is practically fully charged after 5.0 s.

**Example 3: Discharging.** A capacitor charged to 10 V discharges through the same resistor. Find the voltage after one time constant.
1. Use V = V0 e^(-t / tau) with t = tau, which gives V = V0 e^-1.
2. V = 10 x 0.368.
3. The voltage is V = 3.7 V.

## Common mistakes

Students often use microfarads as if they were farads, which makes the time constant wrong by a factor of a million. Another is to think that the capacitor charges instantly; it takes about 5 time constants to fill. A third mistake is to confuse the 63 percent of charging with the 37 percent of discharging, which are really the same curve seen from two sides: after one time constant, 63 percent has been gained or 37 percent remains. Finally, remember that a larger R makes the process slower, not faster.
