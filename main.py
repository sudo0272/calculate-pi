import mpmath as mp
import decimal
import math
import random

method = int(input('Method(1 ~ 3): '))
precision = int(input('Precision: '))
actualPi = decimal.Decimal('3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679821480865132823066470938446095505822317253594081284811174502841027019385211055596446229489549303819644288109756659334461284756482337867831652712019091456485669234603486104543266482133936072602491412737245870066063155881748815209209628292540917153643678925903600113305305488204665213841469519415116094330572703657595919530921861173819326117931051185480744623799627495673518857527248912279381830119491298336733624406566430860213949463952247371907021798609437027705392171762931767523846748184676694051320005681271452635608277857713427577896091736371787214684409012249534301465495853710507922796892589235420199561121290219608640344181598136297747713099605187072113499999983729780499510597317328160963185950244594553469083026425223082533446850352619311881710100031378387528865875332083814206171776691473035982534904287554687311595628638823537875937519577818577805321712268066130019278766111959092164201989'[:precision + 2])

if method == 1:
    mp.dps = 40

    n = 1
    while True:
        try:
            calculatedPi = decimal.Decimal(str(mp.mpf(n) / mp.mpf(2) * mp.sin(2 * mp.pi / mp.mpf(n))))

            print(f'\rn = {n}, pi = {calculatedPi}', end='')
            print(f', e = ', end='')
            print(abs(actualPi - calculatedPi) / actualPi * 100, end='%')

            n += 1

        except KeyboardInterrupt:
            break

elif method == 2:
    decimal.getcontext().prec = precision

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

            print(f'\rN = {squareDots}, M = {circleDots}, pi = {calculatedPi}', end='')
            print(f', e = ', end='')
            print(abs(actualPi - calculatedPi) / actualPi * 100, end='%')

        except KeyboardInterrupt:
            break

        except ZeroDivisionError:
            continue

elif method == 3:
    decimal.getcontext().prec = precision

    zeta = decimal.Decimal(0)
    n = 1

    while True:
        try:
            zeta += (1 / decimal.Decimal(n ** 2))
            calculatedPi = (6 * zeta).sqrt()

            print(f'\rn = {n}, zeta(2) = {zeta}, pi = {calculatedPi}, e = {abs(actualPi - calculatedPi) / actualPi * 100}%', end='')

            n += 1

        except KeyboardInterrupt:
            break
print()

