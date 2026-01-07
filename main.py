import pygame
import math



#  SETTINGS 
WIDTH = 1267
HEIGHT = 775
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
SCALE = WIDTH // NUM_RAYS

# GAME STATES
MENU = "menu"
GAME = "game"
CREDITS = "credits"
game_state = MENU

# INIT 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#  MAP 
MAP = [
    "###########",
    "#......#..#",
    "#..##.....#",
    "#.........#",
    "#.........#",
    "#.....##..#",
    "###########"
]

TILE = 100
MAP_WIDTH = len(MAP[0]) * TILE
MAP_HEIGHT = len(MAP) * TILE

# FONTS
title_font = pygame.font.SysFont("arialblack", 72)
menu_font = pygame.font.SysFont("arial", 32)
small_font = pygame.font.SysFont("arial", 24)

# PLAYER 
px, py = 150, 150
angle = 0
speed = 2

def draw_centered_text(text, font, color, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(WIDTH // 2, y))
    screen.blit(surface, rect)

def is_wall(x, y):
    if x < 0 or y < 0:
        return True
    if x >= MAP_WIDTH or y >= MAP_HEIGHT:
        return True
    return MAP[int(y // TILE)][int(x // TILE)] == "#"


# GAME LOOP 
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if game_state == MENU:
                game_state = GAME
            elif game_state == CREDITS:
                game_state = MENU
            elif event.key == pygame.K_c and game_state == GAME:
                game_state = CREDITS

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if game_state == GAME:
            game_state = MENU
        else:
            running = False

    # ---------------- MENU ----------------
    if game_state == MENU:
        screen.fill((10, 10, 20))

        draw_centered_text("ARGON", title_font, (200, 200, 255), HEIGHT // 2 - 80)
        draw_centered_text("The Last Knight", menu_font, (180, 180, 220), HEIGHT // 2 - 20)

        draw_centered_text("Press any key to begin", small_font, (200, 200, 200), HEIGHT // 2 + 60)
        draw_centered_text("ESC to quit", small_font, (150, 150, 150), HEIGHT // 2 + 100)

        pygame.display.flip()
        clock.tick(60)
        continue

    # ---------------- CREDITS ----------------
    if game_state == CREDITS:
        screen.fill((0, 0, 0))

        draw_centered_text("Credits", menu_font, (255, 255, 255), 120)
        draw_centered_text("Argon: The Last Knight", small_font, (200, 200, 200), 180)
        draw_centered_text("Created by Nathan Chan", small_font, (200, 200, 200), 220)
        draw_centered_text("Powered by Python & Pygame", small_font, (200, 200, 200), 260)
        draw_centered_text("Press any key to return", small_font, (180, 180, 180), 340)

        pygame.display.flip()
        clock.tick(60)
        continue

    # ---------------- GAME ----------------
    dx = math.cos(angle) * speed
    dy = math.sin(angle) * speed

    if keys[pygame.K_w] and not is_wall(px + dx, py + dy):
        px += dx
        py += dy
    if keys[pygame.K_s] and not is_wall(px - dx, py - dy):
        px -= dx
        py -= dy
    if keys[pygame.K_a]:
        angle -= 0.04
    if keys[pygame.K_d]:
        angle += 0.04

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (70, 70, 70), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    ray_angle = angle - HALF_FOV

    for ray in range(NUM_RAYS):
        for depth in range(1, MAX_DEPTH):
            x = px + depth * math.cos(ray_angle)
            y = py + depth * math.sin(ray_angle)

            if is_wall(x, y):
                depth *= math.cos(angle - ray_angle)
                wall_height = 50000 / (depth + 0.0001)

                color = 255 / (1 + depth * depth * 0.00002)
                pygame.draw.rect(
                    screen,
                    (color, color, color),
                    (ray * SCALE, HEIGHT // 2 - wall_height // 2, SCALE, wall_height)
                )
                break

        ray_angle += DELTA_ANGLE

    draw_centered_text("Press C for Credits", small_font, (200, 200, 200), HEIGHT - 20)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()