from decimal import Decimal, getcontext
from math import factorial

def pi_ramanujan(reps):
    approx = Decimal(0)
    for k in range(0, reps+1):
        approx += ( factorial((Decimal((4)**k)) * (1103 + 26390 * k)) /
                   Decimal(factorial(k)))
    return Decimal(1) / (((2*(2**(Decimal(1)/2))) / 9801) * approx)

if __name__ == "__main__":
    getcontext().prec = 100
    repetitions = int(input("How many repetitions? "))
    print(pi_ramanujan(repetitions))