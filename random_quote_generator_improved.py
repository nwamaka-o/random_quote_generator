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


def random_quote(history):
    """Selects a random quote, ensuring no immediate repetition."""
    remaining_quotes = [q for q in quotes if q not in history]
    if not remaining_quotes:  # All quotes shown, reset history
        history.clear()
        remaining_quotes = quotes[:]
    selected_quote = random.choice(remaining_quotes)
    history.append(selected_quote)
    return selected_quote


def main():
    history = []  # To track shown quotes
    print("Welcome to the Random Quote Generator!")
    print("Enjoy inspirational quotes or exit anytime.\n")

    while True:
        print("\nHere's your quote:")
        print(f"\"{random_quote(history)}\"")
        print("\nWould you like another quote? (yes/no)")

        user_input = input("> ").strip().lower()
        if user_input == 'no':
            print("\nThank you for using the Random Quote Generator. Stay inspired!")
            print("Credits: All quotes compiled from various authors for inspiration.")
            break
        elif user_input != 'yes':
            print("Invalid input. Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
