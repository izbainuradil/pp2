import pygame
from color_palette import *
import random

pygame.init()

WIDTH = 600
HEIGHT = 600
CELL = 30

# Егер color_palette-те colorGRAY жоқ болса, мына жерге қоса сал:
colorGRAY = (50, 50, 50) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game") # Терезе аты

font = pygame.font.SysFont(None, 36)
image_game_over = font.render("Game Over", True, colorRED)
image_game_over_rect = image_game_over.get_rect(center=(WIDTH // 2, HEIGHT // 2))

def draw_grid():
    for i in range(0, WIDTH, CELL):
        for j in range(0, HEIGHT, CELL):
            pygame.draw.rect(screen, colorGRAY, (i, j, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.score = 0
        self.level = 1 
        self.alive = True

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i - 1].x
            self.body[i].y = self.body[i - 1].y

        self.body[0].x += self.dx
        self.body[0].y += self.dy

        # Border checks
        if self.body[0].x >= WIDTH // CELL or self.body[0].x < 0 or \
           self.body[0].y >= HEIGHT // CELL or self.body[0].y < 0:
            self.alive = False

    def draw(self):
        for i, segment in enumerate(self.body):
            color = colorRED if i == 0 else colorYELLOW
            pygame.draw.rect(screen, color, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        head = self.body[0]
        if head.x == food.pos.x and head.y == food.pos.y:
            self.score += 1
            self.body.append(Point(self.body[-1].x, self.body[-1].y))
            food.generate_random_pos(self.body)
            self.level = 1 + self.score // 3

class Food:
    def __init__(self):
        self.pos = Point(9, 9)

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def generate_random_pos(self, snake_body):
        while True:
            self.pos.x = random.randint(0, WIDTH // CELL - 1)
            self.pos.y = random.randint(0, HEIGHT // CELL - 1)
            if not any(self.pos.x == s.x and self.pos.y == s.y for s in snake_body):
                break

FPS = 5
clock = pygame.time.Clock()
food = Food()
snake = Snake()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx, snake.dy = 0, -1

    if snake.alive:
        snake.move()
        snake.check_collision(food)
        
        screen.fill(colorBLACK)
        draw_grid()
        snake.draw()
        food.draw()
        
        # Индикаторлар
        sc = font.render(f'Score: {snake.score}', True, colorWHITE)
        lv = font.render(f'Level: {snake.level}', True, colorWHITE)
        screen.blit(sc, (10, 10))
        screen.blit(lv, (WIDTH - 120, 10))
    else:
        # Game Over экраны
        screen.fill(colorBLACK)
        screen.blit(image_game_over, image_game_over_rect)
        final_score = font.render(f"Final Score: {snake.score}", True, colorWHITE)
        screen.blit(final_score, (WIDTH // 2 - 80, HEIGHT // 2 + 50))
        pygame.display.flip()
        pygame.time.wait(3000) # 3 секунд күтіп, ойынды жабады
        running = False

    pygame.display.flip()
    clock.tick(FPS + snake.level)

pygame.quit()