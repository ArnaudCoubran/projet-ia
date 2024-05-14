from cryptography.fernet import Fernet

def generate_key():
    # Générer une clé et la retourner
    key = Fernet.generate_key()
    return key

def encrypt_file(file_path, key):
    # Lire le contenu du fichier
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Créer un objet Fernet avec la clé fournie
    cipher_suite = Fernet(key)
    
    # Chiffrer les données
    encrypted_data = cipher_suite.encrypt(file_data)
    
    # Sauvegarder les données chiffrées dans un fichier
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)
    
    print(f'Fichier {file_path} chiffré et sauvegardé dans {file_path}.encrypted')

def decrypt_file(file_path, key):
    # Lire les données chiffrées du fichier
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Créer un objet Fernet avec la clé fournie
    cipher_suite = Fernet(key)
    
    # Déchiffrer les données
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    # Sauvegarder les données déchiffrées dans un fichier
    decrypted_file_path = file_path.replace('.encrypted', '')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)
    
    print(f'Fichier {decrypted_file_path} déchiffré et sauvegardé')

def main():
    # Générer une clé
    key = generate_key()
    print(f'Clé générée : {key.decode()}')

    # Chemin vers le fichier Python à chiffrer
    file_path = "exemple.py"  # Remplacez 'exemple.py' par le chemin du fichier que vous souhaitez chiffrer
    
    # Chiffrer le fichier
    encrypt_file(file_path, key)
    
    # Déchiffrer le fichier pour tester
    encrypted_file_path = file_path + '.encrypted'
    decrypt_file(encrypted_file_path, key)

if __name__ == '__main__':
    main()
