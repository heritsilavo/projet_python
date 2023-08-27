import math

def calcul_probabilite():
    p = float(input("Entrez la probabilité de succès (p) : "))
    k = int(input("Entrez le nombre de succès souhaité (k) : "))
    n = int(input("Entrez le nombre total d'épreuves (n) : "))
    
    if 0 <= p <= 1:
        probabilite = math.comb(n - 1, k - 1) * (p ** k) * ((1 - p) ** (n - k))
        print(f"La probabilité P(X = {k}) avec {n} épreuves est : {probabilite}")
    else:
        print("La probabilité p doit être comprise entre 0 et 1.")

def main():
    while True:
        calcul_probabilite()
        
        continuer = input("Voulez-vous effectuer une autre opération ? (oui/non) : ")
        if continuer.lower() != 'oui':
            break

if __name__ == "__main__":
    main()