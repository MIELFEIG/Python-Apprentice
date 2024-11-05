import random

# Define the ranks and suits
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create the deck of 52 cards
def create_deck():
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(f'{rank} of {suit}')
    return deck

# Shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)
    return deck

# Deal the cards to tableau
def deal_cards(deck):
    tableau = []
    for i in range(7):
        tableau.append([deck.pop() for _ in range(i + 1)])
    return tableau

# Create, shuffle, and deal the deck
deck = create_deck()
shuffled_deck = shuffle_deck(deck)
tableau = deal_cards(shuffled_deck)

# Display the tableau
for i, column in enumerate(tableau):
    print(f"Column {i+1}: {column}")

# Helper function to print the tableau
def print_tableau(tableau):
    for i, column in enumerate(tableau):
        print(f"Column {i + 1}: {column}")

# Move a card from one tableau column to another
def move_card_from_tableau(tableau, from_column, to_column):
    from_column -= 1
    to_column -= 1
    if tableau[from_column]:
        card = tableau[from_column].pop()
        tableau[to_column].append(card)
        print(f"Moved {card} from Column {from_column + 1} to Column {to_column + 1}")
    else:
        print("Invalid move. The column is empty.")

# Example usage:
# Move a card from Column 1 to Column 2
move_card_from_tableau(tableau, 1, 2)

# Print updated tableau
print_tableau(tableau)
def user_input():
    print("\nAvailable commands:")
    print("  'move <from_column> <to_column>' to move a card from one column to another.")
    print("  'draw' to draw a card from the stock.")
    print("  'quit' to quit the game.")
    
    command = input("Enter a command: ").strip().lower()
    
    if command.startswith("move"):
        _, from_col, to_col = command.split()
        from_col, to_col = int(from_col), int(to_col)
        return 'move', from_col, to_col
    elif command == 'draw':
        return 'draw', None, None
    elif command == 'quit':
        return 'quit', None, None
    else:
        print("Invalid command.")
        return None, None, None

# Main game loop
def main_game():
    while True:
        print_tableau(tableau)
        action, from_col, to_col = user_input()
        
        if action == 'move':
            move_card_from_tableau(tableau, from_col, to_col)
        elif action == 'quit':
            print("Thanks for playing!")
            break
        elif action == 'draw':
            print("Drawing from the stock is not implemented yet.")
            # Add stock drawing logic here later.

# Start the game
main_game()
