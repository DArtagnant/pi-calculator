from decimal import Decimal, getcontext

def pi_nilakantha(reps):
    result = Decimal(3.0)
    op = 1
    n = 2
    for n in range(2, (2 * reps) + 1, 2):
        result += 4 / Decimal(n * (n + 1) * ( n + 2) * op)
        op *= -1
    return result

if __name__ == "__main__":
    getcontext().prec = 100
    repetitions = int(input("How many repetitions? "))
    print(pi_nilakantha(repetitions))