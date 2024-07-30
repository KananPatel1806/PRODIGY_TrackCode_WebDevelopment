def encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            encrypted_text += new_char
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                new_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            decrypted_text += new_char
        else:
            decrypted_text += char

    return decrypted_text

# Example usage
if __name__ == "__main__":
    mode = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if mode == 'E':
        encrypted_message = encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif mode == 'D':
        decrypted_message = decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid mode selected.")
