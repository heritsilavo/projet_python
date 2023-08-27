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
    degres_liberte1 = int(saisir_nombre("Entrez les degrés de liberté du numérateur (d1) : "))
    degres_liberte2 = int(saisir_nombre("Entrez les degrés de liberté du dénominateur (d2) : "))
    f = saisir_nombre("Entrez la valeur de la statistique F : ")
    
    probabilite = 1 - math.betainc(degres_liberte1 / 2, degres_liberte2 / 2, degres_liberte1 / (degres_liberte1 + degres_liberte2 * f))
    print(f"La probabilité P(F ≥ {f}) est : {probabilite}")

def calcul_valeur_critique():
    degres_liberte1 = int(saisir_nombre("Entrez les degrés de liberté du numérateur (d1) : "))
    degres_liberte2 = int(saisir_nombre("Entrez les degrés de liberté du dénominateur (d2) : "))
    probabilite = saisir_nombre("Entrez la probabilité : ")
    
    valeur_critique = math.betaincinv(degres_liberte1 / 2, degres_liberte2 / 2, 1 - probabilite)
    valeur_critique = (degres_liberte2 * valeur_critique) / (degres_liberte1 * (1 - valeur_critique))
    print(f"La valeur critique correspondante à P(F ≥ {valeur_critique}) est : {valeur_critique}")

def calcul_moyenne():
    degres_liberte1 = int(saisir_nombre("Entrez les degrés de liberté du numérateur (d1) : "))
    degres_liberte2 = int(saisir_nombre("Entrez les degrés de liberté du dénominateur (d2) : "))
    moyenne = degres_liberte2 / (degres_liberte2 - 2)
    print(f"La moyenne de la distribution F est : {moyenne}")

def calcul_variance():
    degres_liberte1 = int(saisir_nombre("Entrez les degrés de liberté du numérateur (d1) : "))
    degres_liberte2 = int(saisir_nombre("Entrez les degrés de liberté du dénominateur (d2) : "))
    if degres_liberte2 > 4:
        variance = (2 * (degres_liberte2 ** 2) * (degres_liberte1 + degres_liberte2 - 2)) / (degres_liberte1 * (degres_liberte2 - 2) ** 2 * (degres_liberte2 - 4))
        print(f"La variance de la distribution F est : {variance}")
    else:
        print("La variance n'est pas définie pour d2 ≤ 4.")

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
