# Approximation

Approximation means using a number that is close to an exact value, and measuring how close it is.

## Key ideas

- Many real numbers, such as π and √2, have infinite decimals. In practice we use approximations with a limited number of decimal places.
- Rounding rule: look at the digit after the place you keep. If it is 5 or more, increase the kept digit by 1. If it is 4 or less, leave it the same.
- Error = |exact value - approximate value|. It is always 0 or positive.
- Relative error = error / |exact value|. It can be written as a percent. It shows how big the error is compared with the size of the number.
- A result can be an approximation from below (smaller than the exact value) or from above (larger).
- To approximate √n, find two decimals whose squares are just below and just above n. Narrow the interval one decimal place at a time.
- In a calculation, do the rounding at the end. Rounding early can make the final answer less accurate.
- A better approximation has a smaller error.

## Worked examples

Example 1. Round 3.14159 to two decimal places and to three decimal places.
Step 1: For two places, the digits kept are 3.14. The next digit is 1, which is less than 5, so the answer is 3.14.
Step 2: For three places, the digits kept are 3.141. The next digit is 5, so round up. The answer is 3.142.

Example 2. Approximate √7 to two decimal places.
Step 1: 2^2 = 4 and 3^2 = 9, so √7 is between 2 and 3.
Step 2: 2.6^2 = 6.76 and 2.7^2 = 7.29, so √7 is between 2.6 and 2.7.
Step 3: 2.64^2 = 6.9696 and 2.65^2 = 7.0225, so √7 is between 2.64 and 2.65.
Step 4: Compare the distances to 7: 7 - 6.9696 = 0.0304 and 7.0225 - 7 = 0.0225. The second is smaller, so 7 is closer to 2.65^2.
So √7 ≈ 2.65. The calculator value is 2.6458..., which agrees.

Example 3. The fraction 22/7 is used as an approximation of π ≈ 3.14159. Find the error and the relative error.
Step 1: 22/7 = 3.142857... (to six decimal places).
Step 2: Error = |3.14159 - 3.142857| ≈ 0.00127.
Step 3: Relative error = 0.00127 / 3.14159 ≈ 0.0004, which is about 0.04%.
So 22/7 is a good approximation, but it is not exact.

## Common mistakes

- Rounding 2.649 to one decimal place by looking at the last digit only. Look only at the digit right after the place you keep: 2.649 becomes 2.6.
- Rounding in the middle of a long calculation, which increases the final error.
- Writing π = 3.14. The correct statement is π ≈ 3.14.
- Giving a negative error. Error is an absolute value, so it is never negative.

## Remember

- Round up when the next digit is 5 or more; otherwise keep the digit.
- Error = |exact - approximate|.
- Use squares to trap a square root between two decimals.
