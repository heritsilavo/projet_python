import random

def bernoulli(p, n):
    successes = 0
    for _ in range(n):
        if random.random() < p:
            successes += 1
    return successes

p = float(input("Entrez la probabilitée de succes (p) : "))
n = int(input("Entrez le nombre d'essais (n) : "))

successes = bernoulli(p, n)
print(f"Nombre de succès sur {n} essais : {successes}")