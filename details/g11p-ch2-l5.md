# Fluid Flow and Bernoulli's Principle

When a fluid moves, a surprising rule appears: where the fluid flows faster, its pressure is lower. This single idea explains why an aircraft wing lifts the plane, why a perfume sprayer pulls liquid up its tube, and why a shower curtain bends toward the water. This lesson first describes how the speed of a fluid changes in pipes of different sizes, and then shows how the speed is linked to pressure and height.

## Key ideas

The first rule is the equation of continuity. Water cannot pile up or disappear in a pipe, so the volume entering per second must equal the volume leaving per second. The flow rate is Q = A v, in cubic meters per second, where A is the cross-sectional area and v is the speed. For a pipe whose width changes, A1 v1 = A2 v2. A narrower section means a smaller area and therefore a higher speed. This is why a thumb partly covering a garden hose makes the water shoot out faster.

The second rule is Bernoulli's principle, a statement of energy conservation for a flowing fluid. For an ideal fluid that is steady and without friction, the quantity P + 1/2 rho v^2 + rho g h is the same at every point along a streamline. The three terms are the pressure, the kinetic energy per unit volume and the potential energy per unit volume. For horizontal flow, the height term is the same everywhere and can be dropped, which leaves the key result: if the speed increases, the pressure must decrease.

There are two famous applications. For a wing, the air moves faster over the curved top than under the bottom, so the pressure on top is lower, and the difference gives an upward force called lift. For a tank with a hole at a depth h below the surface, Bernoulli's equation gives Torricelli's law, v = sqrt(2 g h), the same speed as an object that has fallen freely through the height h.

It is important to remember the conditions. The equation applies along a single streamline, in steady flow of a fluid with little friction or turbulence, so it gives good estimates but not exact values for real fluids such as thick oil.

## Worked examples

**Example 1: Continuity.** A pipe narrows from a cross-section of 0.040 m^2 to 0.010 m^2. The water speed in the wide part is 2.0 m/s. Find the speed in the narrow part.
1. Use A1 v1 = A2 v2, so v2 = 0.040 x 2.0 / 0.010.
2. The speed in the narrow part is v2 = 8.0 m/s.
3. The flow rate is the same at both places: Q = 0.040 x 2.0 = 0.080 m^3/s.

**Example 2: Torricelli's law.** A hole is made in the side of a tank 5.0 m below the water surface. Use g = 9.8 m/s^2. Find the speed of the water leaving the hole.
1. Use v = sqrt(2 g h) = sqrt(2 x 9.8 x 5.0).
2. The value under the root is 98.
3. The speed is v = 9.9 m/s.

**Example 3: Pressure change.** Water at 2.0 m/s and 150 000 Pa enters a horizontal narrow section where it moves at 6.0 m/s. Find the new pressure.
1. For horizontal flow, P2 = P1 + 1/2 rho (v1^2 - v2^2) = 150 000 + 500 x (4.0 - 36).
2. The bracket is -32, so the change is 500 x (-32) = -16 000 Pa.
3. The pressure drops to P2 = 134 000 Pa in the faster section.

## Common mistakes

Students often think that faster flow means higher pressure, but it is the opposite for a fluid flowing horizontally. Another mistake is to use diameters instead of areas in the continuity equation; areas depend on the square of the diameter. A third mistake is to apply Bernoulli's equation between points that are not on the same streamline or in a flow that is not steady. Finally, do not forget that the height term matters when the two points are at different heights.
