import math

n = 1

while True:
    try:
        print(f'\rn = {n}, {n / 2 * math.sin(2 * math.pi / n)}', end='')

        n += 1

    except KeyboardInterrupt:
        break

print()

