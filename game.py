import pygame

# Initialize Pygame Library
pygame.init()

# Display is an object inside Pygame
# Set Mode method creates a screen with the size inputted
screen = pygame.display.set_mode((900,700))

# Variable to keep track if our game is finished
finished = False

# Set x & y coordinates
x = 0
y = 50

# Load player image to playerImage variable
playerImage = pygame.image.load("elon_musk.png")

# Scale and transform Image to fit rectangle
playerImage = pygame.transform.scale(playerImage, (30, 30))

# Make playerImage ready for game
playerImage = playerImage.convert()

# Create a Clock and store in frame variable
frame = pygame.time.Clock()

# While our game is not finished
while (finished == False):
  # get() method gives us all of the events that have happened since last check
  for event in pygame.event.get():
    # Looking at Event type. If type is a Quit Event then finish the game
    if event.type == pygame.QUIT:
      finished = True

  # Check if key is pressed
  pressedKeys = pygame.key.get_pressed()

  # If Space Key is pressed then increase the y coordinate by 5
  if (pressedKeys[pygame.K_SPACE] == 1):
    y += 5

  # Store rectangle object in a variable
  # Define x, y, width, and height of rectangle
  rectOne = pygame.Rect(x,y,30,30)

  # Create a tuple to hold a color
  color = (0,0,255)
  # Define the color black in a variable
  black = (0,0,0)

  # Overwrite the original blue rectangle to black before creating a new one
  screen.fill((black))

  # Put playerImage into window
  screen.blit(playerImage, (x, y))

  # Draws rectangle onto the screen, need to input screen, color, and rectangle object
  # pygame.draw.rect(screen, color, rectOne)

  # Update the screen
  pygame.display.flip()

  # Create frame rate (frames per second)
  frame.tick(30)