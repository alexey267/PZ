import pygame
import random

pygame.init()

# Определение размеров игрового окна
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tetris")

# Определение цветов
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)

# Определение размеров блока
block_size = 30

# Определение форм фигур
shapes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]

# Определение начальной позиции игрока
player_x = screen_width // 2
player_y = 0

# Определение текущей и следующей фигур
current_shape = random.choice(shapes)
next_shape = random.choice(shapes)

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление позиции игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= block_size
    elif keys[pygame.K_RIGHT]:
        player_x += block_size
    elif keys[pygame.K_DOWN]:
        player_y += block_size

    # Рисование игрового поля
    screen.fill(BLACK)
    for i in range(len(current_shape)):
        for j in range(len(current_shape[i])):
            if current_shape[i][j] == 1:
                pygame.draw.rect(screen, WHITE, (player_x + j * block_size, player_y + i * block_size, block_size, block_size))

    # Отображение следующей фигуры
    next_x = screen_width - 200
    next_y = 100
    for i in range(len(next_shape)):
        for j in range(len(next_shape[i])):
            if next_shape[i][j] == 1:
                pygame.draw.rect(screen, WHITE, (next_x + j * block_size, next_y + i * block_size, block_size, block_size))

    pygame.display.flip()

pygame.quit()
