import random as rd
def verif(prop,prixObjet):
    if 1 >= prop >= 10:
        print("Proposition non valide. Saisir un chiffre entre 1 et 10")
        return 'Continuer'
    if prop == prixObjet:
        print("Bonne réponse")
        return "Bonne réponse"

    elif prop < prixObjet:
        print("Prix trop petit")
    else:
        print("Prix trop grand")
    return "Continuer"
def juste_prix():
    print("Trouver le prix de l'objet situé entre 1 et 10 euros")
    prixObjet = rd.randint(1,10)
    print("Prix de l'objet :",prixObjet)

    prop=int(input("Saisir une proposition : "))

    for i in range(5):
        try:
            prop = int(input("Saisir une proposition : "))
        except ValueError:
            print("Erreur. Entrez un entier")
            continue

        if verif(prop, prixObjet) == "Bonne réponse":
           break
    print("Fin du jeu")
if __name__=="__main__":
    juste_prix()