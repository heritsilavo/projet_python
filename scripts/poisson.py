def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def poisson(k, lambd):
    return (lambd ** k) * math.exp(-lambd) / factorial(k)

import math

lambd = float(input("saisir la valeure de lambda: "))
k = int(input("saisir la valeure de 'k': "))

prob = poisson(k, lambd)
print(f"La probabilité d'obtenir {k} événements est : {prob:.4f}")