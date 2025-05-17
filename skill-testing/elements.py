# Periodic Table Word Chain Game (2 Players with File Save and History)
#lets fucking goooo 
#today song is Runaway by aurora it nice song 
import time

# List of valid periodic table elements (lowercased for consistency)
elements = [
    "hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen",
    "oxygen", "fluorine", "neon", "sodium", "magnesium", "aluminum", "silicon",
    "phosphorus", "sulfur", "chlorine", "argon", "potassium", "calcium", "scandium",
    "titanium", "vanadium", "chromium", "manganese", "iron", "cobalt", "nickel",
    "copper", "zinc", "gallium", "germanium", "arsenic", "selenium", "bromine",
    "krypton", "rubidium", "strontium", "yttrium", "zirconium", "niobium",
    "molybdenum", "technetium", "ruthenium", "rhodium", "palladium", "silver",
    "cadmium", "indium", "tin", "antimony", "tellurium", "iodine", "xenon",
    "cesium", "barium", "lanthanum", "cerium", "praseodymium", "neodymium",
    "promethium", "samarium", "europium", "gadolinium", "terbium", "dysprosium",
    "holmium", "erbium", "thulium", "ytterbium", "lutetium", "hafnium",
    "tantalum", "tungsten", "rhenium", "osmium", "iridium", "platinum", "gold",
    "mercury", "thallium", "lead", "bismuth", "polonium", "astatine", "radon",
    "francium", "radium", "actinium", "thorium", "protactinium", "uranium",
    "neptunium", "plutonium", "americium", "curium", "berkelium", "californium",
    "einsteinium", "fermium", "mendelevium", "nobelium", "lawrencium", "rutherfordium",
    "dubnium", "seaborgium", "bohrium", "hassium", "meitnerium", "darmstadtium",
    "roentgenium", "copernicium", "nihonium", "flerovium", "moscovium", "livermorium",
    "tennessine", "oganesson"
]

elements = [el.lower() for el in elements]

def get_last_letter(word):
    for ch in reversed(word):
        if ch.isalpha():
            return ch.lower()
    return ""

def play_game():
    used = []
    player1 = input("Enter name for Player 1: ").strip()
    player2 = input("Enter name for Player 2: ").strip()
    scores = {player1: 0, player2: 0}
    turn = 0
    current_letter = ""
    round_number = 1

    while True:
        print(f"\n--- Round {round_number} ---")
        current_player = player1 if turn == 0 else player2
        print(f"{current_player}'s turn.")

        if current_letter:
            print(f"Element must start with: '{current_letter}'")

            # Check if there are any valid elements left
            valid_options = [
                el for el in elements
                if el.startswith(current_letter) and el not in used
            ]
            if not valid_options:
                print(f"No elements left starting with '{current_letter}'!")
                print(f"{current_player} loses! Game over.")
                winner = player1 if turn == 1 else player2
                break

        guess = input("Enter an element: ").strip().lower()

        if guess not in elements:
            print("❌ That is not a valid element. Game over.")
            winner = player1 if turn == 1 else player2
            break
        if guess in used:
            print("❌ That element was already used. Game over.")
            winner = player1 if turn == 1 else player2
            break
        if current_letter and guess[0] != current_letter:
            print("❌ Wrong starting letter. Game over.")
            winner = player1 if turn == 1 else player2
            break

        used.append(guess)
        scores[current_player] += 1
        current_letter = get_last_letter(guess)
        print(f"✅ Good! {current_player} score: {scores[current_player]}")
        turn = 1 - turn
        round_number += 1

    # Game over display
    print("\n🏁 Final Scores:")
    print(f"{player1}: {scores[player1]}")
    print(f"{player2}: {scores[player2]}")
    print(f"🎉 Winner: {winner}")

    save_results(player1, player2, scores[player1], scores[player2], winner, used)


def save_results(p1, p2, s1, s2, winner, used):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open("game_results.txt", "a") as file:
        file.write("=== Periodic Table Word Chain Result ===\n")
        file.write(f"Date: {timestamp}\n")
        file.write(f"{p1}: {s1} point(s)\n")
        file.write(f"{p2}: {s2} point(s)\n")
        file.write(f"Winner: {winner}\n")
        file.write("Used Elements: " + ", ".join(used) + "\n")
        file.write("----------------------------------------\n")


def view_past_results():
    print("\n📜 Previous Game Results:")
    try:
        with open("game_results.txt", "r") as file:
            content = file.read()
            print(content if content.strip() else "No past results found.")
    except FileNotFoundError:
        print("No game history found.")


def display_menu():
    print("\n--- Periodic Table Word Chain ---")
    print("1. Start New Game")
    print("2. View Past Results")
    print("3. Exit")


def main():
    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()
        if choice == "1":
            play_game()
        elif choice == "2":
            view_past_results()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")

main()
