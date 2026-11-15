# Equations of Motion with Constant Acceleration

Many real motions have an acceleration that stays nearly constant: a car braking steadily, a sprinter pulling away from the blocks, a stone falling in air. For such motion, five quantities describe everything: the displacement d, the initial velocity v0, the final velocity v, the acceleration a and the time t. A small set of equations, often called the kinematic equations, connects them. If you know any three of the five, you can find the others. This lesson shows how to choose the right equation quickly and safely.

## Key ideas

There are four equations, and each one leaves out one of the five quantities. The first is v = v0 + at, which does not contain the displacement. The second is d = v0 t + (1/2) a t^2, which does not contain the final velocity. The third is v^2 = v0^2 + 2ad, which does not contain the time. The fourth is d = ((v0 + v) / 2) t, which does not contain the acceleration. The reason for having four is practical: the right choice is the one that contains the quantity you want and does not contain the quantity you neither know nor need.

A reliable plan makes the work straightforward. First, choose a positive direction and write down every known quantity with its sign, for example a = -5.0 m/s^2 for a braking car moving in the positive direction. Second, write the unknown. Third, find the equation that holds the unknown and the knowns but leaves out the missing quantity. Fourth, solve, and check that the units and the size of the answer make sense.

These equations are valid only if the acceleration is constant during the whole time. If the acceleration changes, they cannot be used for the entire motion. A second condition appears in braking problems: the equations describe the motion only until the object stops. After the car comes to rest, the brakes do not push it backward, so continuing to apply the equation would describe a motion that never happens.

The third equation shows an important fact about stopping. Since d is proportional to v0^2 when v = 0 and a is fixed, a car moving twice as fast needs four times the distance to stop. This is why speed limits near schools matter far more than the numbers suggest.

## Worked examples

**Example 1: Distance from rest.** A bike starts from rest and accelerates at 4.0 m/s^2 for 3.0 s. How far does it go?
1. Known: v0 = 0, a = 4.0 m/s^2, t = 3.0 s. The unknown is d, and the final velocity is not needed.
2. Use d = v0 t + (1/2) a t^2 = 0 + 0.5 x 4.0 x 3.0^2 = 0.5 x 4.0 x 9.0.
3. The displacement is d = 18 m.

**Example 2: Stopping distance.** A car at 20 m/s brakes with a = -5.0 m/s^2 until it stops. How far does it travel?
1. Known: v0 = 20 m/s, v = 0, a = -5.0 m/s^2. Time is not given, so the third equation is the natural choice.
2. Write v^2 = v0^2 + 2ad, which gives 0 = 400 + 2 x (-5.0) x d.
3. This becomes 10d = 400, so d = 40 m.

**Example 3: Stopping before the time ends.** A car at 15 m/s brakes with a = -3.0 m/s^2. How far does it travel in 7.0 s?
1. First find the time to stop: t = 15 / 3.0 = 5.0 s. The car is already at rest before 7.0 s have passed.
2. So only the first 5.0 s matter: d = v0^2 / (2 x 3.0) = 225 / 6.0 = 37.5 m.
3. Putting t = 7.0 s into the second equation would give 31.5 m, a smaller and wrong answer, because it pretends the car reverses.

## Common mistakes

The biggest mistake is using these equations when the acceleration is not constant. A second is ignoring signs: if the velocity is positive and the car brakes, the acceleration must be negative. Students also forget the factor one half in d = (1/2) a t^2 or the factor 2 in 2ad. When solving v^2 = something, many forget to take the square root at the end, and give the square of the speed instead. Lastly, applying the equations after the object has already stopped gives results that do not match reality.
