# Inductance, Transformers and AC

Power stations send electricity at very high voltage to reduce losses along the cables, and transformers lower the voltage again before it reaches our homes. Both ideas rest on electromagnetic induction. This lesson looks at three related topics: inductors, which resist changes in current, transformers, which change voltages, and alternating current, which is the form of electricity used in homes.

## Key ideas

When the current in a coil changes, its own magnetic field changes, and this induces an emf in the coil itself. The effect is called self-induction, and by Lenz's law the induced emf opposes the change in current. The relation is emf = -L delta I / delta t, where L is the inductance of the coil, measured in henries (H). An inductor therefore acts like inertia in a circuit: it resists any sudden change in current. It also stores energy in its magnetic field, U = 1/2 L I^2, which is similar to the energy stored in a capacitor.

A transformer has two coils wound on a common iron core, the primary with N_p turns and the secondary with N_s turns. An alternating current in the primary creates a changing flux in the core, which induces an emf in the secondary. Because the same flux passes through both coils, the voltages are in the ratio of the turns: V_s / V_p = N_s / N_p. A step-up transformer has more turns in the secondary and raises the voltage, while a step-down transformer lowers it. A transformer does not create energy. For an ideal transformer, the power in equals the power out, V_p I_p = V_s I_s, so a higher voltage means a lower current. This is why power lines use high voltage: a smaller current means smaller losses of I^2 R in the cables. A transformer works only with a changing current. A steady direct current gives no change in flux and no induced voltage.

Alternating current changes its direction regularly, following a sine curve. The peak voltage is the maximum value, but the meaningful value is the root-mean-square (rms) value, V_rms = V_peak / sqrt(2), which is about 0.707 of the peak. The rms value of an AC supply gives the same heating as a DC supply of equal value. The average power is P = I_rms V_rms. A mains supply described as 220 V is quoted as an rms value.

## Worked examples

**Example 1: A transformer.** A transformer has 200 turns in the primary and 1000 turns in the secondary. The primary voltage is 12 V. Find the secondary voltage.
1. Use V_s = V_p N_s / N_p = 12 x 1000 / 200.
2. The ratio of turns is 5.
3. The secondary voltage is V_s = 60 V.

**Example 2: Currents.** The secondary of the same ideal transformer supplies 0.50 A. Find the primary current.
1. Use V_p I_p = V_s I_s, so I_p = 60 x 0.50 / 12.
2. The primary current is I_p = 2.5 A.
3. The voltage went up by 5, and the current went down by 5, so the power is the same, 30 W.

**Example 3: The rms value.** The peak voltage of an AC supply is 311 V. Find the rms voltage.
1. Use V_rms = V_peak / sqrt(2) = 311 / 1.414.
2. The rms voltage is V_rms = 220 V.

## Common mistakes

Students often use the peak value where the rms value is needed, which makes the power wrong by a factor of two. Another mistake is thinking that a transformer increases power; a step-up transformer raises the voltage but lowers the current. A third is to try to use a transformer with direct current, which does not work. Finally, remember that the turns ratio gives the voltage ratio, and the current ratio is its inverse.
