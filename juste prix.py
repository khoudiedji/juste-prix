import random as rd
print("Trouver le prix de l'objet situé entre 1 et 10 euros")
prixObjet = rd.randint(1,10)
print("Prix de l'objet :",prixObjet)
tentatives =5
prop=int(input("Saisir une proposition : "))

if 1>=prop>=10:
    print("Proposition non valide. Saisir un chiffre entre 1 et 10")
    prop = int(input("Saisir une proposition :\n"))

if prop == prixObjet:
    print("Bonne réponse")
elif prop < prixObjet:
    print("Prix trop petit")
else:
    prop > prixObjet
    print("Prix trop grand")
