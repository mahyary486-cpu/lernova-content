# Electric Power, Energy and EMF

An electricity bill charges for energy in kilowatt-hours, not for power. This lesson explains why, and it shows how to calculate the power used by a device and the energy that it consumes. It also looks at the battery itself, which is never perfect: it has an internal resistance that makes the voltage at its terminals lower than its emf when it supplies current.

## Key ideas

When a current I flows through a component with a voltage V across it, energy is transferred at the rate P = I V. This is the electrical power, measured in watts. Using Ohm's law, the same power can be written P = I^2 R or P = V^2 / R. The choice depends on what you know: use I^2 R when the current is the same, as in a series circuit, and V^2 / R when the voltage is the same, as in a parallel circuit. The energy that the resistor receives becomes heat, which is the principle of heaters and toasters.

Energy is power multiplied by time, E = P t. In SI units this is in joules, but electricity companies use the kilowatt-hour (kWh), the energy used by a 1 kW device in one hour. Since 1 kW = 1000 W and 1 h = 3600 s, 1 kWh = 3.6 x 10^6 J. The cost of using an appliance is the energy in kWh multiplied by the price per kWh.

A source of electrical energy has an emf (electromotive force), which is the energy supplied per unit charge. It is not a force but a voltage: the potential difference of the source when no current flows. A real battery has an internal resistance r, so when it supplies a current I, part of the voltage is lost inside it. The terminal voltage is V = emf - I r, and the current in a simple circuit with an external resistance R is I = emf / (R + r). The larger the current, the lower the terminal voltage, which is why car headlights dim when the starter motor draws a large current.

This also explains why electricity is sent over long distances at a high voltage. The power lost in the cables is I^2 R. For the same transmitted power P = I V, a higher voltage means a smaller current, and the loss falls with the square of the current. Fuses and circuit breakers protect circuits by cutting the current when it becomes too large.

## Worked examples

**Example 1: Power of a heater.** A heater has a resistance of 24 ohm and is connected to a 120 V supply. Find its power.
1. Use P = V^2 / R = 120^2 / 24 = 14 400 / 24.
2. The power is P = 600 W.
3. The current is I = V / R = 120 / 24 = 5.0 A, and P = I V = 5.0 x 120 = 600 W, the same result.

**Example 2: Cost of energy.** A 2.0 kW heater runs for 3.0 h, and electricity costs 0.15 dollars per kWh. Find the cost.
1. The energy is E = P t = 2.0 x 3.0 = 6.0 kWh.
2. The cost is 6.0 x 0.15.
3. The cost is 0.90 dollars.

**Example 3: Internal resistance.** A battery has an emf of 12 V and an internal resistance of 0.50 ohm. It supplies a current of 4.0 A. Find the terminal voltage.
1. The lost voltage is I r = 4.0 x 0.50 = 2.0 V.
2. The terminal voltage is V = emf - I r = 12 - 2.0.
3. V = 10 V is available to the external circuit.

## Common mistakes

Students often mix kilowatts and watts, which makes the answers wrong by a factor of 1000. Another mistake is forgetting the internal resistance and using the emf as the voltage across the load. Many also treat power and energy as the same thing; power is the rate, and energy is the total. Finally, do not use the wrong form of the power formula: P = V^2 / R needs the voltage across that resistor, not the voltage of the source, unless they are the same.
