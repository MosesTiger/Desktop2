import pygame 
import sys 
from pygame.locals import * 

pygame.init()

screen = pygame.display.set_mode((800,600))

paddle = pygame.Rect(400,500,60,10)
ball = pygame.Rect(400,300,10,10)
ball_dx = 1
ball_dy = 1 

bricks = [pygame.Rect(50+100*i,50+20*j,80,10) for i in range(7) for j in range(3)]

def draw_text(text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, (255,255,255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    screen.blit(text_surface, text_rect)
def game_over():
    draw_text("GAME OVER",48)