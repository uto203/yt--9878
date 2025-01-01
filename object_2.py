
import os
import pygame

# Initialize variables for the add-on
boss_spawned = False  # Tracks whether the boss has spawned
image_shown = False  # Tracks whether the image has already been shown

# Path to the image (4454.png) in the same directory as this script
image_path = os.path.join(os.path.dirname(__file__), '4454.png')
image = pygame.image.load(image_path).convert_alpha()  # Ensure transparency is handled

# Initialize the game data (to be filled by the game during initialization)
game_data = {}

# Function to initialize the add-on with game data
def initialize(data):
    global game_data
    game_data.update(data)

# Function to update the add-on state
def update():
    global boss_spawned, image_shown

    # Check if a boss has spawned
    for boss in game_data.get('bosses', []):
        if boss.get('spawned') and not boss_spawned:
            boss_spawned = True
            break

# Optimized function to apply overlay blending mode
def apply_overlay_fast(base_surface, overlay_surface):
    # Use pygame's built-in blending functions for faster operation
    temp_surface = overlay_surface.copy()
    temp_surface.set_alpha(128)  # Adjust transparency level (128 = 50%)
    base_surface.blit(temp_surface, (0, 0), special_flags=pygame.BLEND_RGBA_ADD)

# Function to draw the image on the screen using overlay blend mode
def draw(screen):
    global boss_spawned, image_shown

    # If a boss has spawned and the image has not yet been shown, display the image
    if boss_spawned and not image_shown:
        # Create a temporary surface scaled to the screen size
        temp_surface = pygame.transform.scale(image, screen.get_size())

        # Apply the optimized overlay blend mode
        apply_overlay_fast(screen, temp_surface)

        image_shown = True  # Mark the image as shown

# Example usage:
# initialize({'bosses': [{'spawned': True}]})
# update()
# draw(screen)


