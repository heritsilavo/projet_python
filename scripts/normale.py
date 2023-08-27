import math

def demande_action():
    print("Que souhaitez-vous faire ?")
    print("1. Calculer une probabilité")
    print("2. Calculer une espérance")
    print("3. Calculer une variance")
    print("4. Calculer un écart type")
    
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
    moyenne = saisir_nombre("Entrez la moyenne (μ) : ")
    ecart_type = saisir_nombre("Entrez l'écart type (σ) : ")
    x1 = saisir_nombre("Entrez la borne inférieure (x1) : ")
    x2 = saisir_nombre("Entrez la borne supérieure (x2) : ")
    
    z1 = (x1 - moyenne) / ecart_type
    z2 = (x2 - moyenne) / ecart_type
    
    probabilite = (math.erf(z2 / math.sqrt(2)) - math.erf(z1 / math.sqrt(2))) / 2
    print(f"La probabilité P({x1} ≤ X ≤ {x2}) est : {probabilite}")

def calcul_esperance():
    moyenne = saisir_nombre("Entrez la moyenne (μ) : ")
    print(f"L'espérance de la distribution est : {moyenne}")

def calcul_variance():
    ecart_type = saisir_nombre("Entrez l'écart type (σ) : ")
    variance = ecart_type ** 2
    print(f"La variance de la distribution est : {variance}")

def calcul_ecart_type():
    variance = saisir_nombre("Entrez la variance : ")
    ecart_type = math.sqrt(variance)
    print(f"L'écart type de la distribution est : {ecart_type}")

def main():
    while True:
        action = demande_action()
        
        if action == '1':
            calcul_probabilite()
        elif action == '2':
            calcul_esperance()
        elif action == '3':
            calcul_variance()
        elif action == '4':
            calcul_ecart_type()
        else:
            print("Option invalide. Veuillez choisir une option valide (1/2/3/4).")
        
        continuer = input("Voulez-vous effectuer une autre opération ? (oui/non) : ")
        if continuer.lower() != 'oui':
            break

if __name__ == "__main__":
    main()
