
from encoder_decoder import password_encoder, password_decoder, decode_passwords
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
                print("Your password has been encoded and stored!")


        elif option == '2':
            decode_passwords(stored_passwords)

        elif option == '3':
            # Quit the program
            break

        else:
            print("Invalid option. Please try again.")

# To run the program, you would uncomment the main() call in a local Python environment
# main()
if __name__ == "__main__":
    main()