import pygame

# Function to check for collisions
def checkCollision(x,y,treasureX,treasureY):
  # Use global keyword to declare global variables
  global screen, textWin

  collisionState = False

  # Check if playerImage touches the treasureImage
  if (y >= treasureY and y <= treasureY + 100):
    if (x >= treasureX and x <= treasureX + 100):
      # Move playerImage back to original starting position
      y = 550
      x = 0
      collisionState = True
    elif (x + 100 >= treasureX and x + 100 <= treasureX + 100):
      y = 550
      x = 0
      collisionState = True
  elif (y + 200 >= treasureY and y + 200 <= treasureY + 200):
    if (x >= treasureX and x <= treasureX + 100):
      y = 550
      x = 0
      collisionState = True
    elif (x + 100 >= treasureX and x + 100 <= treasureX + 100):
      y = 550
      x = 0
      collisionState = True
  return collisionState, y, x

# Initialize Pygame Library
pygame.init()

# Display is an object inside Pygame
# Set Mode method creates a screen with the size inputted
screen = pygame.display.set_mode((1000,700))

# Variable to keep track if our game is finished
finished = False

# Set x & y coordinates
x = 0
y = 550

# Load player image to playerImage variable
playerImage = pygame.image.load("rocket.png")

# Scale and transform Image to fit rectangle
playerImage = pygame.transform.scale(playerImage, (100, 200))

# Make playerImage ready for game
playerImage = playerImage.convert_alpha()

# Load background image to backgroundImage variable
backgroundImage = pygame.image.load("space.jpg")

# Scale and transform Image to fit the screen
backgroundImage = pygame.transform.scale(backgroundImage, (1000,700))

# Put background image into the window
screen.blit(backgroundImage, (0,0))

# Load treasure image to treasureImage variable
treasureImage = pygame.image.load("mars.png")

# Scale and transform Image to be smaller than the playerImage
treasureImage = pygame.transform.scale(treasureImage, (100, 100))

# Make treasureImage ready for game
treasureImage = treasureImage.convert_alpha()

# Load enemy image to enemyImage variable
enemyImage = pygame.image.load("asteroid.png")

# Scale and transform enemyImage
enemyImage = pygame.transform.scale(enemyImage, (35,40))

# Make enemyImage ready for game
enemyImage = enemyImage.convert_alpha()

# Set treasure coordinates
treasureX = 890
treasureY = 10

# Set enemy coordinates
enemyX = 600
enemyY = 500

# Put treasure image into the window
screen.blit(treasureImage, (treasureX, treasureY))

# Get font from Pygame and store in font variable
font = pygame.font.Font("MuktaMahee.ttf", 60)

# Create Levels variable
level = 1

# Create a Clock and store in frame variable
frame = pygame.time.Clock()

# Define if the playerImage has collided with the treasure
collisionTreasure = False

# Define if the playerImage has collided with the enemy
collisionEnemy = False

# Determines the direction the enemy is moving
movingUp = True

# While our game is not finished
while (finished == False):
  # get() method gives us all of the events that have happened since last check
  for event in pygame.event.get():
    # Looking at Event type. If type is a Quit Event then finish the game
    if event.type == pygame.QUIT:
      finished = True

  # Check if key is pressed
  pressedKeys = pygame.key.get_pressed()

  # If enemy is about to reach the bottle of the screen then movingUp equals true
  if (enemyY >= 665):
    movingUp = True
  # If enemy is about to reach the bottle of the screen then movingUp equals false
  elif (enemyY <= 10 ):
    movingUp = False

  # If movingUp is true then move enemy up
  if movingUp == True:
    # Scale movement depending on the level
    enemyY -= 5 * level
  # Else if movingUp is false then move enemy down
  else:
    # Scale movement depending on the level
    enemyY += 5 * level

  # If Space Key is pressed then increase the y coordinate by 5
  if (pressedKeys[pygame.K_SPACE] == 1):
    y -= 3
    x += 5

  # Store rectangle object in a variable
  # Define x, y, width, and height of rectangle
  # rectOne = pygame.Rect(x,y,30,30)

  # Create a tuple to hold a color
  color = (0,0,255)
  # Define the color black in a variable
  white = (255,255,255)

  # Overwrite the original blue rectangle to black before creating a new one
  # screen.fill((white))

  # Fill background image onto the screen
  screen.blit(backgroundImage, (0,0))

  # Put treasure image onto the screen
  screen.blit(treasureImage, (treasureX, treasureY))

  # Put playerImage into window
  screen.blit(playerImage, (x, y))

  # Put enemyImage into window
  screen.blit(enemyImage, (enemyX, enemyY))

  # Call checkCollision function and store in variables
  collisionTreasure, y, x = checkCollision(x,y,treasureX,treasureY)

  # Call checkCollision function and store in variables
  collisionEnemy, y, x = checkCollision(x,y,enemyX,enemyY)

  # Refactor checkCollisions function to make it DRY (Don't Repeat Yourself)
  if (collisionTreasure == True):
    # Increment Level
    level += 1
    # Create text object and display level that user is on
    textWin = font.render("You've reached level " + str(level), True, (255,255,255))
    # Display textWin on the screen and center the text
    screen.blit(textWin, (500 - textWin.get_width()/2, 350 - textWin.get_height()/2))
    # Update the screen
    pygame.display.flip()
    # Slow down frame to make text appear slower
    frame.tick(1)

  # Draws rectangle onto the screen, need to input screen, color, and rectangle object
  # pygame.draw.rect(screen, color, rectOne)

  # Update the screen
  pygame.display.flip()

  # Create frame rate (frames per second)
  frame.tick(30)