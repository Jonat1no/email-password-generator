import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + numbers + special_characters

    length = max(length, 8)

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def save_to_file(passwords):
    with open('generated_passwords.txt', 'a') as file:
        for password in passwords:
            file.write(password + '\n')

def main():
    while True:
        try:
            password_length = int(input("Enter the desired password length: "))
        except ValueError:
            print("Please enter a valid integer for the password length.")
            continue

        password = generate_password(password_length)
        print("Generated Password:", password)

        another_password = input("Do you want to generate another password? (yes/no): ").lower()
        if another_password != 'yes':
            break

    save_to_file_option = input("Do you want to save the generated passwords to a file? (yes/no): ").lower()
    if save_to_file_option == 'yes':
        passwords_to_save = [generate_password(12) for _ in range(5)]  # Example: save 5 passwords
        save_to_file(passwords_to_save)
        print("Passwords saved to 'generated_passwords.txt'.")

if __name__ == "__main__":
    main()
import random
import string

def generate_password(length):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    special_characters = string.punctuation

    all_characters = uppercase_letters + lowercase_letters + numbers + special_characters

    length = max(length, 8)

    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    try:
        password_length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid integer for the password length.")
        return

    password = generate_password(password_length)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
