import decimal
import math
import random

method = int(input('Method(1 ~ 3): '))
precision = int(input('Precision: '))
actualPi = decimal.Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'[:precision + 2])

decimal.getcontext().prec = precision

def calculateError(acceptedValue, experimentalValue):
    return abs(acceptedValue - experimentalValue) / acceptedValue * 100

if method == 1:
    # since Bhaskara I's sine approximation formula is only accurate in range from 0 to 180,
    # we should start n with 2 to make the first degree to 180 deg
    n = 2

    while True:
        try:
            degree = decimal.Decimal(360) / n
            # Bhaskara I's sine approximation formula
            sinValue = 4 * degree * (180 - degree) / (40500 - degree * (180 - degree))
            calculatedPi = decimal.Decimal(sinValue * n / 2)

            print(f'\rn = {n}, sin = {sinValue}, π = {calculatedPi}, e = {calculateError(actualPi, calculatedPi)}%', end='')

            n += 1

        except KeyboardInterrupt:
            break

elif method == 2:
    circleDots = 0
    squareDots = 0

    while True:
        try:
            x = random.randint(0, 10000)
            y = random.randint(0, 10000)

            # if the dot is in the circle
            if x ** 2 + y ** 2 <= 100000000:
                circleDots += 1

            squareDots += 1

            calculatedPi = 4 * circleDots / decimal.Decimal(squareDots)

            print(f'\rN = {squareDots}, M = {circleDots}, π = {calculatedPi}, e = {calculateError(actualPi, calculatedPi)}%', end='')

        except KeyboardInterrupt:
            break

        except ZeroDivisionError:
            continue

elif method == 3:
    zeta = decimal.Decimal(0)
    n = 1

    while True:
        try:
            zeta += (1 / decimal.Decimal(n ** 2))
            calculatedPi = (6 * zeta).sqrt()

            print(f'\rn = {n}, ζ(2) = {zeta}, π = {calculatedPi}, e = {calculateError(actualPi, calculatedPi)}%', end='')

            n += 1

        except KeyboardInterrupt:
            break
print()

