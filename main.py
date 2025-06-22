import pygame
import sys
import time
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 1300
HEIGHT = 750
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Argon: The last knight")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHTBLUE = (180, 215, 230)
RED = (250, 0, 0)
BLUE = (0, 0, 250)
SKYBLUE = (135, 206, 235)
CORNFLOWERBLUE = (154, 206, 235)
BABYBLUE = (137, 207, 240)
DODGERBLUE = (89, 174, 254)

# Fonts
font = pygame.font.Font(None, 50)

# Main Menu
def main_menu():
    while True:
        screen.fill(WHITE)
        pygame.display.set_caption("Argon: The last knight")


