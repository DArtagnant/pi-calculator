from decimal import Decimal, getcontext

#Time Complexity: O(N * logN * loglogN) N = reps
#Auxilary Space : O(1)

def pi_nilakantha(reps):
    approx = Decimal(3.0)
    sign = 1
    for n in range(2, (2 * reps) + 1, 2):
        approx += 4 / Decimal(n * (n + 1) * (n + 2) * sign)
        sign *= -1
    return approx

if __name__ == "__main__":
    getcontext().prec = 100
    repetitions = int(input("How many repetitions? "))
    print(pi_nilakantha(repetitions))