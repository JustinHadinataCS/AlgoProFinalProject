import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('player/Player1.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(200, 500))

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and (self.rect.bottom >= 500) and (canJump):
            self.gravity = -25
        if keys[pygame.K_w]:
            self.rect.y -= 10
        if keys[pygame.K_d]:
            self.rect.x += 10
        if keys[pygame.K_a]:
            self.rect.x -= 10

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity

    def animation_state(self):
        if self.rect.bottom < 500:
            self.image = self.Player_jump
        else:
            self.Player_index += 0.1
            if self.Player_index >= len(self.Player_standing): self.Player_index = 0
            self.image = self.Player_standing[int(self.Player_index)%2]

class Killer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('killer/killer1.gif').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(1200, 505))

    def update(self):
        self.animation_state()

    def animation_state(self):
        self.Killer_index += 0.1
        if self.Killer_index >= len(self.Killer_standing): self.Killer_index = 0
        self.image = self.Killer_standing[int(self.Killer_index)]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1500, 900))
        pygame.display.set_caption('Analog Horor 1.2')
        self.MaximumFrameRate = pygame.time.Clock()
        self.bg_music = pygame.mixer.Sound('sound/scaryAudio.mp3')
        self.bg_music.set_volume(0)
        self.snow_music = pygame.mixer.Sound('sound/Snow.mp3')
        self.snow_music.set_volume(0)
        self.scary_music_intro = pygame.mixer.Sound('sound/scaryIntro.mp3')
        self.scary_music_intro.set_volume(0)
        self.loudMusic = pygame.mixer.Sound('sound/LoudNoise.mp3')
        self.loudMusic.set_volume(0)

        self.home_screen = pygame.image.load('images/homeScreen3.jpg').convert_alpha()
        self.title_screen = pygame.image.load('images/title.png').convert_alpha()
        self.start_surf = pygame.font.Font("font/Mangolaine.ttf", 50).render('Start', False, 'Black').convert_alpha()
        self.start_rect = self.start_surf.get_rect(center=(200, 700))
        self.quit_surf = pygame.font.Font("font/Mangolaine.ttf", 50).render('Quit', False, 'Black').convert_alpha()
        self.quit_rect = self.quit_surf.get_rect(center=(400, 700))
        self.back_surf = pygame.font.Font("font/Mangolaine.ttf", 50).render('Back', False, 'White').convert_alpha()
        self.back_rect = self.back_surf.get_rect(center=(764, 700))
        self.game_over_font = pygame.font.Font("font/Mangolaine.ttf", 200).render('GAMEOVER!', False, 'Red').convert_alpha()
        self.You_Win_surf = pygame.font.Font("font/Mangolaine.ttf", 200).render('GOOD ENDING', False, 'Green').convert_alpha()
        self.bed_surface = pygame.image.load('images/bed.png').convert_alpha()
        self.bed_rect = self.bed_surface.get_rect(midbottom=(200, 500))
        self.killer_screen_surface = pygame.image.load('images/KillerSurfaceImage.jpg').convert_alpha()
        self.phone_surf = pygame.image.load('images/Phone1.png')
        self.hover_phone = pygame.image.load('images/Phone2.png')
        self.phone_rect = self.phone_surf.get_rect(midbottom=(1100, 430))
        self.table_surf = pygame.image.load('images/table.png').convert_alpha()
        self.table_rect = self.table_surf.get_rect(midbottom=(1100, 510))

        self.Floor_1 = pygame.image.load('images/ground2.png').convert_alpha()

        self.player = Player()
        self.player_group = pygame.sprite.GroupSingle()
        self.player_group.add(self.player)

        self.killer = Killer()

        self.text1 = pygame.image.load('textbox/loadingtext.png').convert_alpha()
        self.text2 = pygame.image.load('textbox/text1.png').convert_alpha()
        self.text3 = pygame.image.load('textbox/text2.png').convert_alpha()
        self.text4 = pygame.image.load('textbox/text3.png').convert_alpha()
        self.text5 = pygame.image.load('textbox/text4.png').convert_alpha()
        self.text6 = pygame.image.load('textbox/text5.png').convert_alpha()
        self.text7 = pygame.image.load('textbox/text6.png').convert_alpha()
        self.text8 = pygame.image.load('textbox/text7.png').convert_alpha()
        self.text9 = pygame.image.load('textbox/text8.png').convert_alpha()
        self.text10 = pygame.image.load('textbox/text9.png').convert_alpha()
        self.text11 = pygame.image.load('textbox/text10.png').convert_alpha()
        self.text12 = pygame.image.load('textbox/text11.png').convert_alpha()
        self.text13 = pygame.image.load('textbox/text12.png').convert_alpha()
        self.text14 = pygame.image.load('textbox/text13.png').convert_alpha()
        self.text15 = pygame.image.load('textbox/text14.png').convert_alpha()
        self.text16 = pygame.image.load('textbox/text15.png').convert_alpha()
        self.text17 = pygame.image.load('textbox/text16.png').convert_alpha()
        self.text18 = pygame.image.load('textbox/text17.png').convert_alpha()
        self.text19 = pygame.image.load('textbox/text18.png').convert_alpha()
        self.text20 = pygame.image.load('textbox/text19.png').convert_alpha()
        self.text21 = pygame.image.load('textbox/text20.png').convert_alpha()
        self.text22 = pygame.image.load('textbox/text21.png').convert_alpha()
        self.text23 = pygame.image.load('textbox/text22.png').convert_alpha()
        self.text24 = pygame.image.load('textbox/text23.png').convert_alpha()
        self.text25 = pygame.image.load('textbox/text24.png').convert_alpha()
        self.text26 = pygame.image.load('textbox/text25.png').convert_alpha()
        self.text27 = pygame.image.load('textbox/text26.png').convert_alpha()
        self.text28 = pygame.image.load('textbox/text27.png').convert_alpha()
        self.text29 = pygame.image.load('textbox/text28.png').convert_alpha()

        self.decision1 = pygame.image.load('textbox/decision1.png').convert_alpha()
        self.decision2 = pygame.image.load('textbox/decision2.png').convert_alpha()
        self.decision3 = pygame.image.load('textbox/decision3.png').convert_alpha()
        self.decision4 = pygame.image.load('textbox/decision4.png').convert_alpha()
        self.decision5 = pygame.image.load('textbox/decision5.png').convert_alpha()
        self.decision6 = pygame.image.load('textbox/decision6.png').convert_alpha()
        self.decision7 = pygame.image.load('textbox/decision7.png').convert_alpha()
        self.decision8 = pygame.image.load('textbox/decision8.png').convert_alpha()

        self.intro_sprite = Intro()

    def run(self):
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
                    if self.start_rect.collidepoint((event.pos)) and not self.game_active:
                        self.game_active = True
                        self.bg_music.stop()
                    elif self.quit_rect.collidepoint((event.pos)) and not self.game_active:
                        pygame.quit()
                        exit()
                    elif self.back_rect.collidepoint(event.pos) and (self.text_box15 or self.phone_activated7 or self.downstair_activated6 or self.level_4 or self.level_5):
                        self.player.rect.x = 200
                        self.run = True
                        self.text_box15 = False
                        self.phone_activated7 = False
                        self.downstair_activated6 = False
                        self.text_box1 = True
                        self.active = True
                        self.canJump = True

                    elif self.phone_rect.collidepoint((event.pos)) and self.level_1:
                        if self.active:
                            self.phone_activated = True
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    self.phone_rect = self.hover_phone.get_rect(midbottom=(1100, 430))
                    self.phone_hovered = self.phone_rect.collidepoint(mouse_pos)
                if event.type == pygame.KEYDOWN and self.Introduction:
                    if event.key == pygame.K_SPACE:
                        if self.text_box1:
                            self.text_box1 = False
                            self.text_box2 = True
                        elif self.text_box2:
                            self.text_box2 = False
                            self.text_box3 = True
                        elif self.text_box3:
                            self.text_box3 = False
                            self.text_box4 = True
                        elif self.text_box4:
                            self.text_box4 = False
                            self.text_box5 = True
                        elif self.text_box5:
                            self.text_box5 = False
                            self.text_box6 = True
                        elif self.text_box7:
                            self.text_box7 = False
                            self.text_box8 = True
                        elif self.text_box8:
                            self.text_box8 = False
                            self.text_box9 = True
                        elif self.text_box9:
                            self.text_box9 = False
                            self.text_box10 = True
                        elif self.text_box10:
                            self.text_box10 = False
                            self.text_box11 = True
                        elif self.text_box11:
                            self.text_box11 = False
                            self.text_box12 = True
                        elif self.text_box12:
                            self.text_box12 = False
                            self.text_box13 = True
                        elif self.text_box13:
                            self.text_box13 = False
                            self.text_box14 = True
                        elif self.text_box14:
                            self.text_box14 = False
                            self.text_box15 = True
                        elif self.text_box16:
                            self.Introduction = False
                            self.level_1 = True

                if event.type == pygame.KEYDOWN and self.level_1:
                    if event.key == pygame.K_SPACE:
                        if self.phone_activated:
                            self.active = False
                            self.phone_activated2 = True
                            self.phone_activated = False
                        elif self.phone_activated3:
                            self.phone_activated4 = True
                            self.phone_activated3 = False
                        elif self.phone_activated4:
                            self.phone_activated5 = True
                            self.phone_activated4 = False
                        elif self.phone_activated5:
                            self.phone_activated6 = True
                            self.phone_activated5 = False
                        elif self.phone_activated6:
                            self.phone_activated7 = True
                            self.phone_activated6 = False

                if event.type == pygame.KEYDOWN and self.level_2:
                    if event.key == pygame.K_SPACE:
                        if self.downstair_activated:
                            self.downstair_activated = False
                            self.downstair_activated2 = True
                        elif self.downstair_activated3:
                            self.downstair_activated3 = False
                            self.downstair_activated4 = True
                        elif self.downstair_activated4:
                            self.downstair_activated4 = False
                            self.downstair_activated5 = True
                        elif self.downstair_activated5:
                            self.downstair_activated5 = False
                            self.downstair_activated6 = True
                        elif self.downstair_activated7:
                            self.downstair_activated7 = False
                            self.downstair_activated8 = True
                        elif self.downstair_activated8:
                            self.downstair_activated8 = False
                            self.downstair_activated9 = True
                        elif self.downstair_activated9:
                            self.player.rect.x = 200
                            self.downstair_activated9 = False
                            self.level_2 = False
                            self.level_3 = True

                if event.type == pygame.KEYDOWN and self.level_4:
                    if event.key == pygame.K_SPACE:
                        if self.downstair_activated10:
                            self.downstair_activated10 = False
                            self.downstair_activated11 = True
                        elif self.downstair_activated11:
                            self.downstair_activated11 = False
                            self.downstair_activated15 = True

                if event.type == pygame.KEYDOWN and self.level_5:
                    if event.key == pygame.K_SPACE:
                        if self.downstair_activated12:
                            self.downstair_activated12 = False
                            self.downstair_activated13 = True
                        elif self.downstair_activated13:
                            self.downstair_activated13 = False
                            self.downstair_activated14 = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_buttons = pygame.mouse.get_pressed()
                    if mouse_buttons[0] == 1:
                        if self.decision1_rect.collidepoint(pygame.mouse.get_pos()) and self.text_box6:
                            self.text_box7 = True
                            self.text_box6 = False
                        elif self.decision2_rect.collidepoint(pygame.mouse.get_pos()) and self.Introduction:
                            self.text_box16 = True
                            self.text_box6 = False
                        elif self.decision3_rect.collidepoint(pygame.mouse.get_pos()) and self.phone_activated2:
                            self.phone_activated = False
                            self.phone_activated2 = False
                            self.active = True
                            self.canJump = True
                            self.player.rect.x = 1000
                        elif self.decision4_rect.collidepoint(pygame.mouse.get_pos()) and self.phone_activated2
