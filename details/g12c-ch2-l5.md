# The Nernst Equation, Batteries and Corrosion

Rust never sleeps. As long as there is water and oxygen, a piece of iron forms tiny galvanic cells on its surface and slowly turns into iron oxide. The same electrochemical ideas explain how batteries work, why they eventually go flat, and how engineers protect ships and pipelines. Real cells rarely work with the standard concentrations of 1 M, so we also need an equation that gives the potential under other conditions.

## Key ideas

The Nernst equation gives the potential of a cell at any concentrations: E = E0 - (0.0592 / n) log Q, at 25 degrees C. Here n is the number of electrons in the balanced equation and Q is the reaction quotient, which is written like K, with products over reactants. When Q is less than 1, the logarithm is negative and E is larger than E0. As the reaction proceeds, Q grows, and E falls. At equilibrium Q = K and E = 0, so the cell is flat, and no more current can be drawn. This is why a battery runs down.

Batteries are divided into two groups. A primary battery cannot be recharged, because its reaction cannot be easily reversed, as in an alkaline cell. A secondary battery can be recharged by supplying electrical energy to reverse the reaction, as in lead-acid car batteries and lithium-ion cells. A fuel cell is different. The reactants, hydrogen and oxygen, are supplied continuously from outside, and the only product is water. It does not store energy, and it produces current for as long as the fuel is supplied.

Corrosion is the unwanted oxidation of a metal. Iron is oxidized at one point, where it acts as an anode, and the electrons travel through the metal to another point, where oxygen is reduced in the presence of water. The Fe 2+ ions that form are oxidized further to rust. Salt speeds the process by making the water a better conductor. To prevent it, the iron can be coated with a layer of paint or zinc, which is called galvanizing. If the zinc coating is scratched, it still protects the iron, because zinc is oxidized more easily. A sacrificial anode works in the same way. A block of magnesium or zinc is attached to the steel, and it corrodes instead of the iron.

## Worked examples

**Example 1: The Nernst equation.** A Zn-Cu cell has [Zn 2+] = 1.0 M and [Cu 2+] = 0.010 M, with E0 = 1.10 V and n = 2.
1. The reaction is Zn + Cu 2+ -> Zn 2+ + Cu, so Q = [Zn 2+] / [Cu 2+] = 1.0 / 0.010 = 100, and log Q = 2.
2. E = 1.10 - (0.0592 / 2) x 2 = 1.10 - 0.059.
3. E = 1.04 V, which is lower than the standard value, because the product concentration is high and the reactant concentration is low.

**Example 2: A sacrificial anode.** Why does a magnesium block protect a steel hull?
1. Magnesium is oxidized more easily than iron, since it has a lower reduction potential.
2. It therefore acts as the anode and corrodes in place of the iron, while the hull becomes the cathode.
3. The block has to be replaced from time to time, which is why it is called sacrificial.

**Example 3: A hydrogen fuel cell.** What are the reactions?
1. At the anode, hydrogen is oxidized: H2 -> 2 H+ + 2 e-.
2. At the cathode, oxygen is reduced: O2 + 4 H+ + 4 e- -> 2 H2O.
3. The overall reaction is 2 H2 + O2 -> 2 H2O, and the only product is water.

## Common mistakes

A frequent error is to use the natural logarithm with the constant 0.0592, which is valid only for log base 10. Another is to write Q upside down, with reactants over products. The third is to think that a fuel cell stores energy like a battery, when in fact it converts the energy of a fuel that is supplied from outside.
