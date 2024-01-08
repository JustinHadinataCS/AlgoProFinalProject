import pygame
from sys import exit
import time
#CLASSES
#PLAYER CLASS
#-> In this class, The player animation is being handled, Gravity Function is being defined, while also Making the function for the player input. All of those Function are stored inside the Display_Update function, which is then the function is used to called the class functions.
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        Player_standing_1 = pygame.image.load('player/Player1.png').convert_alpha()
        Player_standing_2 = pygame.image.load('player/Player2.png').convert_alpha()
        #The Player Index is going to be used to shuffled the animation / Images The reason it works #because all of the images have very similiar names and stored. With the only key
        #differences is the number between each image file, hence if we change the player index, the #image will change. That is because the self.image is based on the Self.Player_standing
        #list, and the list is based on the self.Player_index.

        self.Player_index = 0
        self.Player_standing = [Player_standing_1, Player_standing_2]
        self.Player_jump = pygame.image.load('player/PlayerJUMP.png').convert_alpha()
        self.direction = pygame.math.Vector2(0,0)
 
        self.image = self.Player_standing[self.Player_index]
        self.rect = self.image.get_rect(midbottom = (200, 500))
        # we set the rectangle, Gravity and the Jumping sound when certain input is 
        #detected later on
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('sound/jump.mp3')
        self.jump_sound.set_volume(0.2)
        
        pass
    def player_input(self):
        #We check the Player Input, and condition. For Jumping for example,
        #the player can only jump, when the rectangle position is at the bottom or 500,
        #Hence stopping an infinite jumping mechanic. 
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_SPACE] and (self.rect.bottom >= 500) and  (canJump):
            self.gravity = -25
            self.jump_sound.play()
        if keys[pygame.K_w]:
            self.rect.y -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_a]:
            self.rect.x -= 10
        #DO the same for gravity, but when mouse is clicked with the player rectangle
        if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.rect.bottom >= 500:
                self.gravity = -21
                self.jump_sound.play()
        pass 
    def apply_gravity(self):
        #Gravity Function, In short, To replicate the gravity, the longer
        #the player is in the air, the higher the gravity is.
        #This can be done by keep increasing the self.gravity, but connect
        #The self.rect.y with the self.gravity.
        #When The player is on the bottom, we change the gravity
        #Into 0, to stop the player from falling through the ground.
        self.gravity += 1
        self.rect.y += self.gravity 
        if self.rect.bottom >= 500:
            self.rect.bottom = 500
            self.gravity = 0

    def update(self):
        #Where we call all of the function
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        pass
    def animation_state(self):
        #Where the animation is being handled
        if self.rect.bottom < 500:
            self.image = self.Player_jump
        else:
        #The self.Player_index is being increased by 0.1, which is the speed of the animation
        
            self.Player_index += 0.1
            if self.Player_index  >= len(self.Player_standing): self.Player_index =0
            self.image = self.Player_standing[int(self.Player_index)%2]
class Killer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        # Load Killer standing images using a loop
        self.Killer_standing = [pygame.image.load(f'killer/killer{i}.gif').convert_alpha() for i in range(1, 8)]
        
        # Initialize Killer index, image, and position
        self.Killer_index = 0
        self.image = self.Killer_standing[self.Killer_index]
        self.rect = self.image.get_rect(midbottom=(1200, 505))

    def display_update(self, screen):
        # Update Killer's animation state and display on the screen
        self.animation_state()
        screen.blit(self.image, (self.rect.x, self.rect.y))
        pygame.display.update()

    def animation_state(self):
        # Update Killer's animation index and image, and reset if necessary
        self.Killer_index = (self.Killer_index + 0.1) % len(self.Killer_standing)
        self.image = self.Killer_standing[int(self.Killer_index)]
#PLAYER CLASS END
#CLASSES END
#FUNCTIONS
#FUNCTIONS END
#INITIALIZATIONd
pygame.init()

screen = pygame.display.set_mode((1500, 900))
pygame.display.set_caption('Analog Horor 1.2')
MaximumFrameRate = pygame.time.Clock()
bg_music = pygame.mixer.Sound('sound/scaryAudio.mp3')
bg_music.set_volume(0.5)
snow_music = pygame.mixer.Sound('sound/Snow.mp3')
snow_music.set_volume(0.3)
scary_music_intro = pygame.mixer.Sound('sound/scaryIntro.mp3')
scary_music_intro.set_volume(0.3)
loudMusic = pygame.mixer.Sound('sound/LoudNoise.mp3')
loudMusic.set_volume(0.08)
breathing_sound = pygame.mixer.Sound('sound/Breathing.mp3')
breathing_sound.set_volume(0.6)
killer_revealed_sound = pygame.mixer.Sound('sound/killerReveal.mp3')
killer_revealed_sound.set_volume(0.6)


bg_music.play(loops=-1)




#GAME HOME SCREEN AND SURFACES IMAGE
custom_cursor = pygame.Surface((32, 32), pygame.SRCALPHA)
test_font = pygame.font.Font("font/Mangolaine.ttf",50)
home_screen = pygame.image.load('images/homeScreen3.jpg').convert_alpha()
title_screen = pygame.image.load('images/title.png').convert_alpha()
start_surf = test_font.render('Start',False,'Black').convert_alpha()
start_rect = start_surf.get_rect(center = (200, 700))
quit_surf_button = test_font.render('Quit',False,'Black').convert_alpha()
quit_rect_button = quit_surf_button.get_rect(center = (400, 700))
back_surf = test_font.render('Back',False,'White').convert_alpha()
back_rect = back_surf.get_rect(center = (764, 700))
game_over_font = pygame.font.Font("font/Mangolaine.ttf",200)
game_over_surf = test_font.render('GAMEOVER!',False,'Red').convert_alpha()
game_tutorial_font = pygame.font.Font("font/Mangolaine.ttf",70)
game_tutorial_surf = game_tutorial_font.render('Press Space to Continue',False,'White').convert_alpha()
You_Win_surf = test_font.render('GOOD ENDING', False, 'Green').convert_alpha()
bed_surface = pygame.image.load('images/bed.png').convert_alpha()
bed_rect = bed_surface.get_rect(midbottom = (200,500))
killer_screen_surface = pygame.image.load('images/KillerSurfaceImage.jpg').convert_alpha()
phone_surf = pygame.image.load('images/Phone1.png')
hover_phone = pygame.image.load('images/Phone2.png')
phone_rect = phone_surf.get_rect(midbottom = (1100,430))
table_surf =  pygame.image.load('images/table.png').convert_alpha()
table_rect = table_surf.get_rect(midbottom = (1100,510))
#GAME HOME SCREEN END
#MUSIC
#GAME HOME SCREEN END
#MUSIC
def render_back_button(mouse_pos, back_surf, back_rect):
    if back_rect.collidepoint(mouse_pos):
        if pygame.mouse.get_focused():
            back_surf = test_font.render('Back', False, 'Green').convert_alpha()
            back_rect = back_surf.get_rect(center=(764, 700))
            pygame.mouse.set_cursor(*pygame.cursors.diamond)
        else:
            back_surf = test_font.render('Back', False, 'White').convert_alpha()
    else:
        back_surf = test_font.render('Back', False, 'White').convert_alpha()

    return back_surf, back_rect
Floor_1 = pygame.image.load('images/ground2.png').convert_alpha()
#LEVEL_1 END

#PLAYER DRAWING
Player_Gravity = 0
Player_Speed = 10
player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)
player_group.draw(screen)
player_group.update()
#PLAYER END

#TEXTBOX surface
loadingtext = pygame.image.load('textbox/loadingtext.png').convert_alpha()
text1 = pygame.image.load('textbox/text1.png').convert_alpha()
text2 = pygame.image.load('textbox/text2.png').convert_alpha()
text3 = pygame.image.load('textbox/text3.png').convert_alpha()
text4 = pygame.image.load('textbox/text4.png').convert_alpha()
text5 = pygame.image.load('textbox/text5.png').convert_alpha()
text6 = pygame.image.load('textbox/text6.png').convert_alpha()
text7 = pygame.image.load('textbox/text7.png').convert_alpha()
text8 = pygame.image.load('textbox/text8.png').convert_alpha()
text9 = pygame.image.load('textbox/text9.png').convert_alpha()
text10 = pygame.image.load('textbox/text10.png').convert_alpha()
text11 = pygame.image.load('textbox/text11.png').convert_alpha()
text12 = pygame.image.load('textbox/text12.png').convert_alpha()
text13 = pygame.image.load('textbox/text13.png').convert_alpha()
text14 = pygame.image.load('textbox/text14.png').convert_alpha()
text15 = pygame.image.load('textbox/text15.png').convert_alpha()
text16 = pygame.image.load('textbox/text16.png').convert_alpha()
text17 = pygame.image.load('textbox/text17.png').convert_alpha()
text18 = pygame.image.load('textbox/text18.png').convert_alpha()
text19 = pygame.image.load('textbox/text19.png').convert_alpha()
text20 = pygame.image.load('textbox/text20.png').convert_alpha()
text21 = pygame.image.load('textbox/text21.png').convert_alpha()
text22 = pygame.image.load('textbox/text22.png').convert_alpha()
text23 = pygame.image.load('textbox/text23.png').convert_alpha()
text24 = pygame.image.load('textbox/text24.png').convert_alpha()
text25 = pygame.image.load('textbox/text25.png').convert_alpha()
text26 = pygame.image.load('textbox/text26.png').convert_alpha()
text27 = pygame.image.load('textbox/text27.png').convert_alpha()
text28 = pygame.image.load('textbox/text28.png').convert_alpha()
text29 = pygame.image.load('textbox/text29.png').convert_alpha()
#DECISION surface & Rectangle

decision1 = pygame.image.load('textbox/decision1.png').convert_alpha()
decision2 = pygame.image.load('textbox/decision2.png').convert_alpha()
decision1_rect = decision1.get_rect(topleft = (130, 400))
decision2_rect = decision2.get_rect(topleft = (870, 400))

decision3 = pygame.image.load('textbox/decision3.png').convert_alpha()
decision4 = pygame.image.load('textbox/decision4.png').convert_alpha()
decision3_rect = decision3.get_rect(topleft = (130, 400))
decision4_rect = decision4.get_rect(topleft = (870, 400))

decision5 = pygame.image.load('textbox/decision5.png').convert_alpha()
decision6 = pygame.image.load('textbox/decision6.png').convert_alpha()
decision5_rect = decision5.get_rect(topleft = (130, 400))
decision6_rect = decision6.get_rect(topleft = (870, 400))

decision7 = pygame.image.load('textbox/decision7.png').convert_alpha()
decision8 = pygame.image.load('textbox/decision8.png').convert_alpha()
decision7_rect = decision7.get_rect(topleft = (300, 200))
decision8_rect = decision8.get_rect(topleft = (800, 200))

#Color Variable
white = (255,255,255)
black = (0,0,0)
#COLORS END 

#GAMESTATES
#These Are the game States
#Their function is to manage the transition between the frames.
run = True
game_active = False
level_1 = False
level_2 = False
level_3 = False
level_4 = False
level_5 = False
#These are used to manage the textboxes Surface
#So in order to display the right Textboxes I use these variable
#How it works is everytime an Input (SpaceBar) is detected->
#The For event function from Pygame Will Check these Variables
#If for example phone_activated is True, It will continue by
#Making the phone_activated into False while Phone_activated2 into True
#This Cycle Only happens when our user press the spacebar.
#The same can be said for downstair_activated
#The identifiers Explain
phone_activated = False
phone_activated2 = False
phone_activated3 = False
phone_activated4 = False
phone_activated5 = False
phone_activated6 = False
phone_activated7 = False
downstair_activated = False
downstair_activated2 = False
downstair_activated3 = False
downstair_activated4 = False
downstair_activated5 = False
downstair_activated6 = False
downstair_activated7 = False
downstair_activated8 = False
downstair_activated9 = False
downstair_activated10 = False
downstair_activated11 = False
downstair_activated12 = False
downstair_activated13 = False
downstair_activated14 = False
downstair_activated15 = False
Introduction = False
#GAMESTATES

#LOGIC VARIABLE TO KEEP THE GAME RUNNING SMOOTHLY

#Phone Hovered for the Telephone Animation when Hovered
phone_hovered = False
#Killer_activated is for the condition for the killer to move to the right
Killer_activated = False
active = True
active2 = True
active3 = True
canJump = True
game_over = False
game_win = False
#TextBoxes States
text_box1 = True
text_box2 = False
text_box3 = False
text_box4 = False
text_box5 = False
text_box6 = False
text_box7 = False
text_box8 = False
text_box9 = False
text_box10 = False
text_box11 = False
text_box12 = False
text_box13 = False
text_box14 = False
text_box15 = False
text_box16 = False

#MUSIC END
#INTRO
import pygame

class Intro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()        
        self.Intro_Index = 0
        self.Intro_Images = []

        Introduction_Frame1 = pygame.image.load('Intro/frame1.gif').convert_alpha()
        Introduction_Frame2 = pygame.image.load('Intro/frame2.gif').convert_alpha()
        Introduction_Frame3 = pygame.image.load('Intro/frame3.gif').convert_alpha()
        Introduction_Frame4 = pygame.image.load('Intro/frame4.gif').convert_alpha()
        Introduction_Frame5 = pygame.image.load('Intro/frame5.gif').convert_alpha()
        Introduction_Frame6 = pygame.image.load('Intro/frame6.gif').convert_alpha()
        Introduction_Frame7 = pygame.image.load('Intro/frame7.gif').convert_alpha()
        Introduction_Frame8 = pygame.image.load('Intro/frame8.gif').convert_alpha()
        Introduction_Frame9 = pygame.image.load('Intro/frame9.gif').convert_alpha()
        Introduction_Frame10 = pygame.image.load('Intro/frame10.gif').convert_alpha()
        Introduction_Frame11 = pygame.image.load('Intro/frame11.gif').convert_alpha()
        Introduction_Frame12 = pygame.image.load('Intro/frame12.gif').convert_alpha()
        Introduction_Frame13 = pygame.image.load('Intro/frame13.gif').convert_alpha()
        Introduction_Frame14 = pygame.image.load('Intro/frame14.gif').convert_alpha()
        Introduction_Frame15 = pygame.image.load('Intro/frame15.gif').convert_alpha()
        Introduction_Frame16 = pygame.image.load('Intro/frame16.gif').convert_alpha()
        Introduction_Frame17 = pygame.image.load('Intro/frame17.gif').convert_alpha()
        Introduction_Frame18 = pygame.image.load('Intro/frame18.gif').convert_alpha()
        Introduction_Frame19 = pygame.image.load('Intro/frame19.gif').convert_alpha()
        Introduction_Frame20 = pygame.image.load('Intro/frame20.gif').convert_alpha()
        Introduction_Frame21 = pygame.image.load('Intro/frame22.gif').convert_alpha()
        Introduction_Frame23 = pygame.image.load('Intro/frame23.gif').convert_alpha()
        Introduction_Frame24 = pygame.image.load('Intro/frame24.gif').convert_alpha()
        Introduction_Frame25 = pygame.image.load('Intro/frame25.gif').convert_alpha()
        Introduction_Frame26 = pygame.image.load('Intro/frame26.gif').convert_alpha()
        Introduction_Frame27 = pygame.image.load('Intro/frame27.gif').convert_alpha()
        Introduction_Frame28 = pygame.image.load('Intro/frame28.gif').convert_alpha()

        self.Intro_Images = [Introduction_Frame1, Introduction_Frame2, Introduction_Frame3, Introduction_Frame4, Introduction_Frame5, Introduction_Frame6, Introduction_Frame7, Introduction_Frame8, Introduction_Frame9, Introduction_Frame10, Introduction_Frame11, Introduction_Frame12, Introduction_Frame13, Introduction_Frame14, Introduction_Frame15, Introduction_Frame16, Introduction_Frame17, Introduction_Frame18, Introduction_Frame19, Introduction_Frame20, Introduction_Frame21, Introduction_Frame23, Introduction_Frame24, Introduction_Frame25, Introduction_Frame26, Introduction_Frame27, Introduction_Frame28]
        self.Intro_image = self.Intro_Images[self.Intro_Index]

    def animation_state_intro(self):
        self.Intro_Index += 0.1
        #print("Intro_Index:", self.Intro_Index)  # Add this line for debugging
        if self.Intro_Index >= len(self.Intro_Images):
            self.Intro_Index = 0
        self.Intro_image = self.Intro_Images[int(self.Intro_Index) % 28]

    def display_update(self, screen):
        # Update the introduction animation state
        self.animation_state_intro()

        # Blit the current image onto the screen
        screen.blit(self.Intro_image, (-400, 0))

        # Update the display

        pygame.display.update()

# Example usage:
# intro_sprite = Intro()
# intro_sprite.display_update(screen)  # assuming 'screen' is your pygame display surface
intro_sprite = Intro()
killer = Killer()
#
firstCount = 0
phone_rect = phone_surf.get_rect(midbottom=(1100, 430))
hover_phone_rect = hover_phone.get_rect(bottomleft=phone_rect.bottomleft)

#


#INTRO END

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
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint((event.pos)) and run:
                scary_music_intro.play()
                time.sleep(1)
                game_active = True
                run = False
                print(run, game_active)
                bg_music.stop() 
            elif quit_rect_button.collidepoint((event.pos)) and run:
                time.sleep(0.1)
                pygame.quit()
                exit()
            elif back_rect.collidepoint(event.pos) and (text_box15 or phone_activated7 or downstair_activated6 or level_4 or level_5):
                player.rect.x = 200
                run = True
                text_box15 = False
                phone_activated7 = False
                downstair_activated6 = False
                downstair_activated7 = False
                downstair_activated8 = False
                downstair_activated9 = False
                downstair_activated10 = False
                downstair_activated11 = False
                downstair_activated12 = False
                downstair_activated13 = False
                downstair_activated14 = False
                downstair_activated15 = False
                level_4 = False
                level_5 = False
                text_box1 = True
                active = True
                canJump = True


            elif phone_rect.collidepoint((event.pos)) and level_1:
                if active:
                    phone_activated = True
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos
            phone_rect = hover_phone.get_rect(midbottom=(1100, 430))
            phone_hovered = phone_rect.collidepoint(mouse_pos)
        #CHeck if player press spacebar
        if event.type == pygame.KEYDOWN and Introduction:
            if event.key == pygame.K_SPACE:
                time.sleep(0.2)
                if text_box1:
                    text_box1 = False
                    text_box2 = True
                elif text_box2:
                    text_box2 = False
                    text_box3 = True
                elif text_box3:
                    text_box3 = False
                    text_box4 = True
                elif text_box4:
                    text_box4 = False
                    text_box5 = True
                elif text_box5:
                    text_box5 = False
                    text_box6 = True
                elif text_box7:
                    text_box7 = False
                    text_box8 = True
                elif text_box8:
                    text_box8 = False
                    text_box9 = True
                elif text_box9:
                    text_box9 = False
                    text_box10 = True
                elif text_box10:
                    text_box10 = False
                    text_box11 = True
                elif text_box11:
                    text_box11 = False
                    text_box12 = True
                elif text_box12:
                    text_box12 = False
                    text_box13 = True
                elif text_box13:
                    text_box13 = False
                    text_box14 = True
                elif text_box14:
                    text_box14 = False
                    text_box15 = True
                elif text_box16:
                    Introduction = False
                    level_1 = True

                #do the same until text_box15
        if event.type == pygame.KEYDOWN and level_1:
            if event.key == pygame.K_SPACE:
                time.sleep(0.2)
                if phone_activated:
                    active = False
                    phone_activated2 = True
                    phone_activated = False
                elif phone_activated3:
                    phone_activated4 = True
                    phone_activated3 = False
                elif phone_activated4:
                    phone_activated5 = True
                    phone_activated4 = False
                elif phone_activated5:
                    phone_activated6 = True
                    phone_activated5 = False
                elif phone_activated6:
                    phone_activated7 = True
                    phone_activated6 = False
        # Check if the mouse is clicked
        if event.type == pygame.KEYDOWN and level_2:
            if event.key == pygame.K_SPACE:
                time.sleep(0.2)
                if downstair_activated:
                    downstair_activated = False
                    downstair_activated2 = True
                elif downstair_activated3:
                    downstair_activated3 = False
                    downstair_activated4 = True
                elif downstair_activated4:
                    downstair_activated4 = False
                    downstair_activated5 = True
                elif downstair_activated5:
                    downstair_activated5 = False
                    downstair_activated6 = True
                elif downstair_activated7:
                    downstair_activated7 = False
                    downstair_activated8 = True
                elif downstair_activated8:
                    downstair_activated8 = False
                    downstair_activated9 = True
                elif downstair_activated9:
                    player.rect.x = 200
                    downstair_activated9 = False
                    level_2 = False
                    level_3 = True
        if event.type == pygame.KEYDOWN and level_4:
            if event.key == pygame.K_SPACE:
                time.sleep(0.2)
                if downstair_activated10:
                    downstair_activated10 = False
                    downstair_activated11 = True
                elif downstair_activated11:
                    downstair_activated11 = False
                    downstair_activated15 = True
        if event.type == pygame.KEYDOWN and level_5:
            if event.key == pygame.K_SPACE:
                time.sleep(0.2)
                if downstair_activated12:
                    downstair_activated12 = False
                    downstair_activated13 = True
                elif downstair_activated13:
                    downstair_activated13 = False
                    downstair_activated14 = True
                
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse button state
            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0] == 1:
                # Check if the click is within the decision1_rect area
                if decision1_rect.collidepoint(pygame.mouse.get_pos()) and text_box6:
                    time.sleep(0.1)
                    text_box7 = True
                    text_box6 = False
                    # Add your logic here
                elif decision2_rect.collidepoint(pygame.mouse.get_pos()) and Introduction:
                    text_box16 = True
                    text_box6 = False
                    # Add your logic here
                elif decision3_rect.collidepoint(pygame.mouse.get_pos()) and phone_activated2:
                    phone_activated = False
                    phone_activated2 = False
                    active = True
                    canJump = True
                    player.rect.x = 1000
                    # Add your logic here
                elif decision4_rect.collidepoint(pygame.mouse.get_pos()) and phone_activated2:
                    phone_activated3 = True
                    phone_activated2 = False
                    canJump = False
                elif decision5_rect.collidepoint(pygame.mouse.get_pos()) and downstair_activated2:
                    downstair_activated7 = True
                    downstair_activated2 = False
                    player.rect.x = 200
                    killer.rect.x = 1200

                elif decision6_rect.collidepoint(pygame.mouse.get_pos()) and downstair_activated2:
                    downstair_activated3 = True
                    downstair_activated2 = False
                elif decision7_rect.collidepoint(pygame.mouse.get_pos()) and active2 and player.rect.x >= 1200:
                    print('1')
                    player.rect.x = 300
                elif decision8_rect.collidepoint(pygame.mouse.get_pos()) and active2 and player.rect.x >= 1200:
                    print('2') 
                    level_1 = False
                    level_2 = True
                    downstair_activated = True
                    active2 = False
                
                    # Add your logic here
                #repeat until decision 8

        
    #GAME LOOP END

    if run:
        firstCount = 0
        Hello = pygame.draw.rect(screen, 'Black', pygame.Rect(0, 0, 1500, 900))
        screen.blit(home_screen, (0, 0))
        screen.blit(title_screen, (130, 50))
        pygame.draw.rect(screen, white, (128, 650, 160, 100),border_radius=10)
        pygame.draw.rect(screen, white, (325, 650, 160, 100),border_radius=10)
        screen.blit(quit_surf_button, quit_rect_button)
        mouse_pos = pygame.mouse.get_pos()
        if start_rect.collidepoint((mouse_pos)):
            if pygame.mouse.get_focused():
                start_surf = test_font.render('Start',False,'Orange').convert_alpha()
                start_rect = start_surf.get_rect(center = (200, 700))
                pygame.draw.rect(screen, 'Orange', start_rect, 100, 10)
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else:
                start_surf = test_font.render('Start',False,'Black').convert_alpha()
                
        elif quit_rect_button.collidepoint((mouse_pos)):
            if pygame.mouse.get_focused():
                quit_surf_button = test_font.render('Quit',False,'Orange').convert_alpha() 
                quit_rect_button = quit_surf_button.get_rect(center = (400, 700))
                pygame.mouse.set_cursor(*pygame.cursors.diamond)
            else: 
                quit_surf_button = test_font.render('Quit',False,'Black').convert_alpha()
        else:
            if pygame.mouse.get_focused():
                start_surf = test_font.render('Start',False,'Black').convert_alpha()
                quit_surf_button = test_font.render('Quit',False,'Black').convert_alpha()
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
        pygame.draw.rect(screen, 'White', start_rect, 100, 10)
        screen.blit(start_surf,start_rect)
    elif game_active:
        Intro_duration = 300
        start_time = pygame.time.get_ticks()
        intro_sprite.display_update(screen)
        snow_music.play(loops=0)
        firstCount += 1
        print(firstCount)
        if firstCount >= Intro_duration:
                print('Level 1')
                Introduction = True
                snow_music.stop()
                game_active = False
    elif Introduction:
        screen.fill('Black')
        aKey = pygame.key.get_pressed()
        if text_box1:
            screen.blit(game_tutorial_surf, (430, 250))
            screen.blit(text1, (280, 400))
        elif text_box2:
            screen.blit(text2, (280, 400))
        elif text_box3:
            screen.blit(text3, (280, 400))
        elif text_box4:
            screen.blit(text4, (280, 400))
            loudMusic.play(loops=0)
        elif text_box5:
            screen.blit(text5, (280, 400))
        elif text_box6:
            screen.blit(decision1, (130, 400))
            screen.blit(decision2, (870, 400))
            # Outside the event loop
            mouse_buttons = pygame.mouse.get_pressed()
        elif text_box7:
            screen.blit(text6, (280, 400))
        elif text_box8:
            screen.blit(loadingtext, (280, 400))
        elif text_box9:
            breathing_sound.play(loops=1)
            screen.blit(text7, (280, 400))
        elif text_box10:
            breathing_sound.stop()
            killer_revealed_sound.play(loops=0)
            screen.blit(killer_screen_surface,(170,100))
        elif text_box11:
            screen.blit(killer_screen_surface,(170,100))
            screen.blit(loadingtext, (280, 400))
        elif text_box12:
            screen.blit(text9, (280, 400))
        elif text_box13:
            screen.blit(text10, (280, 400))
        elif text_box14:
            screen.blit(text11, (280, 400))
        elif text_box15:
            mouse_pos10 = pygame.mouse.get_pos()
            mouse_pos10 = pygame.mouse.get_pos()
            if back_rect.collidepoint(mouse_pos10):
                if pygame.mouse.get_focused():
                    back_surf = test_font.render('Back', False, 'Red').convert_alpha()
                    back_rect = back_surf.get_rect(center=(764, 700))
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                else:
                    back_surf = test_font.render('Back', False, 'White').convert_alpha()
            else:
                back_surf = test_font.render('Back', False, 'White').convert_alpha()
                #draw the back rect
            #position the game over surf in the middle
            screen.blit(game_over_surf, (630, (screen.get_height() / 2) - 20 ))
            screen.blit(back_surf, back_rect)
        elif text_box16:
            screen.blit(text12, (280, 400))
    elif level_1:
        screen.fill('Black')
        active2 = True
        screen.blit(Floor_1, (0, 500))
        screen.blit(bed_surface, bed_rect)
        screen.blit(table_surf,table_rect)
        mouse_posX = pygame.mouse.get_pos()
        if active:
            if phone_hovered:
                screen.blit(hover_phone, hover_phone_rect)
            else:
                screen.blit(phone_surf, phone_rect)
        player_group.draw(screen)
        player_group.update()
        Player_Gravity += 1
        if active2:
            if player.rect.x >= 1200:
                screen.blit(text18, (280, 400))
                screen.blit(decision7, (300, 200))
                screen.blit(decision8, (800, 200))
        if player.rect.x >= 1350:
            player.rect.x = 1350
        if phone_activated:
            canJump = False
            screen.fill('Black')
            screen.blit(text13, (280, 400))
        elif phone_activated2:
            screen.fill('Black')
            screen.blit(decision3, (130, 400))
            screen.blit(decision4, (870, 400))
        elif phone_activated3:
            screen.fill('Black')
            screen.blit(text14, (280, 400))
        elif phone_activated4:
            screen.fill('Black')
            screen.blit(text15, (280, 400))
        elif phone_activated5:
            screen.fill('Black')
            screen.blit(text16, (280, 400))
        elif phone_activated6:
            screen.fill('Black')
            screen.blit(text17, (280, 400))
        elif phone_activated7:
            screen.fill('Black')
            mouse_pos100 = pygame.mouse.get_pos()
            if back_rect.collidepoint(mouse_pos100):
                if pygame.mouse.get_focused():
                    back_surf = test_font.render('Back', False, 'Green').convert_alpha()
                    back_rect = back_surf.get_rect(center=(764, 700))
                    pygame.mouse.set_cursor(*pygame.cursors.diamond)
                else:
                    back_surf = test_font.render('Back', False, 'White').convert_alpha()
            else:
                back_surf = test_font.render('Back', False, 'White').convert_alpha()
            screen.blit(You_Win_surf, (630, (screen.get_height() / 2) - 20 ))
            screen.blit(back_surf, back_rect)
    elif level_2:
        screen.fill('Black')
        if downstair_activated:
            screen.blit(text19, (280, 400))
        elif downstair_activated2:
            screen.blit(decision5, (130, 400))
            screen.blit(decision6, (870, 400))
        elif downstair_activated3:
            screen.blit(text20, (280, 400))
        elif downstair_activated4:
            screen.blit(text21, (280, 400))
        elif downstair_activated5:
            screen.blit(text22, (280, 400))
        elif downstair_activated6:
            mouse_posx2 = pygame.mouse.get_pos()
            back_surf, back_rect = render_back_button(mouse_posx2, back_surf, back_rect)
            screen.blit(game_over_surf, (630, (screen.get_height() / 2) - 20 ))
            screen.blit(back_surf, back_rect)
                #draw the back rect
            #position the game over surf in the middle
            screen.blit(game_over_surf, (630, (screen.get_height() / 2) - 20 ))
            screen.blit(back_surf, back_rect)
        elif downstair_activated7:
            screen.blit(text23, (280, 400))
        elif downstair_activated8:
            screen.blit(text24, (280, 400))
        elif downstair_activated9:
            screen.blit(text25, (280, 400))
    elif level_3:
        screen.fill('Black')
        screen.blit(Floor_1, (0, 500))
        player_group.draw(screen)
        player_group.update()
        Player_Gravity += 1
        killer.display_update(screen)
        if player.rect.x >= 1350:
            player.rect.x = 1350
        if player.rect.x <= 0:
            player.rect.x = 0
        if player.rect.x >= 400 or player.rect.x <= 30:
            Killer_activated = True
        if Killer_activated:
            killer.rect.x -= 15
        if player.rect.colliderect(killer.rect):
            level_3 = False
            level_4 = True
            player.rect.x = 200
            downstair_activated10 = True
            Killer_activated = False
        if killer.rect.x <= 0:
            level_5 = True
            level_3 = False
            downstair_activated12 = True
            player.rect.x = 200
            Killer_activated = False
    elif level_4:
        screen.fill('Black')
        if downstair_activated10:
            screen.blit(text28, (280, 400))
        elif downstair_activated11:
            screen.blit(text29, (280, 400))
        elif downstair_activated15:
            mouse_posx2 = pygame.mouse.get_pos()
            back_surf, back_rect = render_back_button(mouse_posx2, back_surf, back_rect)
            screen.blit(game_over_surf, (630, (screen.get_height() / 2) - 20 ))
            screen.blit(back_surf, back_rect)
    elif level_5:
        screen.fill('Black')
        if downstair_activated12:
            screen.blit(text26, (280, 400))
        elif downstair_activated13:
            screen.blit(text27, (280, 400))
            mouse_posx2 = pygame.mouse.get_pos()
        elif downstair_activated14:
            mouse_posx2 = pygame.mouse.get_pos()
            back_surf, back_rect = render_back_button(mouse_posx2, back_surf, back_rect)
            screen.blit(You_Win_surf, (630, (screen.get_height() / 2) - 20 ))
            screen.blit(back_surf, back_rect)
    pygame.display.update()
    MaximumFrameRate.tick(60)
