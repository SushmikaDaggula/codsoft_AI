import secrets
import string

class PasswordGenerator:
    def __init__(self):
        self.complexity_levels = {
            'low': string.ascii_letters + string.digits,
            'medium': string.ascii_letters + string.digits + string.punctuation,
            'high': string.ascii_letters + string.digits + string.punctuation + string.ascii_letters.upper() + string.punctuation
        }

    def generate_password(self, length, complexity='medium'):
        characters = self.complexity_levels.get(complexity)
        if not characters:
            raise ValueError("Invalid complexity level. Choose 'low', 'medium', or 'high'.")

        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password

def get_user_input():
    length = int(input("Enter the desired length of the password: "))
    complexity = input("Enter the complexity level (low, medium, high): ").lower()
    return length, complexity

def display_password(password):
    print("Generated Password:", password)

def main():
    password_generator = PasswordGenerator()

    try:
        length, complexity = get_user_input()
        generated_password = password_generator.generate_password(length, complexity)
        display_password(generated_password)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
