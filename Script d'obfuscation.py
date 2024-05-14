import os
import subprocess


def obfuscate_directory(source_dir, output_dir):
    # Vérifier si le répertoire source existe
    if not os.path.exists(source_dir):
        print(f"Le répertoire source spécifié n'existe pas : {source_dir}")
        return

    # Créer le répertoire de sortie s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)

    # Compteur pour suivre le nombre de fichiers traités
    file_count = 0

    # Obfusquer chaque fichier Python dans le répertoire source
    for filename in os.listdir(source_dir):
        if filename.endswith('.py'):
            file_count += 1
            source_file = os.path.join(source_dir, filename)
            output_file = os.path.join(output_dir, filename)
            
            # Appel de PyArmor via la ligne de commande
            result = subprocess.run(['pyarmor', 'gen', '-O', output_file, source_file], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Le fichier {filename} a été obfusqué et sauvegardé dans {output_file}")
            else:
                print(f"Erreur lors de l'obfuscation de {filename}: {result.stderr}")

    if file_count == 0:
        print("Aucun fichier Python (.py) trouvé dans le répertoire source.")

if __name__ == "__main__":
    # Définissez ici les chemins vers vos répertoires
    source_directory = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/'
    output_directory = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/Script_obfusque/'
    
    # Lancer le processus d'obfuscation
    obfuscate_directory(source_directory, output_directory)
