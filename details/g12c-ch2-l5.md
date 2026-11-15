# The Nernst Equation, Batteries and Corrosion

Rust never sleeps: iron constantly forms a tiny galvanic cell with water and oxygen.

## Key ideas
- **E = E0 - (0.0592 / n) log Q** (25 C).
- At equilibrium **E = 0**.
- **Primary**: not rechargeable; **secondary**: rechargeable (lead-acid, Li-ion).
- **Fuel cell**: H2 + O2 continuously supplied, product H2O.
- **Rusting**: iron oxidized with water and O2.
- **Galvanizing** and **sacrificial anodes** protect iron.

## Worked examples
**Example 1: Nernst.** Zn-Cu cell with [Zn^2+] = 1.0 M and [Cu^2+] = 0.010 M (E0 = 1.10 V, n = 2).
1. Q = [Zn^2+] / [Cu^2+] = 100 and log Q = 2.
2. E = 1.10 - (0.0592 / 2) x 2 = 1.10 - 0.059 = 1.04 V.

**Example 2: Sacrificial anode.** Why does a magnesium block protect a steel hull?
1. Magnesium is oxidized more easily than iron.
2. It corrodes instead of the iron.

**Example 3: Fuel cell.** What are the reactions in a hydrogen fuel cell?
1. Anode: H2 -> 2 H+ + 2 e-; cathode: O2 + 4 H+ + 4 e- -> 2 H2O.
2. The only product is water.

## Common mistakes
- Using ln instead of log with 0.0592.
- Forgetting that Q uses concentrations of products over reactants.
- Thinking a fuel cell stores energy.
