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
    # Looking at Event type. If type is a Quit Event then finish the game
    if event.type == pygame.QUIT:
      finished = True

  # Store rectangle object in a variable
  # Define x, y, width, and height of rectangle
  rectOne = pygame.Rect(0,50,30,30)

  # Create a tuple to hold a color
  color = (0,0,255)

  # Draws rectangle onto the screen, need to input screen, color, and rectangle object
  pygame.draw.rect(screen, color, rectOne)

  # Update the screen
  pygame.display.flip()