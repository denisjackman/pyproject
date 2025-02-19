'''
    This is a Sprite checking utility

    Notes:
    The tiles are 16 x 16px and have a 1px margin between them.

    ---

    TILE SIZE: 16 x 16
    MARGIN:	   1

    Sheets:
    Z:/Resources/roguelike/Spritesheet/rogueLikeChar_Transparent.png
    Z:/Resources/roguelike/Spritesheet/rogueLikeCity_Transparent.png
    Z:/Resources/roguelike/Spritesheet/roguelikeDungeon_transparent.png
    Z:/Resources/roguelike/Spritesheet/rogueLikeSheet_Transparent.png
'''
from pathlib import Path
import pygame

WIDTH = 800
HEIGHT = 800
CAPTION = "Jackmanimation [SpriteSheet]"
ICON_FILE = 'y:/Resources/jackmanimation.png'
WHITE = (255, 255, 255)
FILEPATH = Path(__file__).parent
SHEET_NAME = "Z:/Resources/roguelike/Spritesheet/rogueLikeSheet_Transparent.png"

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(CAPTION)
pygame_icon = pygame.image.load(ICON_FILE)
pygame.display.set_icon(pygame_icon)
SPRITE_SHEET = pygame.image.load(SHEET_NAME).convert_alpha()
SPRITE_SHEET_WIDTH = SPRITE_SHEET.get_width()
SPRITE_SHEET_HEIGHT = SPRITE_SHEET.get_height()

SPRITES = []


def load_sprites():
    ''' load sprites from sprite sheet'''
    sx = 0
    sy = 0
    swidth = 16
    sheight = 16
    totalwidth = 0
    totalheight = 0
    while totalheight + sheight < SPRITE_SHEET_HEIGHT:
        while totalwidth + swidth < SPRITE_SHEET_WIDTH:
            asset = SPRITE_SHEET.subsurface((sx, sy, swidth, sheight))
            asset = pygame.transform.scale(asset, (64, 64))
            SPRITES.append(asset)
            sx += 17
            totalwidth += 17
        sx = 0
        sy += 17
        totalwidth = 0
        totalheight += 17


def tool_main():
    ''' main routine '''
    load_sprites()
    done = False
    clock = pygame.time.Clock()
    sprite_index = 0
    while not done:
        clock.tick(240)
        title_caption = f"Jackmanimation [SpriteSheet] Sprite: {sprite_index}"
        pygame.display.set_caption(title_caption)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                sprite_index += 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    sprite_index += 1
                elif event.key == pygame.K_LEFT:
                    sprite_index -= 1
        if sprite_index >= len(SPRITES):
            sprite_index = 0
        if sprite_index < 0:
            sprite_index = len(SPRITES) - 1
        window.fill((WHITE))
        window.blit(SPRITES[sprite_index], (WIDTH/2 - 8, HEIGHT/2 - 8))
        pygame.display.update()


def save_sprites():
    ''' save sprites to file '''
    for index, sprite in enumerate(SPRITES):
        pygame.image.save(sprite,
                          f"{FILEPATH}/sprites/RLS_sprite_{index:04}.png")
    print(f"Done! {len(SPRITES)} sprites saved.")


def tool_finish():
    ''' finish routine '''
    pygame.quit()


if __name__ == '__main__':
    tool_main()
    save_sprites()
    tool_finish()
