import math

limit = int(input('limit: '))
steps = int(input('steps: '))

for n in range(1, limit + 1, steps):
    print(f'n = {n}, {n / 2 * math.sin(2 * math.pi / n)}')

