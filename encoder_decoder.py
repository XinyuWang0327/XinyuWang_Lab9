def password_encoder(password):
    # Check if the password is 8 digits and contains only integers
    if len(password) == 8 and password.isdigit():
        # Shift each digit up by 3 and take care of digit overflow
        encoded = ''.join(str((int(char) + 3) % 10) for char in password)
        return encoded
    else:
        return "Invalid password. Ensure it is an 8-digit integer."

def password_decoder(encoded_password):
    # Check if the encoded password is 8 digits and contains only integers
    if len(encoded_password) == 8 and encoded_password.isdigit():
        # Shift each digit down by 3 and take care of digit underflow
        decoded = ''.join(str((int(char) - 3) % 10) for char in encoded_password)
        return decoded
    else:
        return "Invalid encoded password. Ensure it is an 8-digit integer."