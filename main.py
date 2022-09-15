import pygame
import sys
import random
pygame.init()
clock = pygame.time.Clock()

# Shooter


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


# Target
# Screen
width = 1600
height = 720
screen = pygame.display.set_mode((width, height))
pygame.mouse.set_visible(False)
backgorund = pygame.image.load("bg_blue-big.png")


# Crosshair group
crosshair = crosshair("crosshair_red_large.png", "10 Guage Shotgun.wav")
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Targets_group

targets_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target("target_red3.png", random.randrange(
        0, width), random.randrange(0, height))
    targets_group.add(new_target)


Game_Active = True
while Game_Active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shooting()
    screen.blit(backgorund, (0, 0))
    targets_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    pygame.display.update()
    clock.tick(120)
