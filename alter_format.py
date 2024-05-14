import os

def obfuscate_script(source_dir, output_dir):

    os.makedirs(output_dir, exist_ok=True)
    
    # Obfusquer chaque fichier Python dans le répertoire source
    for filename in os.listdir(source_dir):
        if filename.endswith('.py'):
            source_file = os.path.join(source_dir, filename)
            output_file = os.path.join(output_dir, filename)
            
            # Lire le contenu du fichier source
            with open(source_file, 'r') as f:
                code = f.read()
            
            # Convertir chaque caractère du code en hexadécimal
            obfuscated_code = ''.join([hex(ord(char))[2:] for char in code])
            
            # Écrire le code obfusqué dans le fichier de sortie
            with open(output_file, 'w') as f:
                f.write(obfuscated_code)
            
            print(f"Le fichier {filename} a été obfusqué et sauvegardé dans {output_file}")

# Définir les répertoires source et de sortie
source_dir = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/'
output_dir = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/Script_obfusque/'


# Appeler la fonction d'obfuscation
obfuscate_script(source_dir, output_dir)