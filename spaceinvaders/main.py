import pygame
import os
import time
import random


WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# LOAD IMAGES
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))
# PLAYER SHIP
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# LASERS
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# BACKGROUND
BG = pygame.image.load(os.path.join("assets", "background-black.png"))
