# MonJumper is a game that will be similar to geometry dash.

#import modules
import pygame




def initialize():
    # Intialize the pygame
    pygame.init()

    #create a resizeable screen  (withd, height)
    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def main():
    initialize()


if __name__=='__main__':
    main()