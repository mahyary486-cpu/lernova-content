# Gauss's Law and Conductors

A car acts as a shield during a lightning storm. People inside it are safe even if lightning strikes the roof, because the metal body keeps the electric field inside equal to zero. Gauss's law explains why. It is a powerful statement that connects the electric field on a closed surface to the charge inside, and it lets us find fields of symmetric charge distributions without long calculations.

## Key ideas

Electric flux measures how much electric field passes through a surface. For a flat surface of area A in a uniform field E, the flux is the product E A cos(theta), where theta is the angle between the field direction and the line perpendicular to the surface. The flux is largest when the field is perpendicular to the surface (theta = 0) and zero when the field is parallel to it. Its unit is N m^2/C.

Gauss's law says that the total flux through any closed surface equals the net charge enclosed divided by epsilon_0: flux = Q_enclosed / epsilon_0. The constant epsilon_0 = 8.85 x 10^-12 C^2/(N m^2) is called the permittivity of free space, and it is related to Coulomb's constant by k = 1 / (4 pi epsilon_0). Only the charge inside the surface counts; charges outside may create fields that pass through the surface, but they enter and leave, and their net flux is zero. The surface must be closed, like a sphere or a box, for the law to apply.

When the charge distribution has symmetry, Gauss's law gives the field quickly. For a charged sphere, the field outside is the same as if all the charge were concentrated at the center: E = k Q / r^2. Near the surface of a charged conductor, the field is perpendicular to the surface and has the size E = sigma / epsilon_0, where sigma is the surface charge density, the charge per unit area.

The law explains the behavior of conductors. In equilibrium, the field inside a conductor is zero and any excess charge lies on its outer surface. A hollow conductor therefore shields its inside from external fields, and this is called a Faraday cage. Cars, airplanes and shielded cables protect their contents in the same way.

## Worked examples

**Example 1: Flux.** A uniform field of 200 N/C passes perpendicularly through a surface of area 0.50 m^2. Find the flux.
1. Use flux = E A cos(theta), with theta = 0 and cos(0) = 1.
2. Flux = 200 x 0.50 x 1.
3. The flux is 100 N m^2/C.

**Example 2: Enclosed charge.** The flux through a closed surface is 1.13 x 10^3 N m^2/C. Find the charge inside.
1. Use Q = flux x epsilon_0 = 1.13 x 10^3 x 8.85 x 10^-12.
2. The charge is Q = 1.0 x 10^-8 C.
3. The result does not depend on the shape of the surface or on where the charge sits inside.

**Example 3: Field near a conductor.** The surface of a conductor has a charge density of sigma = 2.0 x 10^-6 C/m^2. Find the field just outside it.
1. Use E = sigma / epsilon_0 = 2.0 x 10^-6 / 8.85 x 10^-12.
2. The field is E = 2.26 x 10^5 N/C, perpendicular to the surface.

## Common mistakes

Students often apply Gauss's law to a surface that is not closed, where the simple result fails. Another error is to count charges outside the surface when finding the enclosed charge. Many forget the angle in the flux formula, using E A even when the field is tilted. Finally, do not think that zero flux means zero field; it means that the net charge inside is zero, and the field may still be present on the surface.
