def encrypt_caesar(ciphertext, shift):
    # Create empty string to store encrypt result
    encrypted = ""

    # Loop through each character in the input text
    for char in ciphertext:
        
        # Check if character is a letter (A-Z or a-z)
        if char.isalpha():
            
            # Decide ASCII starting point
            # 65 = ASCII of 'A'
            # 97 = ASCII of 'a'
            # This keeps uppercase and lowercase correct
            ascii_offset = 65 if char.isupper() else 97
            
            # Convert letter to number using ord()
            # Subtract base ASCII value
            # Subtract shift to encrypt
            # Use % 26 to wrap around alphabet
            # Convert back to character using chr()
            encrypted += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        
        else:
            # If character is not a letter (space, number, symbol)
            # Just add it as it is
            encrypted += char

    # Return the final encrypted text
    return encrypted


if __name__ == "__main__":
    
    # Ask user to enter encrypted message
    ciphertext = input("Enter the text to encrypt: ").strip()
    
    # Ask user to enter shift value
    # Convert input string into integer
    shift = int(input("Enter the shift you want: ").strip())

    # Call decrypt function and store result
    result = encrypt_caesar(ciphertext, shift)

    # Print decrypted result
    print(result)
