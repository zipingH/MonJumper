#import modules
import pygame
from pygame.locals import *
from sys import exit


class Game(object):

    def __init__(self):
        # Intialize the pygame
        pygame.init()

        # create a resizable screen  (withd, height)
        self.screen = pygame.display.set_mode((800, 400), HWSURFACE|DOUBLEBUF|RESIZABLE)
        self.background_screen = self.screen.copy()
        
        # change window/screen title
        pygame.display.set_caption("MonJumper")

        ##################### create surface  ##################### 
        # width = 100
        # height = 200
        # self.test_surface = pygame.Surface((width,height))
        # self.position = (0,0)
        
        # width = 100
        # height = 200
        # position = (0,0)
        # position (x,y) to move right +x to move down +y
        # example : position = (200px to the left, 100px from the top)

        # self.test_surface = pygame.Surface((width,height))
        # color = 'red'
        # self.test_surface.fill(color)
        
        # sky surface
        self.sky_surface = pygame.image.load('./graphics/Sky.png').convert()
        
        # ground surface
        self.ground_surface = pygame.image.load('./graphics/ground.png').convert()
        
        # text surface
        test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
        self.text_surface = test_font.render('My Game', False, 'Black')
        
        # snail surface and draws snail rectangle
        self.snail_surface = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()
        self.snail_rectangle = self.snail_surface.get_rect(bottomright = (600, 300))
        
        #player_surface and draws player rectangle
        self.player_surface = pygame.image.load('./graphics/Player/player_walk_1.png').convert_alpha()
        self.player_rectangle = self.player_surface.get_rect(midbottom = (80,300))
        
        
        

    def drawSurface(self):
        # sky surface
        self.background_screen.blit(self.sky_surface, (0, 0))

        # ground surface
        self.background_screen.blit(self.ground_surface, (0, 300))
        
        # text surface
        self.background_screen.blit(self.text_surface, (300,50))
        
        # snail surface
        self.snail_rectangle.x -= 1
        
        if self.snail_rectangle.x <= 0:
            self.snail_rectangle.left = 800
    
        self.background_screen.blit(self.snail_surface, self.snail_rectangle)
        
        # player surface
        self.player_rectangle.left += 1
        # print(self.player_rectangle.left)
        
        self.background_screen.blit(self.player_surface, self.player_rectangle)
        
        
    def checkCollisions(self):
        if self.player_rectangle.colliderect(self.snail_rectangle) == 1:
            print("collision")
            self.player_rectangle.x -= 15
            self.snail_rectangle.x += 30
            
            
            
            
    
    

    def gameLoop(self):
        # Game loop for screen to run

        # clock
        clock = pygame.time.Clock()
        
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    exit()
                elif event.type == VIDEORESIZE:
                    self.screen = pygame.display.set_mode(event.size, HWSURFACE|DOUBLEBUF|RESIZABLE)
            
            self.drawSurface()
            
            
            #resizable screen
            self.screen.blit(pygame.transform.scale(self.background_screen, self.screen.get_rect().size), (0,0))
            
            # check collision between player_rectangle and snail_rectangle
            self.checkCollisions()
            
            # draw all our elements and update everything in here:
            pygame.display.update()

            # this loop should not run faster than 60x per sec
            clock.tick(60)

       

    def main(self):
        self.__init__()
        self.gameLoop()


if __name__ == '__main__':
    game = Game()
    game.main()
