import pygame
from sys import exit

def display_score():
    current_time = pygame.time.get_ticks()
    print(current_time)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('The Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Early_GameBoy.ttf', 50)
game_active = True

sky_surface = pygame.image.load('Sky.png').convert()

# score_surf = test_font.render('THE GAME', False, (254,254,226))
# score_rect = score_surf.get_rect(center = (400,50))

ground_surface = pygame.image.load('ground.png').convert()
ground_rect = ground_surface.get_rect(topleft = (0,300))
# text_surface = test_font.render('THE GAME', False, (254,254,226))

snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))


player_surf = pygame.image.load('player_stand.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEMOTION:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snail_rect.left = 800
                    game_active = True

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, ground_rect)
        # screen.blit(score_surf, (220,45))

        display_score()

        snail_rect.x -= 4;
        if snail_rect.right < 0: 
            snail_rect.left = 800;
        screen.blit(snail_surface, snail_rect)

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        if snail_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill('Yellow')
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')
    # if (player_rect.colliderect(snail_rect)):

    # if(player_rect.collidepoint(mouse_pos)):
    #     print(pygame.mouse.get_pressed())
        

    pygame.display.update()
    clock.tick(60)