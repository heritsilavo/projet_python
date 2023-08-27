import math

def binomial_probability(n, k, p):
    if 0 <= p <= 1:
        probabilite = math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
        print(f"La probabilité P(X = {k}) est : {probabilite}")
    else:
        print("La probabilité p doit être comprise entre 0 et 1.")

n = int(input("Entrez le nombre d'essais (n) : "))  # Nombre d'essais
p = float(input("Entrez la probabilitée de succes (p) : "))  # Probabilité de succès dans chaque essai
k = int(input("Entrez le nombre de success (k) : "))   # Nombre de succès

probability = binomial_probability(n, k, p)