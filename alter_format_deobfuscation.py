import sys
import os

def deobfuscate_file(source_dir, output_dir):
    # Assurez-vous que le répertoire de sortie existe ou le crée s'il n'existe pas
    os.makedirs(output_dir, exist_ok=True)
    
    # Parcourir tous les fichiers dans le répertoire source
    for filename in os.listdir(source_dir):
        # Vérifier si le fichier est un fichier Python
        if filename.endswith('.py'):
            source_file = os.path.join(source_dir, filename)
            output_file = os.path.join(output_dir, filename)
            
            # Lire le contenu du fichier obfusqué
            with open(source_file, 'r') as f:
                obfuscated_code = f.read()
    
            # Convertir chaque paire hexadécimale en caractère ASCII
            deobfuscated_code = ''.join([chr(int(obfuscated_code[i:i+2], 16)) for i in range(0, len(obfuscated_code), 2)])
    
            # Écrire le code déobfusqué dans le fichier de sortie
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(deobfuscated_code)

    
            print(f"Le fichier {filename} a été déobfusqué et sauvegardé dans {output_file}")

# Définir les répertoires source et de sortie
source_dir = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/Script_obfusque'
output_dir = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/Script_desobfusque' 

# Appeler la fonction de déobfuscation
deobfuscate_file(source_dir, output_dir)
