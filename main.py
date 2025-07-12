import pygame
import sys

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

# Fonts
font = pygame.font.Font(None, 80)
button_font = pygame.font.Font(None, 60)

# Draw a button
def draw_button(text, x, y, width, height, color, text_color=BLACK):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surf = button_font.render(text, True, text_color)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)
    return pygame.Rect(x, y, width, height)

# Main Menu
def main_menu():
    running = True
    while running:
        screen.fill(WHITE)

        # Title
        title = font.render("Argon: The Last Knight", True, BLACK)
        title_rect = title.get_rect(center=(WIDTH // 2, 150))
        screen.blit(title, title_rect)

        # Buttons
        play_button = draw_button("Play", 500, 300, 300, 80, LIGHTBLUE)
        quit_button = draw_button("Quit", 500, 400, 300, 80, RED)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    print("Game Starting...")  # Replace with actual game start
                elif quit_button.collidepoint(event.pos):
                    running = False

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def playGame():
    ran = True
    while ran:
        screen.fill(BLACK)

main_menu()
