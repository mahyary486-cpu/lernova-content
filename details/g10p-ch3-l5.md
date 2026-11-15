# Friction and Inclined Planes

Friction is the contact force that resists sliding between two surfaces. Without it, we could not walk, cars could not brake, and a nail would not stay in a board. On a slope, friction competes with a component of the weight, and the winner decides whether the object slides, stays still, or moves at a steady speed. This lesson combines the friction law with components of weight to solve these problems.

## Key ideas

There are two kinds of friction. Static friction acts when the surfaces are not sliding. It adjusts itself to match the push, up to a maximum value, f_s,max = mu_s N, where mu_s is the coefficient of static friction and N is the normal force. Kinetic friction acts while the surfaces slide, and it equals f_k = mu_k N. Usually mu_k is smaller than mu_s, which is why it takes more effort to start a heavy box moving than to keep it moving.

Friction is parallel to the surface and points opposite to the sliding, or to the attempted sliding. The normal force N is the key quantity in both formulas, and finding it correctly is the main task. On a level floor with no vertical pushes, N = mg. On a slope this is no longer true, and a more careful analysis is needed.

On an incline of angle theta, it is best to tilt the axes: one along the slope and one perpendicular to it. The weight mg is then split into a component along the slope, mg sin(theta), which tries to pull the object down, and a component perpendicular to the slope, mg cos(theta), which presses the object into the surface. The normal force balances the perpendicular part, so N = mg cos(theta). Without friction the acceleration down the slope is a = g sin(theta), independent of the mass. With friction opposing the sliding, a = g sin(theta) - mu_k g cos(theta). If the block slides at constant speed, the acceleration is zero and mu_k = tan(theta).

## Worked examples

**Example 1: Pushing a crate.** A 50 kg crate on a level floor has mu_s = 0.40 and mu_k = 0.30. It is pushed with 250 N. Use g = 9.8 m/s^2. Does it move, and what is its acceleration?
1. The normal force is N = mg = 50 x 9.8 = 490 N.
2. The maximum static friction is 0.40 x 490 = 196 N, and 250 N is greater than 196 N, so the crate slides.
3. The kinetic friction is 0.30 x 490 = 147 N.
4. The acceleration is a = (250 - 147) / 50 = 2.06, about 2.1 m/s^2.

**Example 2: A frictionless ramp.** A 20 kg block rests on a 25 degree frictionless incline. Find the force along the slope, the acceleration and the normal force.
1. The force along the slope is mg sin(25) = 20 x 9.8 x 0.4226 = 82.8 N.
2. The acceleration is a = g sin(25) = 9.8 x 0.4226 = 4.1 m/s^2.
3. The normal force is N = mg cos(25) = 20 x 9.8 x 0.9063 = 177.6 N, about 178 N.

**Example 3: A ramp with friction.** The same block now slides with mu_k = 0.10. Find its acceleration.
1. The friction force is 0.10 x 177.6 = 17.8 N, directed up the slope.
2. The net force along the slope is 82.8 - 17.8 = 65.0 N.
3. The acceleration is a = 65.0 / 20 = 3.25, about 3.3 m/s^2, smaller than the frictionless value.

## Common mistakes

A widespread error is to use N = mg on a slope, where the correct normal force is mg cos(theta). Another is to mix up sine and cosine in the weight components; the part along the slope uses sine, and the part perpendicular uses cosine. Students also use the weight itself as the friction force, but friction is mu times N. Finally, do not assume that static friction always equals mu_s N; it equals only what is needed to prevent sliding, up to that limit.
