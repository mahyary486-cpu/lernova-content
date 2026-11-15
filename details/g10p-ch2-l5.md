# Projectile Motion Launched at an Angle

A football kicked upward, a javelin thrown across a field and a cannonball fired from a gun all start with a velocity that points partly up and partly forward. The launch angle matters a great deal: too flat and the object lands quickly, too steep and it goes high but not far. The method is the same one used for horizontal launches. Split the launch velocity into components, analyze each direction separately, and join the results through the common time.

## Key ideas

If a projectile leaves with speed v at an angle theta above the horizontal, its initial components are vx = v cos(theta) and vy = v sin(theta). The horizontal component stays constant for the whole flight, because no horizontal force acts. The horizontal distance is x = vx t. The vertical component changes steadily, because gravity gives an acceleration of -g. The vertical velocity at time t is vy - g t.

The highest point is where the vertical velocity becomes zero, so the time to the top is t = vy / g. If the projectile lands at the same height from which it was launched, the way down is the mirror image of the way up, and the total time of flight is T = 2 vy / g. The maximum height is H = vy^2 / (2g). The horizontal range on level ground is R = vx T, which can be written as R = v^2 sin(2 theta) / g.

This formula explains why the angle matters. The range is largest at 45 degrees, where sin(2 theta) equals 1. Two angles that add up to 90 degrees, such as 30 and 60, give the same range, because sin(60) equals sin(120). The steeper throw stays in the air longer, but the flatter throw moves faster sideways, and the two effects balance exactly.

At the top of the path the object is not at rest. Only the vertical component is zero there, and the velocity is horizontal and equals vx. This is why a ball thrown at an angle still moves forward at the highest point. Remember also that mass does not matter when air resistance is ignored, so a heavy and a light projectile launched in the same way follow the same path.

## Worked examples

**Example 1: A full analysis.** A ball is launched at 25 m/s at 40 degrees above level ground. Find the time of flight, the maximum height and the range.
1. The components are vx = 25 cos(40) = 19.2 m/s and vy = 25 sin(40) = 16.1 m/s.
2. The time to the top is 16.1 / 9.8 = 1.64 s, so the total time is T = 3.28 s.
3. The maximum height is H = 16.1^2 / (2 x 9.8) = 13.2 m.
4. The range is R = vx T = 19.2 x 3.28 = 62.8 m.

**Example 2: Complementary angles.** A ball is kicked at 20 m/s. Compare the ranges at 30, 60 and 45 degrees.
1. At 30 degrees: R = 20^2 x sin(60) / 9.8 = 400 x 0.866 / 9.8 = 35.3 m.
2. At 60 degrees: R = 20^2 x sin(120) / 9.8 = 35.3 m, the same value.
3. At 45 degrees: R = 400 x 1 / 9.8 = 40.8 m, the largest range possible at this speed.

**Example 3: Speed at the top.** A projectile is launched at 50 m/s at 60 degrees. What is its speed at the highest point?
1. At the top the vertical component is zero, but the horizontal component is unchanged.
2. The speed equals vx = 50 cos(60) = 50 x 0.5.
3. The speed at the top is 25 m/s, half of the launch speed.

## Common mistakes

Many students say that the velocity is zero at the top of the path, but only the vertical part is zero. Another common error is mixing up sine and cosine; the horizontal component uses cosine when the angle is measured from the horizontal. The range formula is valid only when the landing height equals the launch height, so using it for a launch from a cliff gives a wrong result. Finally, do not believe that a heavier projectile follows a different path; without air resistance, mass has no effect on the motion.
