import base64

def decode_and_save(encoded_base64_code, output_file_path):
    """Decode Base64 encoded data and save the decoded data to a file."""
    try:
        
        decoded_data = base64.b64decode(encoded_base64_code)
        
        
        with open(output_file_path, 'wb') as output_file:
            output_file.write(decoded_data)
        
        print(f"Decoded data has been saved to: {output_file_path}")
    except base64.binascii.Error:
        print("The provided input is not a valid Base64 encoded string.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    
    encoded_base64_code = input("Please enter the Base64 encoded string: ")
    
    
    output_file_path = "decoded_file.py"
    
    
    decode_and_save(encoded_base64_code, output_file_path)

if __name__ == "__main__":
    main()
