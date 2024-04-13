
from encoder_decoder import password_encoder, password_decoder
def main():
    stored_passwords = {}  # Dictionary to store the encoded passwords

    while True:
        # Display the menu
        print("Menu\n-----\n1. Encode\n2. Decode\n3. Quit")
        option = input("Please enter an option: ")

        if option == '1':
            # Encode password
            password = input("Please enter your password to encode: ")
            encoded = password_encoder(password)
            if encoded.startswith("Invalid"):
                print(encoded)  # Print the error message
            else:
                stored_passwords[password] = encoded  # Store the encoded password associated with the original
                print(f"Your password has been encoded to {encoded} and stored.")

        elif option == '2':
            # Decode password
            # Directly display all stored passwords and their decoded form
            if stored_passwords:
                for original, encoded in stored_passwords.items():
                    print(f"The encoded password {encoded} decodes to the original password {original}.")
            else:
                print("No passwords have been encoded yet.")

        elif option == '3':
            # Quit the program
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

# To run the program, you would uncomment the main() call in a local Python environment
# main()
if __name__ == "__main__":
    main()