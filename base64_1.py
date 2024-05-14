import os

def base64_custom_encode(data):
    """Encodes data using a custom Base64 encoding algorithm."""
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bits = ''.join(format(ord(char), '08b') for char in data)
    padded_bits = bits + '0' * ((6 - len(bits) % 6) % 6)
    indexes = [int(padded_bits[i:i+6], 2) for i in range(0, len(padded_bits), 6)]
    encoded = ''.join(chars[index] for index in indexes)
    return encoded + '=' * ((4 - len(encoded) % 4) % 4)

def encode_python_code(source_code_file, output_file):
    """Encodes the content of a Python source code file and writes a self-decoding script to an output file."""
    with open(source_code_file, 'r', encoding='utf-8') as file:
        source_code = file.read()

    encoded_code = base64_custom_encode(source_code)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(f"exec(__import__('base64').b64decode('{encoded_code}').decode('utf-8'))\n")

def encode_directory(source_directory, output_directory):
    """Encodes all Python files in the specified directory and outputs them to a new directory."""
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(source_directory):
        if filename.endswith('.py'):
            source_code_file = os.path.join(source_directory, filename)
            output_file = os.path.join(output_directory, filename)
            encode_python_code(source_code_file, output_file)
            print(f"Encoded {filename} and saved to {output_file}")

def main():
    source_directory = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/'  
    output_directory = '/Users/arnaudcoubran/Documents/Cours B3/Projet_de_fin/Script_obfusque'  
    encode_directory(source_directory, output_directory)
    print("All files have been encoded and saved to the output directory.")

if __name__ == "__main__":
    main()
