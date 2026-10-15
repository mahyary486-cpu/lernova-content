# Factoring

Factoring is writing a polynomial as a product of simpler polynomials, which is the reverse of multiplying.

## Key ideas

- First look for the greatest common factor (GCF). It is the largest monomial that divides every term. Take it out in front of brackets: ax + ay = a(x + y).
- Difference of squares: a^2 - b^2 = (a + b)(a - b). Both terms must be perfect squares with a minus sign between them.
- Perfect square trinomials: a^2 + 2ab + b^2 = (a + b)^2 and a^2 - 2ab + b^2 = (a - b)^2.
- Trinomial x^2 + sx + p: find two numbers m and n with m + n = s and m * n = p. Then the factored form is (x + m)(x + n).
- Grouping: for four terms, split them into two pairs, take a common factor from each pair, and then take out the common bracket.
- Often several methods are used together. Take out the GCF first, then check whether the remaining factor can be factored more.
- Factor completely: continue until no factor can be split further.
- Check by expanding. If you multiply the factors, you must get the original polynomial.

## Worked examples

**Example 1.** Factor 12x^3 - 18x^2.

Step 1: The GCF of 12 and 18 is 6. The smallest power of x is x^2. So the GCF is 6x^2.
Step 2: Divide each term by 6x^2: 12x^3 / 6x^2 = 2x and 18x^2 / 6x^2 = 3.
Step 3: The result is 6x^2(2x - 3).
Check: 6x^2 * 2x = 12x^3 and 6x^2 * (-3) = -18x^2.

**Example 2.** Factor x^2 + 7x + 12.

Step 1: We need two numbers with product 12 and sum 7.
Step 2: The pairs with product 12 are 1 and 12, 2 and 6, 3 and 4. Only 3 + 4 = 7.
Step 3: The result is (x + 3)(x + 4).
Check: x^2 + 4x + 3x + 12 = x^2 + 7x + 12.

**Example 3.** Factor 2x^3 - 8x completely.

Step 1: The GCF is 2x. Take it out: 2x^3 - 8x = 2x(x^2 - 4).
Step 2: Now x^2 - 4 = x^2 - 2^2 is a difference of squares, so it equals (x + 2)(x - 2).
Step 3: The complete factorization is 2x(x + 2)(x - 2).
Check: (x + 2)(x - 2) = x^2 - 4, and 2x(x^2 - 4) = 2x^3 - 8x.

## Common mistakes

- Not taking out the whole GCF, for example writing 12x^3 - 18x^2 = 3x(4x^2 - 6x). This is correct but not complete, because 2x is still a common factor inside the bracket.
- Trying to factor a sum of squares such as x^2 + 4 with the difference of squares rule. It does not apply.
- Forgetting the leftover 1 when a whole term is the common factor: 3x + 3 = 3(x + 1), not 3(x).
- Choosing numbers with the right product but the wrong sum. Always check both conditions.

## Remember

- Always look for a common factor first.
- Know the patterns: difference of squares and perfect squares.
- Check every factorization by multiplying it back.
