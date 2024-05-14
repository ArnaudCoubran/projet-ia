def ajouter_code_inutile(fichier_entree, fichier_sortie):
    # Lire le contenu du fichier d'entrée
    with open(fichier_entree, "r") as f:
        contenu = f.read()

    # Ajouter du code inutile à la fin
    code_inutile = """
def fc_in():
    print("!!!!")

def boucle_complexe():
    for i in range(10):
        if i % 2 == 0:
            print(f"Nombre pair : {i}")
        else:
            print(f"Nombre impair : {i}")
            
   

def boucle_complexe():
    for i in range(10):
        if i % 2 == 0:
            print(f"Nombre pair : {i}")
        else:
            print(f"Nombre impair : {i}")

class ClasseSecrete:
    def __init__(self):
        self.secret = " !"



def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def tri_bulle(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

if __name__ == "__main__":
    # Exemple d'utilisation
    ma_liste = [5, 2, 8, 1, 3]
    tri_bulle(ma_liste)


class ClasseSecrete:
    def __init__(self):
        self.secret = "!!!"

    def afficher_secret(self):
        print(self.secret)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

"""

    contenu += code_inutile

    # Écrire le contenu dans le fichier de sortie
    with open(fichier_sortie, "w") as f:
        f.write(contenu)

# Utilisation de la fonction
fichier_entree = "exemple.py"
fichier_sortie = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/Script_obfusque/fichier_obfusque.py'
ajouter_code_inutile(fichier_entree, fichier_sortie)
print(f"Le fichier obfusqué a été enregistré sous {fichier_sortie}")
