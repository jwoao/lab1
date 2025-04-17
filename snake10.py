import pygame
import random
import psycopg2
import time

pygame.init()

def init_db():
    conn = psycopg2.connect(
        dbname="snake_db",
        user="postgres",  
        password="skzf0325", 
        host="localhost",
        port="5432"
    )
    return conn, conn.cursor()

def get_user():
    conn, cur = init_db()
    username = input("Enter your username: ")
    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cur.fetchone()

    if user:
        print(f"Welcome back, {username}! Your current level is {user[2]}.")
        user_id = user[0]
    else:
        cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()
        print(f"New user created: {username}. Starting from level 1.")
    
    return user_id, username, conn, cur

def display_scores():
    conn, cur = init_db()
    cur.execute("SELECT users.username, user_score.score FROM users JOIN user_score ON users.id = user_score.id ORDER BY user_score.score DESC")
    scores = cur.fetchall()
    print("\nLeaderboard:")
    for score in scores:
        print(f"{score[0]}: {score[1]}")

def init_game():
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 24)
    
    return screen, clock, font

def draw_snake(snake_block, snake_list, screen):
    for x in snake_list:
        pygame.draw.rect(screen, (0, 255, 0), [x[0], x[1], snake_block, snake_block])

def game_over(score, id, conn, cur):
    cur.execute("INSERT INTO user_score (id, score) VALUES (%s, %s)", (id, score))
    conn.commit()
    print(f"Game Over! Your score was {score}")
    display_scores()

def game_loop():
    snake_block = 10
    snake_speed = 15
    screen, clock, font = init_game()

    user_id, username, conn, cur = get_user()

    game_over_flag = False
    score = 0
    x1 = 300
    y1 = 200
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0

    while not game_over_flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_flag = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:  # Pause game and save score
                    game_over(score, user_id, conn, cur)
                    game_over_flag = True

        if x1 >= 600 or x1 < 0 or y1 >= 400 or y1 < 0:
            game_over(score, user_id, conn, cur)
            game_over_flag = True

        x1 += x1_change
        y1 += y1_change
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over(score, user_id, conn, cur)
                game_over_flag = True

        draw_snake(snake_block, snake_List, screen)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 600 - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, 400 - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10

        clock.tick(snake_speed)

    pygame.quit()
    quit()

if __name__ == "__main__":
    game_loop()
