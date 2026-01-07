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

#  MAP 
MAP = [
    "###########",
    "#.........#",
    "#..##.....#",
    "#.........#",
    "#....###..#",
    "#.........#",
    "###########"
]

TILE = 100
MAP_WIDTH = len(MAP[0]) * TILE
MAP_HEIGHT = len(MAP) * TILE

#  INIT 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#  PLAYER 
px, py = 150, 150
angle = 0
speed = 2

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

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    # Movement
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

    # Drawing
    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (70, 70, 70), (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

    ray_angle = angle - HALF_FOV

    for ray in range(NUM_RAYS):
        for depth in range(1, MAX_DEPTH):
            x = px + depth * math.cos(ray_angle)
            y = py + depth * math.sin(ray_angle)

            if is_wall(x, y):
                depth *= math.cos(angle - ray_angle)  # remove fish-eye
                wall_height = 50000 / (depth + 0.0001)

                color = 255 / (1 + depth * depth * 0.00002)
                pygame.draw.rect(
                    screen,
                    (color, color, color),
                    (ray * SCALE, HEIGHT // 2 - wall_height // 2, SCALE, wall_height)
                )
                break

        ray_angle += DELTA_ANGLE

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
