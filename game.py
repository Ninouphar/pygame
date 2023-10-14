import pygame
from sys import exit

def display_score():

    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'{current_time}', False, (255,215,0))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('The Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('Early_GameBoy.ttf', 50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('Sky.png').convert()

ground_surface = pygame.image.load('ground.png').convert()
ground_rect = ground_surface.get_rect(topleft = (0,300))

snail_surface = pygame.image.load('snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600, 300))

game_name = test_font.render('Pixel runner', False, (244,237,222))
game_name = pygame.transform.rotozoom(game_name, 0, 0.5)
game_name_rect = game_name.get_rect(center = (400, 70))

player_surf = pygame.image.load('player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0
player_stand = pygame.image.load('player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_message = test_font.render('Press space to run', False, (244,237,222))
game_message = pygame.transform.rotozoom(game_message, 0, 0.4)
game_message_rect = game_message.get_rect(center = (400,350))


obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)


while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEMOTION:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    player_gravity = -25
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= 300:
                        player_gravity = -23
        else:
            start_time = int(pygame.time.get_ticks() / 1000)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    snail_rect.left = 800
                    game_active = True

        if event.type == obstacle_timer:
            print('test')


    if game_active: 
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, ground_rect)
        # screen.blit(score_surf, (220,45))

        score = display_score()

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
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)

        score_message = test_font.render(f'Your score: {score}', False, (244,237,222))
        score_message = pygame.transform.rotozoom(score_message, 0, 0.5)
        score_message_rect = score_message.get_rect(center = (400,330))

        screen.blit(game_name, game_name_rect)

        if score == 0:
            screen.blit(game_message, game_message_rect)
        else:
            screen.blit(score_message, score_message_rect)
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_SPACE]:
    #     print('jump')
    # if (player_rect.colliderect(snail_rect)):

    # if(player_rect.collidepoint(mouse_pos)):
    #     print(pygame.mouse.get_pressed())
        

    pygame.display.update()
    clock.tick(60)