import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 200
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Секундомер")
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

button_start = pygame.Rect(50, 120, 80, 40)
button_pause = pygame.Rect(160, 120, 80, 40)
button_reset = pygame.Rect(270, 120, 80, 40)

start_time = 0
paused_time = 0
running = False
paused = False


def format_time(ms):
    seconds = ms // 1000
    minutes = seconds // 60
    hours = minutes // 60
    return f"{hours:02}:{minutes % 60:02}:{seconds % 60:02}"

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_start.collidepoint(event.pos):
                if not running:
                    start_time = pygame.time.get_ticks() - paused_time
                    running = True
                    paused = False
                elif paused:
                    paused_time = pygame.time.get_ticks() - start_time
                    paused = False

            elif button_pause.collidepoint(event.pos):
                if running and not paused:
                    paused_time = pygame.time.get_ticks() - start_time
                    paused = True
                elif running and paused:
                    paused = False

            elif button_reset.collidepoint(event.pos):
                start_time = pygame.time.get_ticks()
                paused_time = 0
                running = False
                paused = False


    screen.fill(WHITE)

    if running and not paused:
        elapsed_time = pygame.time.get_ticks() - start_time
    else:
        elapsed_time = paused_time

    timer_text = font.render(format_time(elapsed_time), True, BLACK)
    screen.blit(timer_text, (100, 30))
    pygame.draw.rect(screen, GREEN if not running or paused else BLUE, button_start)
    pygame.draw.rect(screen, RED, button_pause)
    pygame.draw.rect(screen, BLACK, button_reset)
    start_text = small_font.render("Старт" if not running else "Продолжить" if paused else "Идет",True, WHITE)
    pause_text = small_font.render("Пауза", True, WHITE)
    reset_text = small_font.render("Сброс", True, WHITE)
    screen.blit(start_text, (button_start.x + 10, button_start.y + 5))
    screen.blit(pause_text, (button_pause.x + 10, button_pause.y + 5))
    screen.blit(reset_text, (button_reset.x + 10, button_reset.y + 5))

    pygame.display.flip()
