import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jet Plane Bombing Animation Game")

# handling images
background_img = pygame.image.load('bombing_bg.jpg').convert()
jet_img = pygame.image.load('fighterjet.png').convert_alpha()
bomb_img = pygame.image.load('bomb.png').convert_alpha()
explosion_img = pygame.image.load('explosion.png').convert_alpha()
house_img = pygame.image.load('house.png').convert_alpha()
explosion_sound = pygame.mixer.Sound('explosion_sound1.mp3')

background_img = pygame.transform.scale(background_img, (800, 600))
jet_img = pygame.transform.scale(jet_img, (200, 100))
bomb_img = pygame.transform.scale(bomb_img, (60, 60))
house_img = pygame.transform.scale(house_img, (300, 250))
explosion_img = pygame.transform.scale(explosion_img, (340, 200))


# Object attributes
jet_x = WIDTH // 2 - 50  
jet_y = 50
jet_speed = 18

bomb_x = 0
bomb_y = 0
bomb_speed = 10
bomb_dropped = False

explosion_x = 0
explosion_y = 0
explosion_timer = 0

score = 0

houses = []

def generate_houses():
    global houses
    houses = []
    for _ in range(random.randint(2, 3)):
        house_x = random.randint(50, WIDTH - 250)
        house_y = HEIGHT - 250
        houses.append((house_x, house_y))

generate_houses()

running = True

while running:
    screen.blit(background_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not bomb_dropped:
                bomb_x = jet_x + 50
                bomb_y = jet_y + 100
                bomb_dropped = True

    jet_x += jet_speed

    if jet_x > WIDTH:
        jet_x = -jet_img.get_width()

    if bomb_dropped:
        bomb_y += bomb_speed
        if bomb_y > HEIGHT:
            bomb_dropped = False


    for house_x, house_y in houses:
        if 200 < bomb_y < 400:
            if house_x < bomb_x < house_x + 200 and house_y < bomb_y < house_y + 200:
                explosion_x = bomb_x
                explosion_y = bomb_y
                explosion_timer = 30
                bomb_dropped = False
                score += 1
                generate_houses()
                explosion_sound.play()



    # Showing objects

    screen.blit(jet_img, (jet_x, jet_y))

    if bomb_dropped:
        screen.blit(bomb_img, (bomb_x, bomb_y))

    if explosion_timer > 0:
        screen.blit(explosion_img, (explosion_x, explosion_y))
        explosion_timer -= 1

    for house_x, house_y in houses:
        screen.blit(house_img, (house_x, house_y))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

    pygame.time.Clock().tick(30)

pygame.quit()
