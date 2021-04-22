# First method
The general equation to find the area of this circle below is \
![circle](./circle.jpg)\
![\pi r^2](./area-of-circle.svg)

And the general equation to find the area of this triangle below is\
![triangle](./triangle.jpg)\
![\frac 1 2 \:  a b \: sin C](./area-of-triangle.svg)

Say a and b both equal to r.

Say there're many triangles which inscribe in a circle and are exactly congruent just like this:\
![triangle inscribing in the circle](./triangles-inscribing-in-circle.jpg)\

Say n is the amount of triangles.\
Then, sum of the areas of the triangles is\
![\frac 1 2 \: n \: r^2 \: sin \frac {2 \pi} {n}](./area-of-triangles-in-circle.svg)


When n converges to infinity, it will be the area of the circle.\
In mathematical expression, it is\
![\lim\_{n \to \infty }\frac 1 2 \: n \: r^2 \: sin \frac {2 \pi} {n}](./lim-area-of-triangles-in-circle.svg)

Since they're same,\
![\pi r^2 = \lim\_{n \to \infty }\frac 1 2 \: n \: r^2 \: sin \frac {2 \pi} {n}](./area-of-circle-same-as-lim-area-of-triangles-in-circle.svg)

And finally,\
![\pi = \lim\_{n \to \infty }\frac 1 2 \: n \: sin \frac {2 \pi} {n}](./value-of-pi.svg)

However, the problem of this method is that we have to use pi anyway to calculate sin(2 * pi).\
You could say that then we can use sin(250 deg).\
But the problem is, we have to convert degree to radian to calculate value of sin.\
So I tried to present sin as different expressions but I couldn't. :(\

# Second method:
Say there's a circle is inscribing in a square.\
The radius of the circle is 1, so the side length of the square is 2.\
We're going to put many many dots on the square.\
Say N is the number of dots on the square and M is the number of dots on the circle.\
When we put enough dots, then N represents the area of the square and M represents the area of the circle.\
Then,\
![\frac {\pi \times 1 \times 1} {2 \times 2} = \frac M N](https://latex.codecogs.com/png.image?\dpi{110}%20\frac%20{\pi%20\times%201%20\times%201}%20{2%20\times%202}%20=%20\frac%20M%20N)
![\frac \pi 4 = \frac M N ](https://latex.codecogs.com/png.image?\dpi{110}%20\frac%20\pi%204%20=%20\frac%20M%20N)
Finally,\
![\pi = 4 \cdot \frac M N](https://latex.codecogs.com/png.image?\dpi{110}%20\pi%20=%204%20\cdot%20\frac%20M%20N)

