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
    a = saisir_nombre("Entrez la borne inférieure (a) : ")
    b = saisir_nombre("Entrez la borne supérieure (b) : ")
    x = saisir_nombre("Entrez la valeur de x : ")
    
    if a <= x <= b:
        probabilite = 1 / (b - a)
        print(f"La probabilité P({a} ≤ X ≤ {b}) est : {probabilite}")
    else:
        print("La valeur x doit être comprise entre a et b.")

def calcul_esperance():
    a = saisir_nombre("Entrez la borne inférieure (a) : ")
    b = saisir_nombre("Entrez la borne supérieure (b) : ")
    
    esperance = (a + b) / 2
    print(f"L'espérance de la distribution est : {esperance}")

def calcul_variance():
    a = saisir_nombre("Entrez la borne inférieure (a) : ")
    b = saisir_nombre("Entrez la borne supérieure (b) : ")
    
    variance = ((b - a) ** 2) / 12
    print(f"La variance de la distribution est : {variance}")

def calcul_ecart_type():
    a = saisir_nombre("Entrez la borne inférieure (a) : ")
    b = saisir_nombre("Entrez la borne supérieure (b) : ")
    
    ecart_type = math.sqrt(((b - a) ** 2) / 12)
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
