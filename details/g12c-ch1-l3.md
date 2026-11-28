# pH Calculations for Strong and Weak Acids and Bases

A weak acid and a strong acid of the same concentration have very different pH values, because the weak acid gives far fewer H3O+ ions. A 0.10 M solution of acetic acid has a pH near 3, while 0.10 M hydrochloric acid has a pH of 1. To calculate pH correctly, you must first decide whether the substance is strong or weak, since the method is different in each case. This lesson gives the method for each, and it shows how the answer is checked.

## Key ideas

The pH is defined as pH = -log [H3O+], and pOH = -log [OH-]. For a strong acid, the ionization is complete, so the concentration of H3O+ equals the concentration of the acid, for a monoprotic acid, and pH = -log C. For a strong base, the concentration of OH- equals the concentration of the base multiplied by the number of hydroxide ions in its formula, so Ba(OH)2 gives two. Then pOH = -log [OH-], and pH = 14 - pOH.

A weak acid needs an equilibrium calculation. If the initial concentration is C and the amount that ionizes is x, then Ka = x^2 / (C - x). When Ka is small compared with C, x is much smaller than C, so C - x is close to C, and the formula simplifies to x = sqrt(Ka C). Here x is [H3O+], and the pH is -log x. The approximation should always be checked. A usual test is that x is less than 5 percent of C. A weak base is treated in the same way, using Kb, and the result x is [OH-].

The percent ionization = x / C x 100 percent. It shows how little of a weak acid is ionized, and it increases when the solution is more dilute, because the equilibrium shifts toward more ionization.

A salt can also change pH when it dissolves, because its ions may react with water. The salt of a weak acid and a strong base, such as sodium acetate, gives a basic solution, because the acetate ion is a weak base. The salt of a strong acid and a weak base, such as ammonium chloride, gives an acidic solution. The salt of a strong acid and a strong base, such as NaCl, is neutral.

## Worked examples

**Example 1: Strong acid.** Find the pH of 0.010 M HCl.
1. HCl ionizes completely, so [H3O+] = 0.010 M = 10^-2 M.
2. pH = -log(10^-2) = 2.00.

**Example 2: Weak acid.** Find the pH of 0.10 M acetic acid, with Ka = 1.8 x 10^-5.
1. Use the approximation x = sqrt(Ka C) = sqrt(1.8 x 10^-5 x 0.10) = sqrt(1.8 x 10^-6) = 1.34 x 10^-3 M.
2. pH = -log(1.34 x 10^-3) = 2.87.
3. Check: x / C = 0.00134 / 0.10 = 1.3 percent, which is less than 5 percent, so the approximation is valid.

**Example 3: Strong base.** Find the pH of 0.020 M Ba(OH)2.
1. Each formula unit gives two hydroxide ions, so [OH-] = 2 x 0.020 = 0.040 M.
2. pOH = -log(0.040) = 1.40.
3. pH = 14 - 1.40 = 12.60.

## Common mistakes

Students often forget that Ba(OH)2 releases two hydroxide ions, which makes the pH wrong by 0.30 units. Another error is to use the strong-acid shortcut for a weak acid, which would give pH 1.00 for the acetic acid in Example 2 instead of 2.87. A third mistake is to skip the check of the approximation. If x is not small compared with C, the quadratic equation must be solved, or the answer will be wrong.
