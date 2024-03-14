from decimal import Decimal, getcontext
from math import factorial

def pi_newton(reps):
    approx = Decimal(0)
    for k in range(0, reps+1):
        approx += ( (Decimal((2)**k) * (factorial(k)**2)) /
                   Decimal(factorial(2 * k + 1)))
    return 2 * approx

if __name__ == "__main__":
    getcontext().prec = 100
    repetitions = int(input("How many repetitions? "))
    print(pi_newton(repetitions))