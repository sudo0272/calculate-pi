The general equation to find the area of this circle below is
![circle](./circle.jpg)
![\pi r^2](./area-of-circle.svg)

And the general equation to find the area of this triangle below is
![triangle](./triangle.jpg)
![\frac 1 2 \:  a b \: sin C](./area-of-triangle.svg)

Say there're many triangles which inscribe in a circle and are exactly congruent just like this:
![triangle inscribing in the circle](./triangles-inscribing-in-circle.jpg)

Say n is the amount of triangles.
Then, sum of the areas of the triangles is
![\frac 1 2 \: n \: r^2 \: sin \frac {2 \pi} {n}](./area-of-triangles-in-circle.svg)


When n converges to infinity, it will be the area of the circle.
In mathematical expression, it is
![\lim\_{n \to \infty }\frac 1 2 \: n \: r^2 \: sin \frac {2 \pi} {n}](./lim-area-of-triangles-in-circle.svg)

Since they're same,
![\pi r^2 = \lim\_{n \to \infty }\frac 1 2 \: n \: r^2 \: sin \frac {2 \pi} {n}](./area-of-circle-same-as-lim-area-of-triangles-in-circle.svg)

And finally,
![\pi = \lim\_{n \to \infty }\frac 1 2 \: n \: sin \frac {2 \pi} {n}](./value-of-pi.svg)

