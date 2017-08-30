import sympy as mp
mp.dps = 15; mp.pretty = True
nsum(lambda n: 1/fac(n), [0, inf])
nsum(lambda n: 1/n**2, [1, inf])

