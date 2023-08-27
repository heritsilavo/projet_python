import random

def loi_geometrique(probabilite_succes):
    essais = 1
    while random.random() > probabilite_succes:
        essais += 1
    return essais

probabilite_succes = 0.3
taille_echantillon = 10

echantillon = [loi_geometrique(probabilite_succes) for _ in range(taille_echantillon)]
print(echantillon)