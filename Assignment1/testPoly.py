__author__ = 'Harrison Jordan'

from polynomials import bisection, eval

toler = 1e-14

poly1 = [-945, 1689, -950, 230, -25, 1]
# roots are 1, 3, 5, 7, 9
x1 = bisection(0, 2, poly1, 1e-15)
# print root and evaluate the polynomial
print(x1, eval(x1,poly1))
x2 = bisection(4,2,poly1,toler)
print(x2, eval(x2,poly1))
x3 = bisection(4,6,poly1, toler)
print(x3, eval(x3,poly1))
x4 = bisection(8,6,poly1, toler)
print(x4, eval(x4,poly1))
x5 = bisection(8,100,poly1, toler)
print(x5, eval(x5,poly1))
# compare the roots to the expected values
print(x1-1, x2-3, x3-5, x4-7, x5-9)

print(eval(1, [1,2,2]))