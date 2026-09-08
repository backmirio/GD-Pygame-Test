import pygame
import random

pygame.init()

pygame.display.set_caption("Projet Yellow")

screen = pygame.display.set_mode((1000, 900))

clock = pygame.time.Clock()

running = True

game_state = "menu"

player_lives = 3
invincible_timer = 0
invincible_duration = 1.5

player_speed = 700
shot_speed = 700
shot_timer = 0
shot_delay = 0.2

green_speed = 150
green_timer = 0
green_delay = 1

greens = []

player_img = pygame.image.load("assets/yellow.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))

player_img_left = pygame.transform.flip(player_img, True, False)
player_img_right = player_img

green_img = pygame.image.load("assets/green.png").convert_alpha()
green_img = pygame.transform.scale(green_img, (50, 50))

heart_img = pygame.image.load("assets/heart.png").convert_alpha()
heart_img = pygame.transform.scale(heart_img, (30, 30))

player_shots = []

player_pos = pygame.Vector2(
    screen.get_width() / 2,
    screen.get_height() / 1.040
)

while running:

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if game_state == "menu":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if play_button.collidepoint(event.pos):
                    game_state = "game"

    screen.fill((0, 0, 0))

    if game_state == "menu":

        font_title = pygame.font.Font(None, 80)

        title = font_title.render(
            "PROJET YELLOW",
            True,
            (240, 255, 0)
        )

        screen.blit(
            title,
            (
                screen.get_width() / 2 - title.get_width() / 2,
                100
            )
        )

        play_button = pygame.Rect(
            400,
            350,
            200,
            80
        )

        pygame.draw.rect(
            screen,
            (240, 255, 0),
            play_button
        )

        font_button = pygame.font.Font(None, 50)

        text_play = font_button.render(
            "PLAY",
            True,
            (0, 0, 0)
        )

        text_rect = text_play.get_rect(
            center=play_button.center
        )

        screen.blit(
            text_play,
            text_rect
        )

    elif game_state == "game":

        keys = pygame.key.get_pressed()

        if invincible_timer > 0:
            invincible_timer -= dt

        if player_lives <= 0:
            game_state = "game_over"

        if keys[pygame.K_LEFT]:
            player_pos.x -= player_speed * dt
            player_img = player_img_left

        if keys[pygame.K_RIGHT]:
            player_pos.x += player_speed * dt
            player_img = player_img_right

        if player_pos.x < 25:
            player_pos.x = 25

        if player_pos.x > screen.get_width() - 25:
            player_pos.x = screen.get_width() - 25

        green_timer += dt

        if green_timer >= green_delay:

            greens.append({
                "pos": pygame.Vector2(
                    random.randint(
                        25,
                        screen.get_width() - 25
                    ),
                    50
                ),
                "hp": 3
            })

            green_timer = 0

        shot_timer += dt

        if keys[pygame.K_SPACE] and shot_timer >= shot_delay:

            player_shots.append(
                pygame.Rect(
                    int(player_pos.x - 3),
                    int(player_pos.y - 30),
                    6,
                    15
                )
            )

            shot_timer = 0

        for shot in player_shots:

            shot.y -= shot_speed * dt

            pygame.draw.rect(
                screen,
                (240, 255, 0),
                shot
            )

        for green in greens:

            green["pos"].y += green_speed * dt

            green_rect = green_img.get_rect(
                center=(
                    int(green["pos"].x),
                    int(green["pos"].y)
                )
            )

            if green_rect.colliderect(player_img.get_rect(
                center=(int(player_pos.x), int(player_pos.y))
            )) and invincible_timer <= 0:
                
                player_lives -= 1
                invincible_timer = invincible_duration
                greens.remove(green)
                break

            screen.blit(
                green_img,
                (
                    int(green["pos"].x - 25),
                    int(green["pos"].y - 25)
                )
            )

            screen.blit(
                green_img,
                (
                    int(green["pos"].x - 25),
                    int(green["pos"].y - 25)
                )
            )

            pygame.draw.rect(
                screen,
                (100, 100, 100),
                (
                    int(green["pos"].x - 25),
                    int(green["pos"].y - 35),
                    50,
                    5
                )
            )

            pygame.draw.rect(
                screen,
                (0, 255, 0),
                (
                    int(green["pos"].x - 25),
                    int(green["pos"].y - 35),
                    int(50 * (green["hp"] / 3)),
                    5
                )
            )

            for shot in player_shots:

                if green_rect.colliderect(shot):

                    green["hp"] -= 1
                    player_shots.remove(shot)

                    break

        greens_to_remove = []

        for green in greens:

            if green["pos"].y > screen.get_height() + 25:
                player_lives -= 1
                greens_to_remove.append(green)

            elif green["hp"] <= 0:
                greens_to_remove.append(green)

        for green in greens_to_remove:
            greens.remove(green)

        player_shots = [
            shot
            for shot in player_shots
            if shot.bottom > 0
        ]

        screen.blit(
            player_img,
            (
                int(player_pos.x - 25),
                int(player_pos.y - 25)
            )
        )

        for i in range(player_lives):

            screen.blit(
                heart_img,
                (
                    20 + i * 40,
                    10
                )
            )

    elif game_state == "game_over":

        font_game_over = pygame.font.Font(None, 100)

        game_over_text = font_game_over.render(
            "GAME OVER",
            True,
            (240, 255, 0)
        )

        screen.blit(
            game_over_text,
            (
                screen.get_width() / 2 - game_over_text.get_width() / 2,
                200
            )
        )

        restart_button = pygame.Rect(
            400,
            350,
            200,
            80
        )

        pygame.draw.rect(
            screen,
            (240, 255, 0),
            restart_button
        )

        font_button = pygame.font.Font(None, 50)

        restart_text = font_button.render(
            "RESTART",
            True,
            (0, 0, 0)
        )

        restart_text_rect = restart_text.get_rect(
            center=restart_button.center
        )

        screen.blit(
            restart_text,
            restart_text_rect
        )

        if game_state == "game_over":

            if event.type == pygame.MOUSEBUTTONDOWN:

                if restart_button.collidepoint(event.pos):

                    game_state = "game"
                    player_lives = 3
                    greens.clear()
                    player_shots.clear()
                    invincible_timer = 0
    pygame.display.flip()

pygame.quit()
