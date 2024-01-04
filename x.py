import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Controlled Rectangle")

# Set up rectangle
rect_width, rect_height = 50, 30
rect_x, rect_y = (width - rect_width) // 2, (height - rect_height) // 2
rect_speed = 5

# Set up colors
white = (255, 255, 255)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the state of the keys
    keys = pygame.key.get_pressed()

    # Update rectangle position based on keys
    if keys[pygame.K_a]:
        rect_x -= rect_speed
    if keys[pygame.K_d]:
        rect_x += rect_speed

    # Clear the screen
    screen.fill(white)

    # Draw the rectangle
    pygame.draw.rect(screen, (0, 128, 255), (rect_x, rect_y, rect_width, rect_height))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(60)
