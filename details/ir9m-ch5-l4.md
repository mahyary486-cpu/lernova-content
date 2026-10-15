# Division of polynomials

This lesson explains how to divide one polynomial by another, using the same ideas as long division of numbers.

## Key ideas

- To divide a polynomial by a monomial, divide every term separately: (a + b) / c = a/c + b/c. Use x^m / x^n = x^(m-n) for powers.
- To divide by a polynomial with more than one term, use long division. Write both polynomials in descending order of powers. If a power is missing, write it with coefficient 0.
- Step A: Divide the first term of the dividend by the first term of the divisor. This is the next term of the quotient.
- Step B: Multiply the whole divisor by that term and subtract the result from the dividend.
- Step C: Repeat with what is left. Stop when the degree of the remainder is lower than the degree of the divisor.
- The division relationship is: dividend = divisor * quotient + remainder. Use it to check your answer.
- If the remainder is 0, the divisor is a factor of the dividend, and the division is exact.
- Remainder rule: when a polynomial p(x) is divided by (x - c), the remainder equals p(c).

## Worked examples

**Example 1.** Divide 12x^3 - 8x^2 + 4x by 4x.

Step 1: Divide each term: 12x^3 / 4x = 3x^2, then -8x^2 / 4x = -2x, then 4x / 4x = 1.
Step 2: The quotient is 3x^2 - 2x + 1.
Check: 4x(3x^2 - 2x + 1) = 12x^3 - 8x^2 + 4x.

**Example 2.** Divide 2x^2 + 7x + 3 by x + 3.

Step 1: Divide the first terms: 2x^2 / x = 2x. This is the first term of the quotient.
Step 2: Multiply: 2x(x + 3) = 2x^2 + 6x. Subtract: (2x^2 + 7x) - (2x^2 + 6x) = x. Bring down 3 to get x + 3.
Step 3: Divide x by x to get 1. Multiply: 1(x + 3) = x + 3. Subtract: (x + 3) - (x + 3) = 0.
The quotient is 2x + 1 and the remainder is 0.
Check: (2x + 1)(x + 3) = 2x^2 + 6x + x + 3 = 2x^2 + 7x + 3.

**Example 3.** Divide x^3 - 2x^2 - 5x + 7 by x - 3.

Step 1: x^3 / x = x^2. Multiply: x^2(x - 3) = x^3 - 3x^2. Subtract: (x^3 - 2x^2) - (x^3 - 3x^2) = x^2. Bring down -5x to get x^2 - 5x.
Step 2: x^2 / x = x. Multiply: x(x - 3) = x^2 - 3x. Subtract: (x^2 - 5x) - (x^2 - 3x) = -2x. Bring down 7 to get -2x + 7.
Step 3: -2x / x = -2. Multiply: -2(x - 3) = -2x + 6. Subtract: (-2x + 7) - (-2x + 6) = 1.
The quotient is x^2 + x - 2 and the remainder is 1.
Check: (x - 3)(x^2 + x - 2) + 1 = x^3 - 2x^2 - 5x + 6 + 1 = x^3 - 2x^2 - 5x + 7. Also p(3) = 27 - 18 - 15 + 7 = 1, which matches the remainder rule.

## Common mistakes

- Forgetting to include missing powers. For x^3 + 1, write x^3 + 0x^2 + 0x + 1 before dividing.
- Making sign errors when subtracting. Subtract every term of the product, not only the first one.
- Dividing by only the first term of a binomial divisor in an expression like (a + b) / (c + d). You cannot split the denominator term by term.
- Stopping too early or too late. Stop only when the remainder has lower degree than the divisor.

## Remember

- dividend = divisor * quotient + remainder.
- Write in descending order and keep place holders for missing powers.
- A remainder of 0 means the divisor is a factor.
