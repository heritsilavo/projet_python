def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def hypergeometric_pmf(sample_successes, population_size, num_success_states, sample_size):
    numerateur = factorial(num_success_states) * factorial(population_size - num_success_states) * factorial(sample_size) * factorial(population_size - sample_size)
    denominateur = factorial(sample_successes) * factorial(sample_size - sample_successes) * factorial(population_size)
    probability = numerateur / denominateur
    return probability

# Paramètres de la distribution
population_size = int(input("Entrez la taille de la population (N) : "))
num_success_states = int(input("Entrez le nombre de succès dans la population (K) : "))
sample_size = int(input("Entrez la taille de l'échantillon (n) : "))
sample_successes = int(input("Entrez le nombre de succès souhaité dans l'échantillon (k) : "))

# Calcul de la probabilité
prob = hypergeometric_pmf(sample_successes, population_size, num_success_states, sample_size)
print("Probabilité :", prob)