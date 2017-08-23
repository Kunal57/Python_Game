import pygame

# Initialize Pygame Library
pygame.init()

# Display is an object inside Pygame
# Set Mode method creates a screen with the size inputted
screen = pygame.display.set_mode((900,700))

# Variable to keep track if our game is finished
finished = False

# While our game is not finished
while (finished == False):
  # get() method gives us all of the events that have happened since last check
  for event in pygame.event.get():
    # keyword to not do anything
    pass