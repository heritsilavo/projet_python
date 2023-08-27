'''
import math

def premierDeg(a, b):
    if a==0:
       if b==0:
        print("Solution infini")
       else: 
        print("solution vide")
    else:
        sol=-b/a
        print("x=",sol)

def secondDeg(a,b,c):
    if a==0:
        print("a==0 donc equation premier degree")
        premierDeg(b,c)
    else:
        delta=(b*b)-(4*a*c)
        if delta<0:
            print("solution introuvable")
        elif delta==0:
            x1=(-b-math.sqrt(delta))/(2*a)
            print("une seule solution:",x1)
        else:
            x1=(-b-math.sqrt(delta))/(2*a)
            x2=(-b+math.sqrt(delta))/(2*a)
            print("x1=",x1)
            print("x2=",x2)


coeffValide=False
valC=""
while not coeffValide:
    try:
        valC=input("Entrer A:")
        A=int(valC)
        valC=input("Entrer B:")
        B=int(valC)
        valC=input("Entrer C:")
        C=int(valC)
        coeffValide=True
        secondDeg(A,B,C)
    except:
        coeffValide=False
        print(valC," n'est pas un nombre\n")

'''
'''
POLYMORPHISME
def f(saveur,taille="normal")

EXO:
    1) ecrire une fonction qui affiche la table de multiplication d'une base donneé
    2) ecrire une fonction qui prend en parametre une serie(tableau)
       retourne la moyenne et l'ecart type
    3)ecrire une fonction binome qui prend en parametre 3 arguments nombre (nombre d'epreuve,proba de success, nombre de succes attendus)
      retourne la probabilite

FONCTION QUI RETOURNE PLUSIEUR VALEUR
***declaration
    def fonc(params...):
        ...
        return a,b

***appel
    x,y=fonc()
'''

'''
def tableMult(base,deb="",fin=""):
    if deb=="":
        deb=0
    if fin=="":
        fin=deb+10
    i=deb
    while i<=fin:
        print(base,"*",i,"=",(base*i))
        i=i+1
tableMult(6,3)
'''
import math
import statistics

# def creerTab(taille):
#     while taille>0:
#         taille=taille-1


def verifierParam(tab):
    val=True
    if type(tab)!=list: val=False
    else:
        for el in tab:
            if type(el)!=int and type(el)!=float:
                val=False
    print(val)
    return val

def stat(tab):
    if verifierParam(tab):
        moy=sum(tab)/len(tab)
        ecr=statistics.stdev(tab)
        return moy,ecr
    else:
        print("Ce n'est pas un tableau de nombre:",tab)
        return '',''


t=[1,2,3,5,2]
a=[2,4,"y",2]

Moyenne,Ecart=stat(a)

if Moyenne!='' and Ecart!='':
    print("Moyenne=",Moyenne)
    print("Ecart Type=",Ecart)
