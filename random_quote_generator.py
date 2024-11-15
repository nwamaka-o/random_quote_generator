import random

# List of inspirational quotes
quotes = [
    "The best way to predict the future is to invent it. – Alan Kay",
    "Life is 10% what happens to us and 90% how we react to it. – Charles R. Swindoll",
    "Your time is limited, so don’t waste it living someone else’s life. – Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. – Albert Schweitzer",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "Act as if what you do makes a difference. It does. – William James",
]


def random_quote():
    """Selects and returns a random quote from the list."""
    return random.choice(quotes)


def main():
    print("Welcome to the Random Quote Generator!")
    while True:
        print("\nHere's your quote:")
        print(f"\"{random_quote()}\"")
        print("\nWould you like another quote? (yes/no)")

        user_input = input("> ").strip().lower()
        if user_input == 'no':
            print("\nThank you for using the Random Quote Generator. Stay inspired!")
            break
        elif user_input != 'yes':
            print("Invalid input. Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
