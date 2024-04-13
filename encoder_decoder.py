def password_encoder(password):
    if len(password) == 8 and password.isdigit():
        return ''.join(str((int(char) + 3) % 10) for char in password)
    else:
        return "Invalid password. Ensure it is an 8-digit integer."

def password_decoder(encoded_password):
    if len(encoded_password) == 8 and encoded_password.isdigit():
        return ''.join(str((int(char) - 3) % 10) for char in encoded_password)
    else:
        return "Invalid encoded password. Ensure it is an 8-digit integer."

def decode_passwords(stored_passwords):
    if stored_passwords:
        for original, encoded in stored_passwords.items():
            print(f"The encoded password {encoded} decodes to the original password {original}.")
    else:
        print("No passwords have been encoded yet.")
