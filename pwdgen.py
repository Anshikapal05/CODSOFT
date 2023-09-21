import random
import string

def generate_password(length):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password using random.choices
    password = ''.join(random.choices(characters, k=length))
    
    return password

def main():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    print("     <---PASSWORD GENERATOR--->\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n")
    print("**A password generator is a useful tool that generates strong and random passwords for users.**\n\n")
    # Prompt the user to specify the desired length of the password
    try:
        length = int(input("\nEnter the desired length of the password: "))
    except ValueError:
        print("\nPlease enter a valid integer for the length!")
        print("\nTry Again")
        return

    if length <= 0:
        print("\nPassword length must be greater than 0!")
        print("\nTry Again\n")
        return

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print("\n\nGenerated Password: ", password)
    print("\nTHANK YOU!")

if __name__ == "__main__":
    main()
