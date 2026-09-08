import pygame

pygame.init()
pygame.font.init()
pygame.display.set_caption("Test de mouvement du joueur")
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 1.040)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0, 0))  # Remplir l'écran avec du noir

    pygame.draw.circle(screen, (240,255,0), (int(player_pos.x), int(player_pos.y)), 20)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos.x -= 5
    if keys[pygame.K_RIGHT]:
        player_pos.x += 5
    pygame.display.flip()   # Met à jour l'affichage
    dt = clock.tick(60) / 1000

pygame.quit()