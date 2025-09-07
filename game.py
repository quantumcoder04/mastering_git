from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

# --- Game Application Setup ---
app = Ursina()

def input(key):
    if key == 'escape':
        quit()

# --- Environment ---
# Create the ocean
water = Entity(
    model='plane',
    color=color.cyan,
    scale=(200, 1, 200),
    position=(0, 0, 0),
    collider='box'
)

# Create a simple island
island = Entity(
    model='sphere',
    color=color.rgb(210, 180, 140),  # Sandy color
    scale=(50, 10, 50),
    position=(0, -5, 0),
    collider='mesh'
)

# Add some palm trees to the island
for i in range(10):
    tree = Entity(
        model='cube',
        color=color.brown,
        scale=(1, 5, 1),
        position=(random.uniform(-20, 20), 2.5, random.uniform(-20, 20)),
    )
    # Add leaves
    Entity(
        parent=tree,
        model='sphere',
        color=color.green,
        scale=(5, 5, 5),
        position=(0, 3, 0)
    )

# --- Player ---
player = FirstPersonController(
    position=(5, 5, 5),
    speed=8
)

# --- Pirate Ship (Going Merry) ---
# A simple representation of the Going Merry
ship_body = Entity(
    model='cube',
    color=color.white,
    scale=(8, 2, 20),
    position=(15, 1, 0),
    rotation=(0, -30, 0)
)
mast = Entity(
    model='cube',
    color=color.brown,
    scale=(1, 10, 1),
    parent=ship_body,
    position=(0, 6, 0)
)
sail = Entity(
    model='quad',
    color=color.white,
    scale=(10, 8),
    parent=mast,
    position=(0, 0, 0),
    double_sided=True,
    texture='white_cube' # Placeholder for a custom sail texture
)

# --- Treasure Chest ---
treasure_chest = Entity(
    model='cube',
    color=color.gold,
    scale=1.5,
    position=(-15, 1, -15),
    collider='box'
)

# --- Game Logic ---
def update():
    # Check if the player finds the treasure
    if player.intersects(treasure_chest).hit:
        Text(text="You found the treasure!", origin=(0, 0), scale=2, duration=4, color=color.yellow)
        treasure_chest.enabled = False # Hide the chest after finding it

# Add a sky for atmosphere
Sky()

# --- Run the Game ---
app.run()
