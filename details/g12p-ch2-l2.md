# Series and Parallel Circuits

If one bulb in a string of old-fashioned decorative lights fails, the entire string goes dark. Yet when one lamp in your home burns out, the others keep shining. The difference is the way the parts are connected: the decorative string is a series circuit, and the household wiring is parallel. Understanding the two arrangements, and how to combine them, lets you analyze almost any circuit.

## Key ideas

In a series circuit the components are connected one after another, forming a single path for the current. The same current flows through every component, because charge has nowhere else to go. The voltages across the components add up to the voltage of the source, and the equivalent resistance is the sum: R = R1 + R2 + and so on. Adding more resistors in series makes the total resistance larger and the current smaller. If any one part is broken, the path is cut, and the whole circuit stops, which is why the string of lights fails.

In a parallel circuit the components are connected across the same two points, so there are several paths for the current. Each branch has the same voltage, equal to that of the source, while the currents in the branches add up to the total current. The equivalent resistance follows 1 / R = 1 / R1 + 1 / R2 + and so on. Adding a branch gives the current an additional path, so the total resistance decreases. For this reason, the equivalent resistance of a parallel combination is always less than the smallest resistor in it. Two equal resistors R in parallel give R / 2. Houses use parallel wiring so that each appliance gets the full supply voltage and works independently of the others.

Many circuits mix the two types. The method is to reduce them step by step: replace each parallel group by its equivalent resistance, then add the series parts, and finally find the total current from Ohm's law. Afterwards, work backward to find the voltage and current of each part.

Meters must be connected correctly. An ammeter measures current, so it is placed in series with the component, and it has a very small resistance. A voltmeter measures voltage, so it is placed in parallel with the component, and it has a very large resistance.

## Worked examples

**Example 1: Series.** Resistors of 6.0 ohm and 12 ohm are connected in series across 18 V. Find the current and the voltage across each.
1. The total resistance is R = 6.0 + 12 = 18 ohm.
2. The current is I = V / R = 18 / 18 = 1.0 A, the same in both resistors.
3. The voltages are 1.0 x 6.0 = 6.0 V and 1.0 x 12 = 12 V, which add up to 18 V.

**Example 2: Parallel.** Resistors of 6.0 ohm and 12 ohm are connected in parallel. Find the equivalent resistance.
1. Use 1 / R = 1 / 6.0 + 1 / 12 = 2 / 12 + 1 / 12 = 3 / 12.
2. The equivalent resistance is R = 12 / 3 = 4.0 ohm.
3. It is smaller than both of the resistors, as it must be.

**Example 3: A mixed circuit.** A 4.0 ohm resistor is in series with a parallel pair of 6.0 ohm and 3.0 ohm.
1. For the parallel pair, 1 / R = 1 / 6.0 + 1 / 3.0 = 1 / 6.0 + 2 / 6.0 = 3 / 6.0, so R = 2.0 ohm.
2. The total is 4.0 + 2.0 = 6.0 ohm.
3. If the source is 12 V, the total current is 12 / 6.0 = 2.0 A.

## Common mistakes

Students often add parallel resistors directly, which gives a result larger than any of them. Another mistake is to forget the last step of inverting the sum after adding the reciprocals. Many connect an ammeter in parallel, which makes a short circuit because the meter has almost no resistance. Finally, remember that in a series circuit the current is common, while in a parallel circuit the voltage is common.
