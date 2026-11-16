# Capacitors in Electric Fields

A camera flash stores energy slowly in a capacitor and then releases it in a fraction of a second, giving a very bright pulse. Capacitors are devices that store electric charge and energy in the electric field between two conductors. They appear in almost every electronic device, from timers and filters to touch screens and power supplies.

## Key ideas

A capacitor is two conductors, often parallel plates, separated by a small gap or an insulator. When a battery is connected, equal and opposite charges, +Q and -Q, build up on the plates, and a potential difference V appears between them. The capacitance is the ratio C = Q / V, the charge stored per volt. Its unit is the farad (F), and since a farad is very large, practical capacitors are in microfarads (10^-6 F) or picofarads (10^-12 F).

For parallel plates of area A separated by a distance d, the capacitance is C = epsilon_0 A / d. Larger plates store more charge for the same voltage, and a smaller gap gives a stronger field and therefore also a larger capacitance. Doubling the separation halves the capacitance. Placing an insulating material, called a dielectric, between the plates increases the capacitance by a factor kappa, the dielectric constant: C = kappa epsilon_0 A / d. The dielectric reduces the field inside, so more charge can be stored at the same voltage.

Energy is stored in the field of the capacitor. The energy of a charged capacitor is U = 1/2 C V^2, which can also be written as 1/2 Q V. The factor 1/2 appears because the voltage grows as the charge builds up, so the average voltage is half of the final value.

Capacitors can be combined. In parallel, they share the same voltage and the charges add, so the total is C = C1 + C2. In series, they carry the same charge and the voltages add, giving 1 / C = 1 / C1 + 1 / C2. Notice that these rules are the opposite of those for resistors. The series combination is always smaller than the smallest capacitor.

## Worked examples

**Example 1: Capacitance.** A capacitor stores 6.0 x 10^-6 C when connected to 12 V. Find its capacitance.
1. Use C = Q / V = 6.0 x 10^-6 / 12.
2. C = 5.0 x 10^-7 F.
3. This is 0.50 microfarad.

**Example 2: Stored energy.** A 10 microfarad capacitor is charged to 100 V. Find the energy stored.
1. Use U = 1/2 C V^2 = 0.5 x 10 x 10^-6 x 100^2.
2. The voltage squared is 10 000, so U = 0.5 x 10^-5 x 10 000.
3. The energy is U = 0.050 J.

**Example 3: Capacitors in series.** A 4.0 microfarad and a 12 microfarad capacitor are connected in series. Find the equivalent capacitance.
1. Use 1 / C = 1 / 4.0 + 1 / 12 = 3 / 12 + 1 / 12 = 4 / 12.
2. So C = 12 / 4 = 3.0 microfarads.
3. This is smaller than the 4.0 microfarad capacitor, as expected for a series connection.

## Common mistakes

A frequent error is to add series capacitors directly; the series rule needs the reciprocals. Another is forgetting the factor 1/2 in the energy formula. Students also use microfarads as if they were farads, which makes the answers wrong by a factor of a million. Finally, remember that a dielectric increases the capacitance, and that doubling the plate separation halves it.
