import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Projet Yellow")
screen = pygame.display.set_mode((1000, 720))
clock = pygame.time.Clock()
running = True
dt = 0
game_state = "menu"
player_lives = 3
player_img = pygame.image.load("assets/yellow.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))
player_img_left = pygame.transform.flip(player_img, True, False)
player_img_right = player_img

player_pos = pygame.Vector2(
    screen.get_width() / 2,
    screen.get_height() / 1.040
    )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_state == "menu":
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    game_state = "game"
    screen.fill((0, 0, 0, 0))  # Remplir l'écran avec du noir

    if game_state == "menu":
        # Titre
        font_title = pygame.font.Font(None, 80)
        title = font_title.render("PROJET YELLOW", True, (240, 255, 0))
        screen.blit(title, (screen.get_width() / 2 - title.get_width() / 2, 100))

        # Bouton Play
        play_button = pygame.Rect(400, 350, 200, 80)
        pygame.draw.rect(screen, (240, 255, 0), play_button)

        font_button = pygame.font.Font(None, 50)
        text_play = font_button.render("PLAY", True, (0, 0, 0))

        text_rect = text_play.get_rect(center=play_button.center)
        screen.blit(text_play, text_rect)

    elif game_state == "game":

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_pos.x -= 10
            player_img = player_img_left

        if keys[pygame.K_RIGHT]:
            player_pos.x += 10
            player_img = player_img_right

        if player_pos.x < 25:
            player_pos.x = 25

        if player_pos.x > screen.get_width() - 25:
            player_pos.x = screen.get_width() - 25

        screen.blit(
        player_img,
        (int(player_pos.x - 25), int(player_pos.y - 25))
        )  

        # Affichage du nombre de vies
        font = pygame.font.Font(None, 40)
        lives_text = font.render("Vies : " + str(player_lives), True, (255, 255, 255))
        screen.blit(lives_text, (20, 20))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()