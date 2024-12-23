import pygame
import random

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LIGHT_GREEN = (144, 238, 144)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Obstacle Course Game with Kaomojis")

kaomojis_player = "─=≡Σ(((  •̀ω•́)"
kaomojis_obstacle = "( ´O` )"
kaomojis_speed = "ᓚ₍ ^. .^₎"
kaomojis_after_speed = ".𖥔 ݁ ˖.𖥔 ݁ ˖.𖥔 ݁ ˖. ݁₊ ⊹ . ݁˖ . ݁.𖥔 ݁ ˖"

def draw_player(x, y, has_speed_item):
    kaomoji = kaomojis_after_speed if has_speed_item else kaomojis_player
    font = pygame.font.SysFont("Arial", 36)
    text = font.render(kaomoji, True, LIGHT_GREEN)
    screen.blit(text, (x, y))

def create_obstacle():
    return pygame.Rect(Screen_WIDTH, random.randint(300, 500), 40, 40)

def create_speed_item():
    return pygame.Rect(SCREEN_WIDTH, random.randint(300, 500), 30, 30)

def game_loop():
    player_x = 100
    player_y = SCREEN_HEIGHT - 100
    player_rect = pygame.Rect(player_x, player_y, 40, 40)
    has_speed_item = False

