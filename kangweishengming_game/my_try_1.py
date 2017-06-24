import sys
import time

import pygame
from pygame.locals import *

from random import randint

__author__ = {
    "name": "TMM",
    "email": "tangmingmingvip@qq.com"
}

SCREEN_SIZE = (640, 480)
BOX_SIZE = 5
SCREEN_COLOR = (0, 0, 0)

MAX_X = SCREEN_SIZE[0] // BOX_SIZE
MAX_Y =SCREEN_SIZE[1] // BOX_SIZE

def init(screen, rect_color):
    pass

    # pygame.draw.rect(screen, rect_color, Rect((10, 20), (30 ,50)))

def init_matrix():
    matrix = []

    for i in range(SCREEN_SIZE[1] // BOX_SIZE):
        matrix.append([])
        for j in range(SCREEN_SIZE[0] // BOX_SIZE):
            item = randint(0, 1)
            matrix[i].append(item)

    return matrix

def update_matrix(matrix):



    new_matrix = []
    for j in range(len(matrix)):
        new_matrix.append([])
        for i in range(len(matrix[j])):
            count_live = 0;
            # 左上
            if(i>0 and j>0):
                if matrix[j-1][i-1]:
                    count_live += 1

            #右上
            if (j > 0):
                if matrix[j - 1][i]:
                    count_live += 1

            # 左上
            if(i < MAX_X-1 and j >0):
                if matrix[j-1][i+1]:
                    count_live += 1

            # right
            if(i < MAX_X-1):
                if matrix[j][i+1]:
                    count_live += 1

            # lower right
            if(i < MAX_X-1 and j < MAX_Y-1):
                if matrix[j+1][i+1]:
                    count_live += 1

            # down
            if(j < MAX_Y-1):
                if matrix[j+1][i]:
                    count_live += 1

            # lower left
            if(i>0 and j<MAX_Y-1):
                if matrix[j+1][i-1]:
                    count_live += 1

            # left
            if(i>0):
                if matrix[j][i-1]:
                    count_live += 1

            if count_live == 3:
                new_matrix[j].append(1)
            elif count_live == 2:
                new_matrix[j].append(matrix[j][i])
            else:
                new_matrix[j].append(0)

    return new_matrix


def draw_rect(screen,rect_color, matrix):
    count_h = 0
    for i in matrix:
        count_w = 0
        for j in i:
            if j:
                s_pos = (count_w*BOX_SIZE, count_h*BOX_SIZE)
                e_pos = (BOX_SIZE, BOX_SIZE)
                pygame.draw.rect(screen,
                                 rect_color,
                                 Rect(s_pos, e_pos))

            count_w += 1

        count_h += 1


def print_matrix(matrix):
    for j in matrix:
        print("")
        for i in j:
            print(i, end=" ")

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

    rect_color = (255, 255, 255)
    rect_start_pos = (10, 20)
    rect_end_pos = (50, 80)

    matrix = init_matrix()

    main_count = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.fill(SCREEN_COLOR)
        draw_rect(screen, rect_color, matrix)
        matrix = update_matrix(matrix)

        pygame.display.update()
        main_count += 1
        # print(main_count)
        time.sleep(0.01)

if __name__ == "__main__":
    main()