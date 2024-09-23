import os
from PIL import Image

def encrypt_image(image_path, key, output_path="encrypted_image.png"):
    try:
        if not os.path.exists(image_path):
            print(f"Error: File not found at {image_path}")
            return 
        
        img= Image.open(image_path)
        pixels= img.load()

        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                r = ( r + key) % 256
                g = ( g + key) % 256
                b = ( b + key) % 256
                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e :
        print(f"Error during image encryption: {e}")


def decrypt_image(encrypted_image_path, key, output_path="decrypted_image.png"):
    try:
        if not os.path.exists(encrypted_image_path):
            print(f"Error: File not found at {encrypted_image_path}")
            return 
        
        img= Image.open(encrypted_image_path)
        pixels= img.load()

        width, height = img.size
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                r = ( r - key) % 256
                g = ( g - key) % 256
                b = ( b - key) % 256
                pixels[x, y] = (r, g, b)

        img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")

    except Exception as e :
        print(f"Error during image decryption: {e}")


if __name__ == "__main__":

    action = input("Do you want to (e)ncrypt or (d)ecrypt the image? (e/d): ").strip().lower()

    if action == 'e':
        image_path = input("Enter the image path to encrypt (full path): ").strip()

        if not os.path.exists(image_path):
            print(f"Error: The file '{image_path}' was not found. Please enter a valid path.")
        else: 
            try:
                encryption_key = int(input("Enter the encryption key (integer): "))
                encrypt_image(image_path, encryption_key)
            except ValueError:
                print("Error: Please enter a valid integer for the key.")

    elif action == 'd':
        encrypted_image_path = input("Enter the path of the encrypted image: ").strip()

        if not os.path.exists(encrypted_image_path):
            print(f"Error: The file '{encrypted_image_path}' was not found.")
        else:
            try:
                encryption_key = int(input("Enter the decryption key (same as encryption key): "))
                decrypt_image(encrypted_image_path, encryption_key)

            except ValueError:
                print("Error: Please enter a valid integer for the key.")

    else:
        print("Error: Unrecognized action. Please enter 'e' to encrypt or 'd' to decrypt.")