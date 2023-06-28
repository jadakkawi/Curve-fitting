# import matplotlib.pyplot as plt
# import pprint
import math
import numpy as np


def d_range_inc(start, stop, step):
    steps = []
    r = start
    while r <= stop:
        steps.append(r)
        r += step
    return steps


def w_circle(x, _x_center, _y_center, r22, a):
    return _y_center + a * math.sqrt(math.pow(r22, 2) - math.pow(x - _x_center, 2))


def sp_from_arc(x, _x_center, y, _y_center):
    return (_x_center - x) / (y - _y_center)


def w_parabola(x, aa, bb, cc):
    return aa * math.pow(x, 2) + bb * x + cc


def sp_from_parabola(x, aa, bb):
    return 2 * aa * x + bb


def r_curvature_2nd_order(x, a, b):
    return 1 / ((2 * a) / (math.pow(1 + math.pow(2 * a * x + b, 2), 1.5)))


def w_s_from_str_line(_u1, _w1, _s1, _u2):
    _w2 = _w1 + (_s1/100) * (_u2 - _u1)
    _s2 = _s1
    return [_w2, _s2]


def straight_line(_u1, _w1, _s1, _u2, _out_nbr):

    _results = []
    for i in d_range_inc(_u1, _u2, (_u2 - _u1) / _out_nbr):
        _results.append([i, round(w_s_from_str_line(_u1, _w1, _s1, i)[0], 3),
                         w_s_from_str_line(_u1, _w1, _s1, i)[1], 'STRAIGHT'])
    return _results


def parabola_arc(_u1, _w1, _s1, _u2, _w2, _s2, _r2, _out_nbr):

    x_center = _u2        # Should consider getting center for any slope not just zero.
    y_center = _w2 + _r2  # s22 to be used for later
    if _u1 < _u2:
        a = - 1
    else:
        a = 1
    possible_ues = [min([_u2 + a * _r2, _u2], max(_u2 + a * _r2, _u2))]  # Possible ues for any slope

    pool_of_u = []
    deltas = []
    abc = []

    for u in d_range_inc(possible_ues[0] + 0.1, possible_ues[1], 0.005):    # Should consider giving only fitting ranges
                                                                            # Not all possible range
        uu = np.array([[math.pow(_u1, 2), _u1, 1], [math.pow(u, 2), u, 1], [2 * _u1, 1, 0]])
        w_on_arc = w_circle(u, x_center, y_center, _r2)
        ww = np.array([_w1, w_on_arc, _s1 / 100])
        solution = np.linalg.solve(uu, ww)
        a = list(solution)[0]
        b = list(solution)[1]
        c = list(solution)[2]
        check = np.allclose(np.dot(uu, solution), ww)
        delta = abs(sp_from_arc(u, x_center, w_on_arc, y_center) - sp_from_parabola(u, a, b))
        deltas.append(delta)
        pool_of_u.append(u)
        abc.append(list(solution))

        # if _w2 < w_parabola(u, a, b, c) < _w1:
        #     print(uu)
        #     print(ww)
        #     print("u: {}".format(round(u, 3)))
        #     print("w(u) from bola: {}".format(round(w_parabola(u, a, b, c), 3)))
        #     print("w(u1) from bola: {}".format(round(w_parabola(_u1, a, b, c), 3)))
        #     print("w(u) from circle: {}".format(round(w_on_arc, 3)))
        #     print("[a, b, c] : {}".format([a, b, c]))
        #     print(check)
        #     print("\n")
        #     t = np.arange(_u1, u, 0.2)
        #     # t2 = np.arange(_u2 - _r2 + 0.1, _u2, 0.2)
        #     # ft = np.array([y_center - math.sqrt(math.pow(_r2, 2) - (x**2 - x_center)) for x in list(t)])
        #     plt.plot(t, a*t**2 + b*t + c)  # , 'r--', t2, ft, 'bs')
        #     plt.show()
        # pprint.pprint(deltas)

    up = pool_of_u[deltas.index(min(deltas))]
    abc_p = abc[deltas.index(min(deltas))]

    # print(up)
    # print(w_circle(up, x_center, y_center, _r2))
    # print(w_parabola(up, abc_p[0], abc_p[1], abc_p[2]))

    results = []
    for i in d_range_inc(_u1, _u2, (_u2 - _u1) / _out_nbr):
        if i < up:
            results.append([round(i, 3), round(w_parabola(i, abc_p[0], abc_p[1], abc_p[2]), 3),
                            round(sp_from_parabola(i, abc_p[0], abc_p[1]) * 100, 4),
                            round(r_curvature_2nd_order(i, abc_p[0], abc_p[1]), 3)])
        else:
            results.append([round(i, 3), round(w_circle(i, x_center, y_center, _r2), 3),
                            round(sp_from_arc(i, x_center, w_circle(i, x_center, y_center, _r2), y_center) * 100, 4),
                            _r2])

    # pprint.pprint(results)
    return results



