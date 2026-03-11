import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Движение паука")

spider_image = pygame.image.load("spider.png")
spider_rect = spider_image.get_rect()
spider_width, spider_height = spider_rect.size

speed_x = 2
speed_y = 2
x, y = 0, 0
direction_x, direction_y = 1, 0  # Начальное направление движения вправо

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y = HEIGHT - spider_height
            elif event.key == pygame.K_ESCAPE:
                y = 0
            elif event.key == pygame.K_KP_ENTER:
                x = WIDTH - spider_width
            elif event.key == pygame.K_BACKSPACE:
                x = 0
            elif event.key == pygame.K_1:
                x, y = WIDTH // 2 - spider_width // 2, HEIGHT // 2 - spider_height // 2

    x += speed_x * direction_x
    y += speed_y * direction_y

    if x + spider_width > WIDTH:
        x = 0
        y += spider_height
        if y + spider_height > HEIGHT:
            y = 0
            x += spider_width
    elif x < 0:
        x = WIDTH - spider_width
        y -= spider_height
        if y < 0:
            y = HEIGHT - spider_height
            x -= spider_width
    elif y + spider_height > HEIGHT:
        y = 0
        x += spider_width
    elif y < 0:
        y = HEIGHT - spider_height
        x -= spider_width

    screen.fill(WHITE)
    screen.blit(spider_image, (x, y))

    pygame.display.flip()
    pygame.time.delay(10)
