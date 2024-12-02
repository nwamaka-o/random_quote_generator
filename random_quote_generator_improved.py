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
     # Filter out quotes that are already in the history
    remaining_quotes = [q for q in quotes if q not in history]

    # If all quotes have been shown, reset the history
    if not remaining_quotes:  # All quotes shown, reset history
        history.clear() # Clear the history list
        remaining_quotes = quotes[:] # Reset to the full quotes list

    # Randomly select a quote from the remaining list
    selected_quote = random.choice(remaining_quotes)

    # Add the selected quote to the history for tracking
    history.append(selected_quote)
    return selected_quote # Return the selected quote


def main():
    history = []  # Initialize an empty list to track shown quotes

    # Welcome message
    print("Welcome to the Random Quote Generator! designed by Nwamaka Okalla")
    print("Enjoy inspirational quotes or exit anytime.\n") # Call the random_quote function

    # Infinite loop to keep offering quotes until the user exits
    while True:
        print("\nHere's your quote:")
        print(f"\"{random_quote(history)}\"")

        # Prompt user for input
        print("\nWould you like another quote? (yes/no)")

         # Get user input and normalize to lowercase
        user_input = input("> ").strip().lower()

        # Check user's decision
        if user_input == 'no':
            # Exit the program with a farewell message
            print("\nThank you for using the Random Quote Generator. Stay inspired!")
            print("Credits: All quotes compiled from various authors for inspiration.")
            break # Exit the loop
        elif user_input != 'yes':
            # Handle invalid inputs
            print("Invalid input. Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main() # Entry point of the program
