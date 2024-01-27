import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    character_sets = {
        'uppercase': string.ascii_uppercase if use_uppercase else '',
        'lowercase': string.ascii_lowercase if use_lowercase else '',
        'numbers': string.digits if use_numbers else '',
        'special_chars': string.punctuation if use_special_chars else ''
    }

    selected_characters = ''.join(character_sets.values())
    
    if not selected_characters:
        print("Please choose at least one character set.")
        return

    password = ''.join(random.choice(selected_characters) for _ in range(length))
    return password

def main():
    print("Password Generator Tool")

    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)

    if password:
        print("Generated Password:", password)
    else:
        print("Password generation failed. Please try again.")

if __name__ == "__main__":
    main()
