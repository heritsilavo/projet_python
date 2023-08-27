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
    t = saisir_nombre("Entrez la valeur de t : ")
    
    probabilite = 1 - (1 + math.erf(t / math.sqrt(2))) / 2
    print(f"La probabilité P(T ≥ {t}) est : {probabilite}")

def calcul_valeur_critique():
    degres_liberte = int(saisir_nombre("Entrez les degrés de liberté : "))
    probabilite = saisir_nombre("Entrez la probabilité : ")
    
    valeur_critique = math.erfinv(1 - 2 * probabilite) * math.sqrt(2)
    print(f"La valeur critique correspondante à P(T ≥ {valeur_critique}) est : {valeur_critique}")

def calcul_moyenne():
    degres_liberte = int(saisir_nombre("Entrez les degrés de liberté : "))
    moyenne = 0
    print(f"La moyenne de la distribution t est : {moyenne}")

def calcul_variance():
    degres_liberte = int(saisir_nombre("Entrez les degrés de liberté : "))
    
    if degres_liberte > 2:
        variance = degres_liberte / (degres_liberte - 2)
        print(f"La variance de la distribution t est : {variance}")
    else:
        print("La variance n'est pas définie pour d degré de liberté ≤ 2.")

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
