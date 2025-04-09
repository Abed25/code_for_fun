import pygame
import random
import time

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Load sound (you can use any glitch or tech sound you like)
sound = pygame.mixer.Sound("./tech_beep.wav")
sound.play(-1)  # Loop the sound

# Screen settings
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SuperDev Tech")

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Font
font = pygame.font.SysFont('Courier', 24)

# Function to generate a random binary string
def random_binary(length):
    return ''.join(random.choice(['0', '1', "superDev"]) for _ in range(length))

# Binary columns
num_columns = WIDTH // 15  # Adjust to your screen width and desired spacing
binary_columns = [random_binary(HEIGHT // 30) for _ in range(num_columns)]

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw and scroll binary columns
    for i in range(num_columns):
        # Scroll the binary data vertically within each column
        binary_columns[i] = binary_columns[i][1:] + random.choice(['0', '1'])
        # Render the text for each column
        for j, bit in enumerate(binary_columns[i]):
            text = font.render(bit, True, GREEN)
            screen.blit(text, (i * 15, j * 30))  # Adjust spacing between columns and rows
    
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
