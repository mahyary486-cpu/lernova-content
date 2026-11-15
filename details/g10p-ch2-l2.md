# Vector Addition and Components

Adding vectors means finding the single vector, called the resultant, that has the same effect as all of them together. If two people pull a boat with ropes in different directions, the boat moves as if one person pulled with the resultant force. Because vectors have direction, ordinary addition does not always work, and we need two tools: a drawing method and a calculation method. This lesson explains both and shows why splitting vectors into components makes every problem manageable.

## Key ideas

The drawing method is called tip-to-tail. Draw the first vector, then start the second vector at the tip of the first, and continue in the same way. The resultant is the arrow from the tail of the first vector to the tip of the last. Two special cases come out of this picture without any calculation: when vectors point the same way, their magnitudes add, and when they point in opposite ways, their magnitudes subtract. For two perpendicular vectors A and B, the resultant is R = sqrt(A^2 + B^2), and the angle from A is found with tan(theta) = B / A.

Most real problems involve vectors at awkward angles. The solution is to use components. Any vector A at an angle theta above the x-axis can be replaced by two perpendicular vectors: a horizontal part Ax = A cos(theta) and a vertical part Ay = A sin(theta). Cosine goes with the side next to the angle, and sine goes with the side opposite it. Together the components have exactly the same effect as the original vector.

The component method turns any addition into three steps. First, break every vector into x and y components, giving each component a sign: east and north are positive, west and south are negative. Second, add all the x components to get Rx and all the y components to get Ry. Third, combine them with R = sqrt(Rx^2 + Ry^2) and theta = tan^-1(Ry / Rx). The method works for any number of vectors at any angles, which is why it is the standard tool of physics.

A useful check is that the magnitude of the resultant of two vectors always lies between the difference and the sum of their magnitudes. If your answer falls outside this range, you made an error. Finally, forces are in equilibrium when their resultant is zero, which means that both Rx and Ry are zero.

## Worked examples

**Example 1: Components of a force.** A 40 N force acts at 30 degrees above the horizontal. Find its components.
1. The horizontal component is Fx = 40 cos(30) = 40 x 0.866 = 34.6 N.
2. The vertical component is Fy = 40 sin(30) = 40 x 0.500 = 20 N.
3. As a check, sqrt(34.6^2 + 20^2) = sqrt(1597) = 40 N, which returns the original force.

**Example 2: Perpendicular forces.** A 12 N force acts east and a 5.0 N force acts north. Find the resultant.
1. The forces are perpendicular, so R = sqrt(12^2 + 5.0^2) = sqrt(169) = 13 N.
2. The angle is theta = tan^-1(5.0 / 12) = 22.6 degrees.
3. The resultant is 13 N at 22.6 degrees north of east.

**Example 3: The component method.** A bird flies with a velocity of 10.0 m/s east in still air, and a gust adds a second velocity of 8.0 m/s at 50 degrees above east. Find the total velocity.
1. The x components add: Rx = 10.0 + 8.0 cos(50) = 10.0 + 5.14 = 15.14 m/s.
2. The y components add: Ry = 0 + 8.0 sin(50) = 6.13 m/s.
3. The magnitude is R = sqrt(15.14^2 + 6.13^2) = 16.3 m/s.
4. The direction is theta = tan^-1(6.13 / 15.14) = 22 degrees above east.

## Common mistakes

A very common error is using sine for the horizontal component when the angle is measured from the horizontal; the horizontal part goes with cosine, because it is the side next to the angle. Students also add the magnitudes of vectors that do not point the same way, which always overestimates the resultant. Another error is to lose the signs: a component pointing west or south must be negative, or the sum comes out wrong. Finally, check that the calculator is in degrees mode; a calculator set to radians gives completely different values for sine and cosine.
