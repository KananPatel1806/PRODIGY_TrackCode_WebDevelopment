from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = np.array(image)
    
    np.random.seed(key)
    random_array = np.random.randint(0, 256, size=pixels.shape, dtype=np.uint8)
    
    encrypted_pixels = (pixels + random_array) % 256
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_image_path)
    print(f"Image encrypted and saved to {output_image_path}")

def decrypt_image(input_image_path, output_image_path, key):
    image = Image.open(input_image_path)
    pixels = np.array(image)
    
    np.random.seed(key)
    random_array = np.random.randint(0, 256, size=pixels.shape, dtype=np.uint8)
    
    decrypted_pixels = (pixels - random_array) % 256
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_image_path)
    print(f"Image decrypted and saved to {output_image_path}")

# Example usage
if __name__ == "__main__":
    mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    input_path = input("Enter the path of the input image: ")
    output_path = input("Enter the path for the output image: ")
    key = int(input("Enter the encryption/decryption key: "))

    if mode == 'E':
        encrypt_image(input_path, output_path, key)
    elif mode == 'D':
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid mode selected.")
