import pygame, sys, os
from ball import Ball

HEIGHT = 800
WIDTH = 1200
FPS = 200



def main():
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    run = True
    ball = Ball(100,100,WIN, WIDTH, HEIGHT)

    while run:
        clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()
        ball_pos = (ball.x, ball.y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                delta_x, delta_y = calculate_delta_x_y(mouse_pos, ball_pos)
                ball.get_velocity(delta_x, delta_y)

            if event.type == pygame.KEYDOWN:
                ball.bounce()

        ball.time_passed = 0.05

        WIN.fill(pygame.Color("black"))
        ball.accelerate()
        ball.move()
        ball.draw()
        ball.bounce_when_touching_sides()
        ball.stop_when_touching_ground()

        draw_line_to_the_cursor(mouse_pos, ball_pos, ball.size,WIN)
        pygame.display.update()


def calculate_delta_x_y(mouse_pos, ball_pos):
    return mouse_pos[0] - ball_pos[0], mouse_pos[1] - ball_pos[1] #delta_x, delta_y

def draw_line_to_the_cursor(mouse_pos, ball_pos, ball_size, WIN):
    ball_pos = (ball_pos[0]+ball_size/2, ball_pos[1]+ball_size/2)
    pygame.draw.line(WIN, pygame.Color("white"), ball_pos, mouse_pos, 1)


if __name__ == "__main__":
    main()
