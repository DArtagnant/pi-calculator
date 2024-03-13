from decimal import Decimal, getcontext

def pi_nilakantha(reps):
    approx = Decimal(3)
    sign = 1
    for n in range(2, (2 * reps) + 1, 2):
        approx += sign * 4 / Decimal(n * (n + 1) * (n + 2))
        sign *= -1
    return approx

if __name__ == "__main__":
    getcontext().prec = 100
    repetitions = int(input("How many repetitions? "))
    print(pi_nilakantha(repetitions))