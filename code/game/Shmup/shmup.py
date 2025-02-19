#!/usr/bin/env python
'''
    shmup py game
'''
import random
import os
import pygame

# Basic Constants
WIDTH = 480
HEIGHT = 600
FPS = 60
CAPTION = "Shmup"
POWERUP_TIME = 5000

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up assets folders
IMG_DIR = 'Z:/Resources/development/shmup/img'
SND_DIR = 'Z:/Resources/development/shmup/snd'

# set up the screen using WIDTH and HEIGHT
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Display the CAPTION
pygame.display.set_caption(CAPTION)

# set the game clock running
clock = pygame.time.Clock()

# initialise pygame main game engine
pygame.init()
# initialise pygame sound engine
pygame.mixer.init()

# load game images
player_img = pygame.image.load(os.path.join(IMG_DIR, "player.png")).convert()
player_mini_img = pygame.transform.scale(player_img, (25, 19))
player_mini_img.set_colorkey(BLACK)

meteor_img = pygame.image.load(os.path.join(IMG_DIR, "meteorSmall.png")).convert()
bullet_img = pygame.image.load(os.path.join(IMG_DIR, "laserRed.png")).convert()
meteor_images = []
meteor_list = ["meteorBrown_big1.png", "meteorBrown_big2.png",
               "meteorBrown_big3.png", "meteorBrown_big4.png",
               "meteorBrown_med1.png", "meteorBrown_med3.png",
               "meteorBrown_small1.png", "meteorBrown_small2.png",
               "meteorBrown_tiny1.png", "meteorBrown_tiny2.png"]
for img in meteor_list:
    meteor_images.append(pygame.image.load(os.path.join(IMG_DIR, img)).convert())

explosion_anim = {}
explosion_anim['lg'] = []
explosion_anim['sm'] = []
explosion_anim['player'] = []

for item in range(9):
    FILENAME = f'regularExplosion0{item}.png'
    img = pygame.image.load(os.path.join(IMG_DIR, FILENAME)).convert()
    img.set_colorkey(BLACK)
    img_lg = pygame.transform.scale(img, (75, 75))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (32, 32))
    explosion_anim['sm'].append(img_sm)
    FILENAME = f'sonicExplosion0{item}.png'
    img = pygame.image.load(os.path.join(IMG_DIR, FILENAME)).convert()
    img.set_colorkey(BLACK)
    explosion_anim['player'].append(img)


powerup_images = {}
powerup_images['shield'] = pygame.image.load(os.path.join(IMG_DIR, 'shield_gold.png')).convert()
powerup_images['gun'] = pygame.image.load(os.path.join(IMG_DIR, 'bolt_gold.png')).convert()
powerups = pygame.sprite.Group()

# set up sounds
# Load all game sounds
shoot_sound = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
expl_sounds = []
for snd in ['expl3.wav', 'expl6.wav']:
    expl_sounds.append(pygame.mixer.Sound(os.path.join(SND_DIR, snd)))
pygame.mixer.music.load(os.path.join(SND_DIR, 'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)

# set up sprite groups
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
font_name = pygame.font.match_font('arial')


def newmob():
    '''
        new mob
    '''
    if len(mobs) < 8:
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)


def draw_text(surf, text, size, x, y):
    '''
        draw text
    '''
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


def draw_shield_bar(surf, x, y, pct):
    '''
        draw shield bar
    '''
    pct = max(pct, 0)
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = pct
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_lives(surf, x, y, lives, img_life):
    '''
        draw lives
    '''
    for item_lives in range(lives):
        img_rect = img_life.get_rect()
        img_rect.x = x + 30 * item_lives
        img_rect.y = y
        surf.blit(img_life, img_rect)


class Player(pygame.sprite.Sprite):
    '''
        player class
    '''
    # initialise the class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.bottom = HEIGHT - 10
        self.radius = 20
        self.speedx = 0
        self.shield = 100
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()

    def update(self):
        '''
            update method
        '''
        # Move the player
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.right = min(self.rect.right, WIDTH)
        self.rect.left = max(self.rect.left, 0)
        self.rect.x += self.speedx
        # Shoot the gun
        if keystate[pygame.K_SPACE]:
            self.shoot()
            # unhide if hidden

        if self.hidden and (pygame.time.get_ticks() - self.hide_timer) > 1000:
            self.hidden = False
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

    def shoot(self):
        '''
            Define the method for handling shooting
        '''
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        '''
            hide the player temporarily
        '''
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (WIDTH / 2, HEIGHT + 200)

    def powerup(self):
        '''
            power up
        '''
        self.power += 1
        self.power_time = pygame.time.get_ticks()


class Mob(pygame.sprite.Sprite):
    '''
        Enemy Class
    '''

    # initialise the class
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)
        self.radius = int(self.rect.width * .8 / 2)
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def rotate(self):
        '''
            rotate
        '''
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.last_update = now
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    # Define the method for the update
    def update(self):
        '''
            update
        '''
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > HEIGHT + 10 or self .rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)


class Bullet(pygame.sprite.Sprite):
    '''
        bullet class
    '''
    # initialise the class
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        '''
            Define the method for the update
        '''
        self.rect.y += self.speedy
        # kill it if it moves off the top of the screen
        if self.rect.bottom < 0:
            self.kill()

    def current_speed(self):
        '''
            return current speed
        '''
        return self.speedy


class Explosion(pygame.sprite.Sprite):
    '''
        explosion
    '''
    def __init__(self, center, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.image = explosion_anim[self.size][0]
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 50

    def update(self):
        '''
            update method
        '''
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim[self.size]):
                self.kill()
            else:
                center = self.rect.center
                self.image = explosion_anim[self.size][self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

    def current_frame_rate(self):
        '''
            current frame rate
        '''
        return self.frame_rate


class PowPow(pygame.sprite.Sprite):
    '''
        POW class
    '''
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield', 'gun'])
        self.image = powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 2

    def update(self):
        '''
            update method
        '''
        self.rect.y += self.speedy
        # kill if it moves off the bottom of the screen
        if self.rect.top > HEIGHT:
            self.kill()

    def current_speed(self):
        '''
            return current speed
        '''
        return self.speedy


def main():
    '''
        Main game routine
    '''
    # initialise pygame and set up the screen
    game_over = True
    running = True
    # load all background graphics
    background = pygame.image.load(os.path.join(IMG_DIR,
                                                "starBackground.png")).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background_rect = background.get_rect()

    # initialise the player
    player = Player()
    all_sprites.add(player)
    score = 0
    pygame.mixer.music.play(loops=-1)
    # add the mobs
    for game_item in range(8):
        newmob()

    # main game loop
    while running:
        if game_over:
            show_go_screen()

        # keep loop running at the right speed
        clock.tick(FPS)
        # process input
        for event in pygame.event.get():
            # check for closing the window
            if event.type == pygame.QUIT:
                running = False
        # update
        all_sprites.update()
        # check to see if a mob hits the player
        hits = pygame.sprite.spritecollide(player,
                                           mobs,
                                           False,
                                           pygame.sprite.collide_circle)
        for hit in hits:
            player.shield -= 1
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
        if player.shield <= 0:
            death_explosion = Explosion(player.rect.center, 'player')
            all_sprites.add(death_explosion)
            player.hide()
            player.lives -= 1
            player.shield = 100

        # if the player died and the explosion has finished playing
        if player.lives == 0 and not death_explosion.alive():
            running = False

        # check to see if a bullet hits a mob
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 1
            newmob()
            random.choice(expl_sounds).play()
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            if random.random() > 0.9:
                powpow = PowPow(hit.rect.center)
                all_sprites.add(powpow)
                powerups.add(powpow)
            newmob()

        # check to see if player hit a powerup
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.type == 'shield':
                player.shield += random.randrange(10, 30)
                player.shield = min(player.shield, 100)
            if hit.type == 'gun':
                player.powerup()

        # render
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        # flip the display always do this last
        pygame.display.flip()

    pygame.quit()


def show_go_screen():
    '''
        show go screen
    '''


if __name__ == "__main__":
    # TODO: add a title screen
    # TODO: add credits screen
    # TODO: add sound
    # TODO: extra stuff
    # run the main routine
    main()
