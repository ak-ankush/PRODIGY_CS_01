def encrypt(text, shift):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to Encrypt(e) or Decrypt(d) or Quit(q)? ").lower() #convert the string to lowercase
        if choice == 'q':
            print("Exiting the program")
            print("**************************************************************************************")
            break
        if choice.lower() not in ['e', 'd']:
            print("**************************************************************************************")
            print("Invalid choice! Please enter 'e' to Encrypt, 'd' to Eecrypt, or 'q' to Quit.")
            print("**************************************************************************************")
            continue
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value! Please enter a valid integer.")
            continue
        if choice == 'e':
            print("Encrypted message: ", encrypt(message, shift))
        elif choice == 'd':
            print("Decrypted message: ", decrypt(message, shift))

if __name__ == "__main__":
    main()