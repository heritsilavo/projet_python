import math

def demande_action():
    print("Que souhaitez-vous faire ?")
    print("1. Calculer une probabilité")
    print("2. Calculer une valeur critique")
    print("3. Calculer une moyenne")
    print("4. Calculer une variance")
    
    choix = input("Choisissez une option (1/2/3/4) : ")
    return choix

def saisir_nombre(message):
    while True:
        try:
            valeur = float(input(message))
            return valeur
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def calcul_probabilite():
    degres_liberte = int(saisir_nombre("Entrez les degrés de liberté : "))
    x2 = saisir_nombre("Entrez la valeur de chi-2 (χ²) : ")
    
    probabilite = 1 - math.gamma(degres_liberte / 2, scale=2).cdf(x2 / 2)
    print(f"La probabilité P(χ² ≥ {x2}) est : {probabilite}")

def calcul_valeur_critique():
    degres_liberte = int(saisir_nombre("Entrez les degrés de liberté : "))
    probabilite = saisir_nombre("Entrez la probabilité : ")
    
    valeur_critique = 2 * math.gamma(degres_liberte / 2, scale=2).ppf(1 - probabilite)
    print(f"La valeur critique correspondante à P(χ² ≥ {valeur_critique}) est : {valeur_critique}")

def calcul_moyenne():
    degres_liberte = int(saisir_nombre("Entrez les degrés de liberté : "))
    moyenne = degres_liberte
    print(f"La moyenne de la distribution χ² est : {moyenne}")

def calcul_variance():
    degres_liberte = int(saisir_nombre("Entrez les degrés de liberté : "))
    variance = 2 * degres_liberte
    print(f"La variance de la distribution χ² est : {variance}")

def main():
    while True:
        action = demande_action()
        
        if action == '1':
            calcul_probabilite()
        elif action == '2':
            calcul_valeur_critique()
        elif action == '3':
            calcul_moyenne()
        elif action == '4':
            calcul_variance()
        else:
            print("Option invalide. Veuillez choisir une option valide (1/2/3/4).")
        
        continuer = input("Voulez-vous effectuer une autre opération ? (oui/non) : ")
        if continuer.lower() != 'oui':
            break

if __name__ == "__main__":
    main()
