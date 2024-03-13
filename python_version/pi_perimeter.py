from decimal import Decimal, getcontext

def pi_perimeter(reps):
    rayon = Decimal(1)
    a = Decimal(1)
    b = Decimal(1)
    for i in range(reps):
        sq = (a**2 + b**2).sqrt()
        p = 2**(i + 2) * sq
        approx = p / (2 * rayon)
        a = rayon - (rayon**2 - b**2).sqrt()
        b = (a**2 + b**2).sqrt() / 2
    return approx

if __name__ == "__main__":
    getcontext().prec = 100
    repetitions = int(input("How many repetitions? "))
    print(pi_perimeter(repetitions))
