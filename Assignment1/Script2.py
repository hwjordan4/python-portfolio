__author__ = 'Harrison Jordan'

from polynomials import bisection, eval

toler = 1e-12
a = 1
b = 3
poly = [10, -13, -14, 15]

bi = bisection(a, b, poly, toler)
evaluate = eval(bi, poly)

print("Root of Polynomial: ", bi)
print("Evaluation: ", evaluate)