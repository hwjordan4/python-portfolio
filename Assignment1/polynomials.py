__author__ = 'Harrison Jordan'


def eval(x, poly):
    power = 0
    total = 0
    for c in poly:
        total += c * pow(x, power)
        power += 1
    return total

def bisection(a, b, poly, tolerance):

   if eval(a, poly) <= 0:
        if eval(b, poly) >= 0:
            while abs(a-b) > tolerance:
                    mid = (a+b)/2
                    if(eval(mid, poly) < 0):
                        a = mid
                    else:
                        b = mid
            return mid


        else:
            print("poly(b) not greater than 0")
   else:
       print("poly(a) not less than 0")



