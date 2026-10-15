# Theorems and proofs

A theorem is a statement that has been shown to be true by a logical proof, and a proof is a chain of reasons that leads from what is given to what must be shown.

## Key ideas

**Parts of a theorem.** Most theorems are written as "If hypothesis, then conclusion". Before proving, write down the Given (the hypothesis) and the To prove (the conclusion). Draw a figure and label it with the given information.

**What we may use as reasons.** We may use definitions, axioms (basic facts accepted without proof), and theorems that were proven earlier. Useful facts:
- Angles on a straight line add up to 180°.
- Angles around a point add up to 360°.
- The angles of a triangle add up to 180°.
- Vertical angles are equal.

**Direct proof.** Start from the given, make a sequence of correct steps, and arrive at the conclusion. Each step needs a reason.

**Indirect proof (proof by contradiction).** Assume that the conclusion is false. Then show that this assumption leads to a contradiction with the given or with a known fact. So the assumption is wrong, and the conclusion is true.

**Writing a proof.** A common form is two columns: statements on the left, reasons on the right. Short paragraph proofs are also fine.

## Worked examples

**Example 1.** Prove: vertical angles are equal.

Given: lines AB and CD cross at point O. Let ∠AOC and ∠BOD be vertical angles.
To prove: ∠AOC = ∠BOD.

Step 1: ∠AOC + ∠COB = 180°, because AB is a straight line.
Step 2: ∠BOD + ∠COB = 180°, because CD is a straight line.
Step 3: So ∠AOC + ∠COB = ∠BOD + ∠COB, because both equal 180°.
Step 4: Subtract ∠COB from both sides: ∠AOC = ∠BOD. Done.

**Example 2.** Prove: an exterior angle of a triangle equals the sum of the two remote interior angles.

Given: △ABC, and side BC is extended to point D. The exterior angle is ∠ACD.
To prove: ∠ACD = ∠A + ∠B.

Step 1: ∠A + ∠B + ∠ACB = 180°, because the angles of a triangle add up to 180°.
Step 2: ∠ACD + ∠ACB = 180°, because B, C, D lie on a straight line.
Step 3: So ∠ACD + ∠ACB = ∠A + ∠B + ∠ACB.
Step 4: Subtract ∠ACB from both sides: ∠ACD = ∠A + ∠B. Done.

Numerical check: if ∠A = 50° and ∠B = 60°, then ∠ACB = 70° and ∠ACD = 110° = 50° + 60°.

**Example 3.** Prove by contradiction: a triangle cannot have two right angles.

Given: a triangle ABC.
To prove: it does not have two right angles.

Step 1: Assume the opposite: ∠A = 90° and ∠B = 90°.
Step 2: Then ∠A + ∠B = 180°.
Step 3: The angle sum of a triangle is 180°, so ∠C = 180° - 180° = 0°.
Step 4: An angle of a triangle cannot be 0°. This is a contradiction.
Step 5: So the assumption is false, and a triangle cannot have two right angles.

## Common mistakes

- Starting the proof by assuming the conclusion. In a direct proof you may only start from the given and known facts.
- Writing a step without a reason, or using "it looks equal in the figure" as a reason.
- Mixing up the hypothesis and the conclusion, so that the proof proves the converse instead.
- In an indirect proof, assuming the wrong opposite. The opposite of "equal" is "not equal", and the opposite of "two right angles" is "not two right angles" (in the proof above we assumed two and found a contradiction, which is allowed because the claim was a negative statement).

## Remember

- Always write Given and To prove, and draw a labeled figure first.
- Every step in a proof needs a reason: a definition, an axiom, or a known theorem.
- In a proof by contradiction, assume the conclusion is false and look for a contradiction.
