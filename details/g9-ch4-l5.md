# Geometric Sequences

## Definition
A **geometric sequence** is a list of numbers where each term is found by multiplying the previous term by the same number, the **common ratio r**.

Example: 3, 6, 12, 24, ... has r = 2. And 81, 27, 9, 3, ... has r = 1/3.

To find r, divide any term by the term before it: r = a2 / a1.

## Formulas
- **Recursive:** a(n) = a(n-1) x r.
- **Explicit:** **a(n) = a1 x r^(n-1)**, where a1 is the first term and n is the term number.

The explicit formula is an exponential function of n, with the domain limited to whole numbers 1, 2, 3, and so on. Compare this with an arithmetic sequence, which adds a common difference and is linear.

## Worked examples
**Example 1.** Find the 7th term of 2, 6, 18, 54, ...
1. r = 6 / 2 = 3 and a1 = 2.
2. a(7) = 2 x 3^6 = 2 x 729.
3. a(7) = 1,458.

**Example 2.** A geometric sequence has a1 = 5 and r = -2. Write the first four terms.
1. 5.
2. 5 x (-2) = -10.
3. -10 x (-2) = 20.
4. 20 x (-2) = -40.
Terms: 5, -10, 20, -40. A negative ratio makes the signs alternate.

**Example 3.** Which term of 4, 8, 16, ... equals 256?
1. a(n) = 4 x 2^(n-1) = 256.
2. Divide by 4: 2^(n-1) = 64 = 2^6.
3. So n - 1 = 6 and n = 7.

## Telling sequences apart
Check differences first. If they are constant, the sequence is arithmetic. Otherwise check ratios. If the ratios are constant, it is geometric. For 2, 4, 8: differences 2, 4 (not constant) and ratios 2, 2 (constant), so it is geometric.

## Common mistakes
- Using r^n instead of r^(n-1) in the explicit formula.
- Multiplying a1 by r before applying the exponent: 3 x 2^4 is 48, not 6^4.
- Calling a sequence geometric after checking only one ratio.
- Forgetting that r can be negative or a fraction.
