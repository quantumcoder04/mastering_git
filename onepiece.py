import random

# --- Devil Fruit Definitions ---
# A greatly expanded dictionary of Devil Fruits, categorized by type.
# There are over 144 canon Devil Fruits in One Piece; this is a representative sample.
DEVIL_FRUITS = {
    # --- Paramecia Type ---
    "Gomu Gomu no Mi": {"type": "Paramecia", "ability": "Grants the user a rubber body, allowing them to stretch and absorb blunt force."},
    "Ope Ope no Mi": {"type": "Paramecia", "ability": "Creates a spherical 'room' where the user has total surgical control over everything inside."},
    "Gura Gura no Mi": {"type": "Paramecia", "ability": "Allows the user to create powerful vibrations or 'quakes', capable of immense destruction."},
    "Bara Bara no Mi": {"type": "Paramecia", "ability": "Allows the user to split their body into pieces and control them independently, immune to slashing attacks."},
    "Ito Ito no Mi": {"type": "Paramecia", "ability": "Grants the ability to create and manipulate strings for control, puppetry, and travel."},
    "Soru Soru no Mi": {"type": "Paramecia", "ability": "Allows the user to manipulate souls, giving life to inanimate objects and stealing lifespan."},
    "Nikyu Nikyu no Mi": {"type": "Paramecia", "ability": "Grants paw pads on the hands that can repel anything, including air, attacks, and even abstract concepts like pain."},
    "Horo Horo no Mi": {"type": "Paramecia", "ability": "Allows the user to produce and control ghosts that can drain morale or create explosions."},
    "Doku Doku no Mi": {"type": "Paramecia", "ability": "Grants the ability to produce and control a wide variety of potent poisons."},
    "Kilo Kilo no Mi": {"type": "Paramecia", "ability": "Allows the user to change their weight from 1 to 10,000 kilograms at will."},
    "Bomu Bomu no Mi": {"type": "Paramecia", "ability": "Makes any part of the user's body explosive, including their breath and mucus."},
    "Supa Supa no Mi": {"type": "Paramecia", "ability": "Allows the user to turn any part of their body into a sharp steel blade."},
    "Mochi Mochi no Mi": {"type": "Special Paramecia", "ability": "Allows the user to create, control, and transform into sticky mochi."},

    # --- Logia Type ---
    "Mera Mera no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into fire."},
    "Suna Suna no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into sand."},
    "Goro Goro no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into lightning."},
    "Hie Hie no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into ice."},
    "Yami Yami no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into darkness, with the unique ability to nullify other Devil Fruit powers on contact."},
    "Pika Pika no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into light, enabling light-speed attacks and movement."},
    "Magu Magu no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into magma, boasting incredible offensive power."},
    "Gasu Gasu no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into various forms of gas."},
    "Moku Moku no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into smoke."},
    "Yuki Yuki no Mi": {"type": "Logia", "ability": "Allows the user to create, control, and transform into snow."},

    # --- Zoan Type ---
    "Hito Hito no Mi": {"type": "Zoan", "ability": "Allows an animal to transform into a human or human-hybrid."},
    "Ushi Ushi no Mi, Model: Giraffe": {"type": "Zoan", "ability": "Allows the user to transform into a giraffe or giraffe-hybrid."},
    "Inu Inu no Mi, Model: Wolf": {"type": "Zoan", "ability": "Allows the user to transform into a wolf or wolf-hybrid."},
    "Neko Neko no Mi, Model: Leopard": {"type": "Zoan", "ability": "Allows the user to transform into a leopard or leopard-hybrid, granting immense speed and strength."},
    
    # --- Mythical Zoan Type ---
    "Hito Hito no Mi, Model: Nika": {"type": "Mythical Zoan", "ability": "Grants the user the powers of the Sun God Nika, giving their rubbery body more freedom and strength, described as the 'most ridiculous power in the world'."},
    "Tori Tori no Mi, Model: Phoenix": {"type": "Mythical Zoan", "ability": "Allows the user to transform into a phoenix, granting flight and regeneration from any wound with blue flames of resurrection."},
    "Uo Uo no Mi, Model: Seiryu": {"type": "Mythical Zoan", "ability": "Allows the user to transform into an Azure Dragon, capable of flight and creating devastating flame clouds and lightning."},
    "Inu Inu no Mi, Model: Okuchi no Makami": {"type": "Mythical Zoan", "ability": "Allows the user to transform into a mythical wolf deity, granting the ability to produce chilling breath attacks."},
    "Hito Hito no Mi, Model: Daibutsu": {"type": "Mythical Zoan", "ability": "Allows the user to transform into a giant golden Buddha statue, granting the power to launch powerful shockwaves."},
}

# --- Game Constants ---
EXIT_COORDINATE = (10, -5, 8)

# --- Player Class ---
class Player:
    """Represents the player in the game."""
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.z = 0
        self.devil_fruit_power = None
        self.inventory = []

    def move(self, dx, dy, dz):
        """Moves the player by the given deltas."""
        self.x += dx
        self.y += dy
        self.z += dz
        print(f"You moved. Your new position is ({self.x}, {self.y}, {self.z}).")

    def eat_fruit(self, fruit_name):
        """Allows the player to eat a Devil Fruit from their inventory."""
        # Find the full fruit name from a partial match
        full_fruit_name = None
        for key in self.inventory:
            if fruit_name.lower() in key.lower():
                full_fruit_name = key
                break
        
        if not full_fruit_name:
            print("You don't have that fruit in your inventory.")
            return

        if self.devil_fruit_power:
            print("You already have a Devil Fruit power! You cannot eat another.")
            return

        print(f"You eat the {full_fruit_name}...")
        self.devil_fruit_power = DEVIL_FRUITS[full_fruit_name]
        self.inventory.remove(full_fruit_name)
        print(f"You have gained the power of the {full_fruit_name}!")
        print(f"Ability: {self.devil_fruit_power['ability']}")

    def check_status(self):
        """Displays the player's current status."""
        print("\n--- PLAYER STATUS ---")
        print(f"Player: {self.name}")
        print(f"Position: ({self.x}, {self.y}, {self.z})")
        if self.devil_fruit_power:
            power_name = [name for name, data in DEVIL_FRUITS.items() if data == self.devil_fruit_power][0]
            print(f"Devil Fruit Power: {power_name} ({self.devil_fruit_power['type']})")
        else:
            print("Devil Fruit Power: None")
        print(f"Inventory: {self.inventory if self.inventory else 'Empty'}")
        print("---------------------\n")

# --- Game Functions ---
def roll_for_devil_fruit():
    """Simulates rolling for a random Devil Fruit from the expanded list."""
    fruit_name = random.choice(list(DEVIL_FRUITS.keys()))
    print(f"You rolled and found the {fruit_name}!")
    return fruit_name

def print_instructions():
    """Prints the available commands to the player."""
    print("\n--- Available Commands ---")
    print("roll         - Roll for a new Devil Fruit.")
    print("eat [fruit]  - Eat a fruit from your inventory (e.g., 'eat Gomu Gomu no Mi').")
    print("move [x] [y] [z] - Move your character (e.g., 'move 1 0 -1').")
    print("status       - Check your current power and position.")
    print("help         - Show this list of commands.")
    print("exit         - Quit the game.")
    print("--------------------------\n")

# --- Main Game Loop ---
def game_loop():
    """The main loop that runs the game."""
    player_name = input("Enter your pirate name: ")
    player = Player(player_name)
    
    print(f"\nWelcome, {player.name}! You find yourself in a mysterious world.")
    print(f"Your goal is to reach the exit coordinates: {EXIT_COORDINATE}")
    print_instructions()

    while True:
        if (player.x, player.y, player.z) == EXIT_COORDINATE:
            print("\nCongratulations! You have reached the exit and escaped!")
            break

        command = input("> ").strip().split()
        if not command:
            continue

        action = command[0].lower()

        if action == "exit":
            print("Fair winds on your next adventure!")
            break
        elif action == "help":
            print_instructions()
        elif action == "status":
            player.check_status()
        elif action == "roll":
            found_fruit = roll_for_devil_fruit()
            player.inventory.append(found_fruit)
            print(f"The {found_fruit} has been added to your inventory.")
        elif action == "eat":
            if len(command) > 1:
                fruit_name_to_eat = " ".join(command[1:])
                player.eat_fruit(fruit_name_to_eat)
            else:
                print("What fruit do you want to eat? Use 'eat [fruit name]'.")
        elif action == "move":
            try:
                if len(command) == 4:
                    dx, dy, dz = map(int, command[1:])
                    player.move(dx, dy, dz)
                else:
                    print("Invalid move command. Use 'move [x] [y] [z]'.")
            except ValueError:
                print("Invalid move command. Please use integer values for coordinates.")
        else:
            print("Unknown command. Type 'help' to see the list of commands.")

if __name__ == "__main__":
    game_loop()

