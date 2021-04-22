import mpmath as mp
import decimal
import math
import random

method = int(input('Method(1 ~ 2): '))
precision = int(input('Precision: '))

if method == 1:
    mp.dps = 40

    n = 1
    while True:
        try:
            print(f'\rn = {n}, {mp.mpf(n) / mp.mpf(2) * mp.sin(2 * mp.pi / mp.mpf(n))}', end='')

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

            print(f'\rN = {squareDots}, M = {circleDots}, ', end='')
            print(4 * circleDots / decimal.Decimal(squareDots), end='')

        except KeyboardInterrupt:
            break

print()

