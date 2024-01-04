import pygame
from sys import exit
import time

#CLASSES

#PLAYER CLASS
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        Player_standing_1 = pygame.image.load('player/Player1.png').convert_alpha()
        Player_standing_2 = pygame.image.load('player/Player2.png').convert_alpha()
        self.Player_index = 0
        self.Player_standing = [Player_standing_1, Player_standing_2]
        self.Player_jump = pygame.image.load('player/PlayerJUMP.png').convert_alpha()



        self.image = self.Player_standing[self.Player_index]
        self.rect = self.image.get_rect(midbottom = (200, 700))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('sound/jump.mp3')
        self.jump_sound.set_volume(0.08)
        
        pass
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 700:
            self.gravity = -21
            self.jump_sound.play()
        if keys[pygame.K_w]:
            self.rect.y -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_a]:
            self.rect.x -= 10
        if keys[pygame.K_r]:
            self.rect.x = 200
        #DO the same for gravity, but when mouse is clicked with the player rectangle
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.rect.bottom >= 700:
                self.gravity = -21
                self.jump_sound.play()

        pass 
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity 
        if self.rect.bottom >= 700:
            self.rect.bottom = 700
            self.gravity = 0
   
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        pass
    #


    def animation_state(self):
        if self.rect.bottom < 700:
            self.image = self.Player_jump
    
        else:
            self.Player_index += 0.1
            if self.Player_index  >= len(self.Player_standing): self.Player_index =0
            self.image = self.Player_standing[int(self.Player_index)%2]

class Obstacles(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100

#PLAYER CLASS END
#CLASSES END

#FUNCTIONS

#FUNCTIONS END

#INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((1500, 900))
pygame.display.set_caption('Analog Horor 1.2')
MaximumFrameRate = pygame.time.Clock()
bg_music = pygame.mixer.Sound('sound/scaryAudio.mp3')
bg_music.set_volume(0.5)
scary_music_intro = pygame.mixer.Sound('sound/scaryIntro.mp3')
scary_music_intro.set_volume(0.5)
#INTRO SCREEN
custom_cursor = pygame.Surface((32, 32), pygame.SRCALPHA)
test_font = pygame.font.Font("font/Mangolaine.ttf",50)
home_screen = pygame.image.load('images/homeScreen3.jpg').convert_alpha()
title_screen = pygame.image.load('images/title.png').convert_alpha()
start_surf = test_font.render('Start',False,'Black').convert_alpha()
start_rect = start_surf.get_rect(center = (200, 700))
quit_surf = test_font.render('Quit',False,'Black').convert_alpha()
quit_rect = quit_surf.get_rect(center = (400, 700))
#INTRO SCREEN END
#MUSIC
bg_music.play(loops=-1)
#MUSIC END

#LEVELS
#LEVEL_1
Floor_1 = pygame.image.load('images/ground1.png').convert_alpha()
Background = pygame.image.load('images/background.jpg').convert_alpha()
Background = pygame.transform.smoothscale_by(Background, 3)

#LEVEL_1 END

#PLAYER

Player_Gravity = 0
Player_Speed = 10
player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)
player_group.draw(screen)
player_group.update()


#PLAYER END


#COLORS
white = (255,255,255)
black = (0,0,0)
#COLORS END

#GAMESTATES
run = True
game_active = False
level_1 = False
level_2 = False
level_3 = False
level_4 = False
level_5 = False
game_over = False
game_win = False
MovingRight = False
#GAMESTATES END

#MUSIC END
#INTRO
Intro_1 = pygame.image.load('Intro/frame1.gif').convert_alpha()
Intro_2 = pygame.image.load('Intro/frame2.gif').convert_alpha()
Intro_3 = pygame.image.load('Intro/frame3.gif').convert_alpha()
Intro_4 = pygame.image.load('Intro/frame4.gif').convert_alpha()
Intro_5 = pygame.image.load('Intro/frame5.gif').convert_alpha()
Intro_6 = pygame.image.load('Intro/frame6.gif').convert_alpha()
Intro_7 = pygame.image.load('Intro/frame7.gif').convert_alpha()
Intro_8 = pygame.image.load('Intro/frame8.gif').convert_alpha()
Intro_9 = pygame.image.load('Intro/frame9.gif').convert_alpha()
Intro_10 = pygame.image.load('Intro/frame10.gif').convert_alpha()
Intro_11 = pygame.image.load('Intro/frame11.gif').convert_alpha()
Intro_12 = pygame.image.load('Intro/frame12.gif').convert_alpha()
Intro_13 = pygame.image.load('Intro/frame13.gif').convert_alpha()
Intro_14 = pygame.image.load('Intro/frame14.gif').convert_alpha()
Intro_15 = pygame.image.load('Intro/frame15.gif').convert_alpha()
Intro_16 = pygame.image.load('Intro/frame16.gif').convert_alpha()
Intro_17 = pygame.image.load('Intro/frame17.gif').convert_alpha()
Intro_18 = pygame.image.load('Intro/frame18.gif').convert_alpha()
Intro_19 = pygame.image.load('Intro/frame19.gif').convert_alpha()
Intro_20 = pygame.image.load('Intro/frame20.gif').convert_alpha()
Intro_21 = pygame.image.load('Intro/frame22.gif').convert_alpha()
Intro_23 = pygame.image.load('Intro/frame23.gif').convert_alpha()
Intro_24 = pygame.image.load('Intro/frame24.gif').convert_alpha()
Intro_25 = pygame.image.load('Intro/frame25.gif').convert_alpha()
Intro_26 = pygame.image.load('Intro/frame26.gif').convert_alpha()
Intro_27 = pygame.image.load('Intro/frame27.gif').convert_alpha()
Intro_28 = pygame.image.load('Intro/frame28.gif').convert_alpha()

Intro_Index = 0
Intro_Images = [Intro_1, Intro_2, Intro_3, Intro_4, Intro_5, Intro_6, Intro_7, Intro_8, Intro_9, Intro_10, Intro_11, Intro_12, Intro_13, Intro_14, Intro_15, Intro_16, Intro_17, Intro_18, Intro_19, Intro_20, Intro_21, Intro_23, Intro_24, Intro_25, Intro_26, Intro_27, Intro_28]

Intro_image = Intro_Images[Intro_Index]

def animation_state_intro():
    global Intro_Index, Intro_image
    Intro_Index += 0.1
    print("Intro_Index:", Intro_Index)  # Add this line for debugging
    if Intro_Index >= len(Intro_Images):
        Intro_Index = 0
    Intro_image = Intro_Images[int(Intro_Index) % 28]

def display_update():
    global Intro_image, screen

    # Update the introduction animation state
    animation_state_intro()

    # Blit the current image onto the screen
    screen.blit(Intro_image, (-400, 0))

    # Update the display
    pygame.display.update()

#INTRO

#GAME LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
        if event.type == pygame.MOUSEBUTTONDOWN and run:
            if start_rect.collidepoint((event.pos)):
                scary_music_intro.play(loops=0)
                time.sleep(1)
                game_active = True
                run = False
                bg_music.stop() 
            elif quit_rect.collidepoint((event.pos)) & run:
                
                time.sleep(0.1)
                pygame.quit()
                exit()

        if event.type == pygame.KEYDOWN and game_active:
            if event.key == pygame.K_d and pygame.KEYDOWN:
                
                MovingRight = True
            else:
                MovingRight = False


        
    #GAME LOOP END

    if run:
        display_update()
        Hello = pygame.draw.rect(screen, 'Black', pygame.Rect(0, 0, 1500, 900))
        screen.blit(home_screen, (0, 0))
        screen.blit(title_screen, (130, 50))
        pygame.draw.rect(screen, white, (128, 650, 160, 100),border_radius=10)
        pygame.draw.rect(screen, white, (325, 650, 160, 100),border_radius=10)
        screen.blit(quit_surf,quit_rect)
        mouse_pos = pygame.mouse.get_pos()
        if start_rect.collidepoint((mouse_pos)):
            if pygame.mouse.get_focused():
                start_surf = test_font.render('Start',False,'Orange').convert_alpha()
                start_rect = start_surf.get_rect(center = (200, 700))
                pygame.draw.rect(screen, 'Orange', start_rect, 100, 10)
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                start_surf = test_font.render('Start',False,'Black').convert_alpha()
                
        elif quit_rect.collidepoint((mouse_pos)):
            if pygame.mouse.get_focused():
                quit_surf = test_font.render('Quit',False,'Orange').convert_alpha() 
                quit_rect = quit_surf.get_rect(center = (400, 700))
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else: 
                quit_surf = test_font.render('Quit',False,'Black').convert_alpha()
        else:
            if pygame.mouse.get_focused():
                start_surf = test_font.render('Start',False,'Black').convert_alpha()
                quit_surf = test_font.render('Quit',False,'Black').convert_alpha()
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
        pygame.draw.rect(screen, 'White', start_rect, 100, 10)
        screen.blit(start_surf,start_rect)

    elif game_active:
        
        screen.fill('Black')
        screen.blit(Floor_1, (0, 700))
        player_group.draw(screen)
        player_group.update()
        Player_Gravity += 1

        
        
    





    pygame.display.update()
    MaximumFrameRate.tick(60)
