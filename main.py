import sys
 
import pygame
from pygame.locals import *
from car import Car
from settings import *
from road import Road
from obstacle import Obstacle
 
pygame.init()
 
fps = 60
timer = 10
mob_gap = 200
timer_gap = 1000
fpsClock = pygame.time.Clock()
 
screen = pygame.display.set_mode((width, height))

MOBCARTICK = pygame.USEREVENT
TIMERTICK = pygame.USEREVENT + 1
pygame.time.set_timer(MOBCARTICK, mob_gap)
pygame.time.set_timer(TIMERTICK, timer_gap)

# Creating Objects
spinny = Car()
spinny_group = pygame.sprite.Group()
spinny_group.add(spinny)

road = Road()

mob_car_group = pygame.sprite.Group()

def display_score(screen):
  font = pygame.font.Font(None, 30)
  score_surf = font.render('Lives: ' + str(spinny.lives), True, (0, 255, 0))
  score_surf_width = score_surf.get_width()
  gap = 30
  score_x = width - gap - score_surf_width
  score_y = gap
  screen.blit(score_surf, (score_x, score_y))

def display_timer(screen):
  font = pygame.font.Font(None, 30)
  score_surf = font.render('Timer: ' + str(timer), True, (0, 255, 0))
  gap = 30
  screen.blit(score_surf, (gap, gap))

def display_message(screen, message):
  font = pygame.font.Font(None, 70)
  game_over_surf = font.render(message, True, (255, 0, 0))
  game_over_surf_width = game_over_surf.get_width()
  game_over_surf_height = game_over_surf.get_height()
  gap = 30
  game_over_x = (width/2) - (game_over_surf_width/2)
  game_over_y = (height/2) - (game_over_surf_height/2)
  screen.blit(game_over_surf, (game_over_x, game_over_y))

 
# Game loop.
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

    if event.type == MOUSEBUTTONDOWN:
      spinny.speed += 1
    else:
      spinny.speed -= 1


    if event.type == MOBCARTICK:
      mob_car = Obstacle()
      mob_car_group.add(mob_car)

    if event.type == TIMERTICK:
      timer -= 1
  
  # Update.
  spinny_group.update()
  mob_car_group.update()
  car_hit_list = pygame.sprite.spritecollide(spinny, mob_car_group, True)
  for mob in car_hit_list:
    spinny.lives -= 1
  
  # Draw.
  if timer < 1:
    display_message(screen, 'You Win')   
  elif spinny.lives <= 0:
    display_message(screen, 'Game Over')
  else:
    road.draw(screen, spinny.speed)
    spinny_group.draw(screen)
    mob_car_group.draw(screen)
    display_score(screen)
    display_timer(screen)
  
  pygame.display.flip()
  fpsClock.tick(fps)