print("hello world!")
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

