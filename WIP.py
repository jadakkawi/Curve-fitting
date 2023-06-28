from os import path, chdir
# import sys
# sys.path.append(path.dirname(path.abspath(__file__)))

import pprint
from geometric_functions import *
import openpyxl

chdir("/Users/apple/IdeaProjects/PT-DOS")
wb = openpyxl.load_workbook('INPUT WB.xlsx')

u_w_s_r = wb['UW COORDINATES']
u_w_s_r_dict = {}

for row in range(4, u_w_s_r.max_row):
    u1 = u_w_s_r['B' + str(row)].value
    w1 = u_w_s_r['C' + str(row)].value
    s1 = u_w_s_r['D' + str(row)].value
    r1 = u_w_s_r['F' + str(row)].value

    u2 = u_w_s_r['B' + str(row + 1)].value
    w2 = u_w_s_r['C' + str(row + 1)].value
    s2 = u_w_s_r['D' + str(row + 1)].value
    r2 = u_w_s_r['E' + str(row + 1)].value

    out_nbr = u_w_s_r['I' + str(row)].value

    if r1 == "STRAIGHT":
        if s1 is not None:
            output = straight_line(u1, w1, s1, u2, out_nbr)
        elif w2 is not None:
            s2 = (w2 - w1) / (u2 - u1)
            output = straight_line(u1, w1, s1, u2, out_nbr)
        elif s2 is not None:
            output = straight_line(u1, w1, s2, u2, out_nbr)
    elif r1 is None:
        if r2 is None:
            pass
        if r2 is not None:
            output = parabola_arc(u1, w1, s1, u2, w2, s2, r2, out_nbr)
    elif r1 is not None:
        if r2 is None:
            output = parabola_arc(u2, w2, s2, u1, w1, s1, r1, out_nbr)






#
# u1 = 0
# w1 = 1.13
# s1 = -10
# u2 = 1.5
# out_nbr = 1
# pprint.pprint(straight_line(u1, w1, s1, u2, out_nbr))
#
#
# u1 = 1.5
# w1 = (1.13 - 0.15)
# s1 = -10
# u2 = 8
# w2 = 0.35
# s2 = 0
# r2 = 10
# out_nbr = 6
# pprint.pprint(parabola_arc(u1, w1, s1, u2, w2, s2, r2, out_nbr))
#
#
# u1 = 28.375
# w1 = 1.345
# s1 = 0
# u2 = 48.75
# w2 = 0.35
# s2 = 0
# R2 = 10
# out_nbr = 20
# pprint.pprint(parabola_arc(u1, w1, s1, u2, w2, s2, r2, out_nbr))



