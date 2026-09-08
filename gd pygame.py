import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Test de mouvement du joueur")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
game_state = "menu"

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.040)

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
        title = font_title.render("PAC MAN", True, (240, 255, 0))
        screen.blit(title, (screen.get_width() / 2 - title.get_width() / 2, 100))

        # Bouton Play
        play_button = pygame.Rect(540, 350, 200, 80)
        pygame.draw.rect(screen, (240, 255, 0), play_button)

        font_button = pygame.font.Font(None, 50)
        text_play = font_button.render("PLAY", True, (0, 0, 0))

        text_rect = text_play.get_rect(center=play_button.center)
        screen.blit(text_play, text_rect)

    elif game_state == "game":

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player_pos.x -= 10

        if keys[pygame.K_RIGHT]:
            player_pos.x += 10

        if player_pos.x < 20:
            player_pos.x = 20

        if player_pos.x > screen.get_width() - 20:
            player_pos.x = screen.get_width() - 20

        pygame.draw.circle(
            screen,
            (240, 255, 0),
            (int(player_pos.x), int(player_pos.y)),
            20
        )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()