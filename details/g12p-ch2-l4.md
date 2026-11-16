# Kirchhoff's Rules and Complex Circuits

Some circuits cannot be reduced to a simple series or parallel combination, for example a circuit with two batteries in different branches. For these, we need more general tools. Kirchhoff's rules are exactly that: two statements of conservation, one for charge and one for energy, that work for every circuit. With them, any circuit can be turned into a set of equations and solved.

## Key ideas

The junction rule states that the total current entering a junction equals the total current leaving it: the sum of currents in equals the sum of currents out. A junction is a point where three or more wires meet. The rule expresses the conservation of charge, because charge cannot accumulate at a point in a steady circuit.

The loop rule states that the sum of all potential changes around any closed loop is zero. It expresses the conservation of energy: a charge that goes around a loop and returns to its start must have the same potential energy as before. To apply it, choose a direction for travelling around the loop, and add the changes in order. When going through a battery from the negative to the positive terminal, the potential rises, so the change is +emf. When going through a resistor in the direction of the current, the potential falls, so the change is -I R. If you travel against the current, the change is +I R.

The method has a few simple steps. Draw the circuit, and assign a direction and a symbol to the current in each branch; you do not need to guess correctly. Write a junction equation for the currents and loop equations for independent loops, so that the number of equations equals the number of unknowns. Solve them. If a current comes out negative, the real direction is opposite to the one assumed, and the size is still correct. This is not an error.

A useful shortcut is the voltage divider. Two resistors R1 and R2 in series across a voltage V_in share it in proportion to their resistances, and the voltage across R2 is V_out = V_in R2 / (R1 + R2). Voltage dividers are used in sensors and volume controls.

## Worked examples

**Example 1: The junction rule.** Currents of 3.0 A and 2.0 A enter a junction, and one wire carries the current out. Find the current in that wire.
1. The current out must equal the total current in.
2. I = 3.0 + 2.0 = 5.0 A.

**Example 2: The loop rule.** A 12 V battery drives a current through a 2.0 ohm and a 4.0 ohm resistor in series. Find the current.
1. Going around the loop in the direction of the current: 12 - I x 2.0 - I x 4.0 = 0.
2. This gives 12 = 6.0 I.
3. The current is I = 2.0 A, the same as the result from R = 6.0 ohm and I = V / R.

**Example 3: A voltage divider.** A potential difference of 9.0 V is across a 3.0 ohm and a 6.0 ohm resistor in series. Find the voltage across the 6.0 ohm resistor.
1. Use V_out = V_in R2 / (R1 + R2) = 9.0 x 6.0 / (3.0 + 6.0).
2. The voltage is V = 54 / 9.0 = 6.0 V.
3. The other resistor has 3.0 V, and the two add to 9.0 V.

## Common mistakes

The most common error is mixing up the signs in the loop rule, particularly when a resistor is crossed against the current. Another is to forget the junction equation, which leaves too few equations to solve. Students also treat a negative current as an error, but it only means that the real direction is opposite to the assumed one. Finally, always check the answer by seeing that the voltages around each loop add up to zero.
