import pygame
import sys
import random
pygame.init()
clock = pygame.time.Clock()
Font= pygame.font.SysFont('Calibri', 75, True, False)
Sound=pygame.mixer.Sound('Dark_Rainy_Night(ambience).ogg')
# Screen
width = 1600
height = 900
screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(False)
backgorund = pygame.image.load("bg_blue-big.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


class button():
     
    def __init__(self,image, pos, text_input,font, base_color,hovering_color):

        self.image=image
        self.x_pos=pos[0]
        self.y_pos=pos[1]
        self.font=font
        self.base_color,self.hovering_color=base_color, hovering_color
        self.text_input=text_input
        self.text= self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image=self.text
        self.rect=self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect=self.text.get_rect(center=(self.x_pos, self.y_pos))

    
    def checkforinputs(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)


    def changecolor(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text=self.font.render(self.text_input, True,self.hovering_color)

        else:
            self.text=self.font.render(self.text_input, True, self.base_color)
class crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path, sound_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound(sound_path)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()

    def shooting(self):
        self.sound.play()
        pygame.sprite.spritecollide(crosshair, targets_group, True)

class Target(pygame.sprite.Sprite):
    def __init__(self, picture_path, x, y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

# Crosshair group
crosshair = crosshair("crosshair_red_large.png", "10 Guage Shotgun.wav")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Targets_group
targets_group = pygame.sprite.Group()
for target in range(10):
    new_target = Target("duck_yellow.png", random.randrange(
        0, width), random.randrange(0, height))
    targets_group.add(new_target)

def options(): 
    while True:
        screen.fill('black')
        mouse_p=pygame.mouse.get_pos() 
        screen.blit(backgorund,(0,0))

        OPTIONS_TEXT = get_font(100).render("Options", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(750, 100))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        button_1=button(None, pos=(750,300), text_input="Sound Level", font=get_font(75),base_color='#142565',hovering_color='red')
        button_2=button(None, pos=(750,400), text_input="Controls", font=get_font(75),base_color='#142565',hovering_color='red')
        button_3= button(None, pos=(750,500), text_input="Backgound", font=get_font(75),base_color='#142565',hovering_color='red')
        button_4= button(None, pos=(750,700), text_input="Back", font=get_font(75),base_color='#142565',hovering_color='red')

        for buttonss in [button_1, button_2,button_3, button_4]:
                    buttonss.changecolor(mouse_p)
                    buttonss.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()            
            if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                        if button_1.checkforinputs(mouse_p):
                            print('1')
                        if button_2.checkforinputs(mouse_p):
                            print('2')
                        if button_3.checkforinputs(mouse_p):
                            print('3')
                        if button_4.checkforinputs(mouse_p):
                           menu()
        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.update()                       

    
        

def Active():
    screen.fill('black')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                crosshair.shooting()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        screen.blit(backgorund,(0,0))
        OPTIONS_TEXT = get_font(20).render("No Ducks were hurt in the process of making this game", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(750, 870))
        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)
        targets_group.draw(screen)
        crosshair_group.draw(screen)
        crosshair_group.update()
        if len(targets_group.sprites()) == 0:
            menu()
        
        pygame.display.update()


game_on = True
Game_Active = True
click = False
def menu():
    Sound.play(-1)
    while Game_Active:
        
        screen.blit(backgorund,(0,0))
        mouse_pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if button1.checkforinputs(mouse_pos):
                    options()
                    
                if button2.checkforinputs(mouse_pos):
                    for target in range(20):
                        new_target = Target("duck_yellow.png", random.randrange(
                             0, width), random.randrange(0, height))
                        targets_group.add(new_target)
                    Active()

                if button3.checkforinputs(mouse_pos):
                        pygame.quit()
                        sys.exit()
        button1=button(None, pos=(750,400), text_input="options", font=get_font(75),base_color='#142565',hovering_color='red')
        button2=button(None, pos=(750,150), text_input="Play", font=get_font(75),base_color='#142565',hovering_color='red')
        button3= button(None, pos=(750,600), text_input="Quit", font=get_font(75),base_color='#142565',hovering_color='red')
        for buttons in [button1, button2,button3]:
            buttons.changecolor(mouse_pos)
            buttons.update(screen)
        

        crosshair_group.draw(screen)
        crosshair_group.update()
        pygame.display.update()
        clock.tick(120)


print('its working')
menu()   