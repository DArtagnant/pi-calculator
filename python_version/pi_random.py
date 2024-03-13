from random import random

def pi_random(reps):
    n = 0
    for i in range(reps):
        x = random()
        y = random()
        if y <= (1 - x**2) ** 0.5:
            n += 1
    return 4 * n / (i + 1)

if __name__ == "__main__":
    repetitions = int(input("How many repetitions? "))
    print(pi_random(repetitions))