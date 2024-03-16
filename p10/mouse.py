import pygame
import sys

PAIN_CIRCLE = 132
CLEAR_CIRCLE = 210

pygame.init()
resolution = (600, 400)
screen = pygame.display.set_mode(resolution)


def draw_circle(action):
    if action == PAIN_CIRCLE:
        color = (255, 0, 50)
    elif action == CLEAR_CIRCLE:
        color = (0, 0, 0)

    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.circle(screen, color, mouse_pos, 20)
    pygame.display.update()


def main():
    is_button_action = ''
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    is_button_action = PAIN_CIRCLE
                if event.button == 3:
                    is_button_action = CLEAR_CIRCLE
            if event.type == pygame.MOUSEBUTTONUP:
                print(is_button_action)
                if event.button == 1 or event.button == 3:
                    is_button_action = ''
        # end event ----------------------------------

        if is_button_action:
            draw_circle(is_button_action)

    sys.exit()


# Run program
main()

