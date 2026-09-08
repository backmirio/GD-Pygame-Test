import pygame
import random

pygame.init()

pygame.display.set_caption("Yellow")

screen = pygame.display.set_mode((1000, 900))

clock = pygame.time.Clock()

running = True

game_state = "menu"

player_lives = 3
score = 0
invincible_timer = 0
invincible_duration = 1.5

player_speed = 700
shot_speed = 700
shot_timer = 0
shot_delay = 0.2

green_speed = 75
green_timer = 0
green_delay = 1.25

blue_speed = 100
blue_timer = 0
blue_delay = 2.5

red_speed = 85
red_timer = 0
red_delay = 3.5

greens = []
blues = []
reds = []

player_img = pygame.image.load("assets/yellow.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (50, 50))

player_img_left = pygame.transform.flip(player_img, True, False)
player_img_right = player_img

green_img = pygame.image.load("assets/green.png").convert_alpha()
green_img = pygame.transform.scale(green_img, (50, 50))

blue_img = pygame.image.load("assets/blue.png").convert_alpha()
blue_img = pygame.transform.scale(blue_img, (50, 50))

red_img = pygame.image.load("assets/red.png").convert_alpha()
red_img = pygame.transform.scale(red_img, (50, 50))

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
            "YELLOW",
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

        blue_timer += dt

        if blue_timer >= blue_delay:

            blues.append({
                "pos": pygame.Vector2(
                    random.randint(
                        25,
                        screen.get_width() - 25
                    ),
                    50
                ),
                "hp": 2
            })

            blue_timer = 0

        red_timer += dt

        if red_timer >= red_delay:

            reds.append({
                "pos": pygame.Vector2(
                    random.randint(
                        25,
                        screen.get_width() - 25
                    ),
                    50
                ),
                "hp": 1
            })

            red_timer = 0

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

        for blue in blues:

            blue["pos"].y += blue_speed * dt

            blue_rect = blue_img.get_rect(
                center=(
                    int(blue["pos"].x),
                    int(blue["pos"].y)
                )
            )

            if blue_rect.colliderect(player_img.get_rect(
                center=(int(player_pos.x), int(player_pos.y))
            )) and invincible_timer <= 0:
                
                player_lives -= 1
                invincible_timer = invincible_duration
                blues.remove(blue)
                break

            screen.blit(
                blue_img,
                (
                    int(blue["pos"].x - 25),
                    int(blue["pos"].y - 25)
                )
            )

            pygame.draw.rect(
                screen,
                (0, 100, 255),
                (
                    int(blue["pos"].x - 25),
                    int(blue["pos"].y - 35),
                    int(50 * (blue["hp"] / 2)),
                    5
                )
            )

            for shot in player_shots:

                if blue_rect.colliderect(shot):

                    blue["hp"] -= 1
                    player_shots.remove(shot)

                    break
        
        greens_to_remove = []
        blues_to_remove = []
        reds_to_remove = []

        for blue in blues:

            if blue["pos"].y > screen.get_height() + 25:
                player_lives -= 1
                blues_to_remove.append(blue)

            elif blue["hp"] <= 0:
                score += 25
                blues_to_remove.append(blue)

        for blue in blues_to_remove:
            blues.remove(blue)

        for red in reds:
            red["pos"].y += red_speed * dt

            red_rect = red_img.get_rect(
                center=(
                    int(red["pos"].x),
                    int(red["pos"].y)
                )
            )

            if red_rect.colliderect(player_img.get_rect(
                center=(int(player_pos.x), int(player_pos.y))
            )):
                
                player_lives -= 1
                reds.remove(red)
                break

            for shot in player_shots:
                
                if red_rect.colliderect(shot):
                    red["hp"] -= 1
                    player_shots.remove(shot)
                    break

            screen.blit(red_img, red_rect)

            pygame.draw.rect(
                screen,
                (100, 0, 0),
                (
                    int(red["pos"].x - 25),
                    int(red["pos"].y - 35),
                    50,
                    5
                )
            )

            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (
                    int(red["pos"].x - 25),
                    int(red["pos"].y - 35),
                    int(50 * (red["hp"] / 1)),
                    5
                )
            )

        for red in reds:
            if red["pos"].y > screen.get_height() + 25:
                player_lives -= 1
                reds_to_remove.append(red)

            elif red["hp"] <= 0:
                score += 75
                reds_to_remove.append(red)

        for red in reds_to_remove:
            reds.remove(red)


        for green in greens:

            if green["pos"].y > screen.get_height() + 25:
                player_lives -= 1
                greens_to_remove.append(green)

            elif green["hp"] <= 0:
                score += 50
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

        score_text = font_button.render(
            f"Score: {score}",
            True,
            (240, 255, 0)
        )

        screen.blit(
            score_text,
            (
                screen.get_width() - score_text.get_width() - 20,
                10,
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
                    score = 0
                    greens.clear()
                    blues.clear()
                    reds.clear()
                    player_shots.clear()

                    player_pos.x = screen.get_width() / 2
                    player_pos.y = screen.get_height() / 1.040

                    green_timer = 0
                    blue_timer = 0
                    red_timer = 0
                    
                    invincible_timer = 0
    pygame.display.flip()

pygame.quit()
