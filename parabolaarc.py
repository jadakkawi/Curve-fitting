u1 = 28.375
w1 = 1.345
s1 = 0
u2 = 48.75
w2 = 0.35
s2 = 0
R2 = 10

import math
import numpy as np

alfa = u2
beta = y2 + R2

possibleues = [u2 - R2, u2]


def drange(start, stop, step):
    steps = []
    r = start
    while r < stop:
        steps.append(r)
        r += step
    return steps

def w_circle(u):
    return beta - math.sqrt((R2**2) - (u - alfa))


# def w_parabola(u):
# #     return a * (u ** 2) + b * u + c
deltas = []

for u in drange(possibleues[0],possibleues[1], 1):

    uu = np.array([u1**2,u1,1],[u**2, u, 1], [2*u1, 1, 0 ])
    warc = w_circle(u)
    ww = np.array([w1, warc, s1])
    a = list(np.linalg.solve(uu, ww))[0]
    b = list(np.linalg.solve(uu, ww))[1]
    sp_from_parabola = 2 * a * u + b
    sp_from_arc = (alfa - u) / (warc - beta)
    delta = abs(sp_from_arc - sp_from_parabola)
    deltas.append([delta,u])

print(deltas)
