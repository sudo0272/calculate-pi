# First method
The general equation to find the area of this circle below is \
![circle](./circle.jpg)

And the general equation to find the area of this triangle below is\
![triangle](./triangle.jpg)\
![\frac 1 2 a b sin C](https://latex.codecogs.com/png.image?\dpi{110}%20\frac%201%202%20a%20b%20sin%20C)

Say a and b both equal to r.

Say there're many triangles which inscribe in a circle and are exactly congruent just like this:\
![triangle inscribing in the circle](./triangles-inscribing-in-circle.jpg)

Say n is the amount of triangles.\
Then, sum of the areas of the triangles is\
![\frac 1 2 n r^2 sin \frac {360 ^{\circ}} {n}](https://latex.codecogs.com/png.image?\dpi{110}%20\frac%201%202%20n%20r^2%20sin%20\frac%20{360%20^{\circ}}%20{n})


When n converges to infinity, it will be the area of the circle.\
In mathematical expression, it is\
![\lim \_{n \to \infty} \frac 1 2 n r^2 sin \frac {360 ^{\circ}} {n}](https://latex.codecogs.com/png.image?\dpi{110}%20\lim%20_{n%20\to%20\infty}%20\frac%201%202%20n%20r^2%20sin%20\frac%20{360%20^{\circ}}%20{n})

Since they're same,\
![\pi r^2 = \lim \_{n \to \infty }\frac 1 2 n r^2 sin \frac {360 ^{\circ}} {n}](https://latex.codecogs.com/png.image?\dpi{110}%20\pi%20r^2%20=%20\lim%20_{n%20\to%20\infty%20}\frac%201%202%20n%20r^2%20sin%20\frac%20{360%20^{\circ}}%20{n})

And finally,\
![\pi = \lim \_{n \to \infty }\frac 1 2 n sin \frac {360 ^{\circ}} {n}](https://latex.codecogs.com/png.image?\dpi{110}%20\pi%20=%20\lim%20_{n%20\to%20\infty%20}\frac%201%202%20n%20sin%20\frac%20{360%20^{\circ}}%20{n})

However, we have to use pi in calculation of sine because python's sine method uses radians.\
So what we should do is to use Bhaskara I's sine approximation formula.\
It is remarkably accurate in range from 0 deg to 180 deg but not exact.\
n converges to infinity in our formula, so degree we should calculate will converge to 0, which means we can use it.\

Bhaskara I's sine approximation formula is defined as below.\
![\sin x^\circ \approx \frac{4 x (180 - x)} {40500 - x (180 - x)}](https://latex.codecogs.com/png.image?\dpi{110}%20\sin%20x^\circ%20\approx%20\frac{4%20x%20(180%20-%20x)}%20{40500%20-%20x%20(180%20-%20x)})

# Second method
![a circle inscribing in a rectangle](./circle-inscribing-in-square.jpg)\
Say there's a circle is inscribing in a square.\
The radius of the circle is 1, so the side length of the square is 2.\
We're going to put many many dots on the square.\
Say N is the number of dots on the square and M is the number of dots on the circle.\
When we put enough dots, then N represents the area of the square and M represents the area of the circle.\
Then,\
![\frac {\pi \times 1 \times 1} {2 \times 2} = \frac M N](https://latex.codecogs.com/png.image?\dpi{110}%20\frac%20{\pi%20\times%201%20\times%201}%20{2%20\times%202}%20=%20\frac%20M%20N)\
![\frac \pi 4 = \frac M N ](https://latex.codecogs.com/png.image?\dpi{110}%20\frac%20\pi%204%20=%20\frac%20M%20N)\
Finally,\
![\pi = 4 \cdot \frac M N](https://latex.codecogs.com/png.image?\dpi{110}%20\pi%20=%204%20\cdot%20\frac%20M%20N)

# Third method
The Riemann Zeta function is defined as\
![\zeta (s) = \sum _{n = 1} ^{\infty} {n ^ {-s}} = \sum _{n = 1} ^{\infty} \frac 1 {n ^ s}](https://latex.codecogs.com/png.image?\dpi{110}%20\zeta%20(s)%20=%20\sum%20_{n%20=%201}%20^{\infty}%20{n%20^%20{-s}}%20=%20\sum%20_{n%20=%201}%20^{\infty}%20\frac%201%20{n%20^%20s})\
And\
![\zeta (2) = \frac {\pi ^ 2} 6](https://latex.codecogs.com/png.image?\dpi{110}%20\zeta%20(2)%20=%20\frac%20{\pi%20^%202}%206)\
![6 \cdot \zeta (2) = \pi ^ 2](https://latex.codecogs.com/png.image?\dpi{110}%206%20\cdot%20\zeta%20(2)%20=%20\pi%20^%202)\
![\pi = \sqrt {6 \cdot \zeta (2)}](https://latex.codecogs.com/png.image?\dpi{110}%20\pi%20=%20\sqrt%20{6%20\cdot%20\zeta%20(2)})\
Finally,\
![\pi = \sqrt {6 \cdot \sum \_{n = 1} ^{\infty} \frac 1 {n ^ 2}}](https://latex.codecogs.com/png.image?\dpi{110}%20\pi%20=%20\sqrt%20{6%20\cdot%20\sum%20_{n%20=%201}%20^{\infty}%20\frac%201%20{n%20^%202}})

