from decimal import Decimal, getcontext
from math import factorial

def pi_chudnovsky(reps):
    approx = Decimal(0)
    for k in range(0, reps+1):
        approx += ( Decimal((-1)**k)*factorial(6*k)*(13591409 + 545140134*k) /
                   Decimal(factorial(3*k)*(factorial(k)**3)*(640320**((3*k)+(Decimal(3)/2)))) )
    return 1 / (12 * approx)

if __name__ == "__main__":
    getcontext().prec = 100
    repetitions = int(input("How many repetitions? "))
    print(pi_chudnovsky(repetitions))