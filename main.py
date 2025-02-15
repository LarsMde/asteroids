# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame   
from constants import *

def main():
    pygame.init()
    pygame.time.Clock = 0
    dt = 0
    print("Starting asteroids!")

    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids Game")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0), rect=None, special_flags=0)
        pygame.display.flip()
        pygame.time.Clock.tick(60)
        dt = pygame.time.Clock.get_time()/1000  
    
if __name__ == "__main__":
    main()