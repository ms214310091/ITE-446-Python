import pygame

black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
purple = (255,0,255)
yellow   = ( 255, 255,   0)

Moving=pygame.image.load('images/Moving Pacman.gif')
pygame.display.set_icon(Moving)

#To Attract More People: Add music
pygame.mixer.init()
pygame.mixer.music.load('Music/pacmanfever.mp3')
pygame.mixer.music.play(-1, 0.0)

# This represents the bar at the bottom that the player controls
class Wall(pygame.sprite.Sprite):
    # Constructor function
    def __init__(self,x,y,width,height, color):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        # Make a blue wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

        # This creates all the walls in room 1
        def setupRoomOne(all_sprites_list):
            # Make the walls. (x_pos, y_pos, width, height)
            wall_list = pygame.sprite.RenderPlain()