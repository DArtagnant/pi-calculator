

def pi_perimeter(reps):
    rayon = 1
    a = 1
    b = 1
    for i in range(reps):
        sq = (a**2 + b**2) ** 0.5
        p = 2**(i + 2) * sq
        pitruc = p / (2 * rayon)
        a = rayon - (rayon**2 - b**2) ** 0.5
        b = (a**2 + b**2)**0.5 / 2
    return pitruc

if __name__ == "__main__":
    repetitions = int(input("How many repetitions? "))
    print(pi_perimeter(repetitions))
