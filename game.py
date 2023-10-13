import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((805,450))
pygame.display.set_caption('Game of Life')
clock = pygame.time.Clock()
test_font = pygame.font.Font('/mnt/nfs/homes/rraffi-k/python/Early_GameBoy.ttf', 50)

sky_surface = pygame.image.load('/mnt/nfs/homes/rraffi-k/Pictures/Screenshots/gamepy.png').convert()

ground_surface = pygame.image.load('/mnt/nfs/homes/rraffi-k/Pictures/Screenshots/ground.png').convert()
ground_rect = ground_surface.get_rect(topleft = (0,424))
text_surface = test_font.render('THE GAME', False, (254,254,226))

snail_surface = pygame.image.load('/mnt/nfs/homes/rraffi-k/Pictures/Screenshots/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(topleft = (805, 388))

player_surf = pygame.image.load('/mnt/nfs/homes/rraffi-k/Pictures/Screenshots/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (0,424))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEMOTION:
        #     if player_rect.collidepoint(event.pos):
        #         print("C'EST MOI QUI AI TUE MUFASA")
        # if event.type == pygame.KEYDOWN:
        #     print('down')
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print('up')
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, ground_rect)
    screen.blit(text_surface, (220,45))

    snail_rect.x -= 2;
    if snail_rect.right < 0: snail_rect.left = 805;

    mouse_pos = pygame.mouse.get_pos()
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surf, player_rect)
    player_rect.left += 1

    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')
    # if (player_rect.colliderect(snail_rect)):

    # if(player_rect.collidepoint(mouse_pos)):
    #     print(pygame.mouse.get_pressed())
        

    pygame.display.update()
    clock.tick(60)
