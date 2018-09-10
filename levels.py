import pygame
from objects import Blocks, Wall, HorWall


def level_one(block_list, all_sprite_list, width):

    for i in range(6):
        block = Blocks(165 + width / 8 * i, 30, 1)
        all_sprite_list.add(block)
        block_list.add(block)

    for i in range(6):
        block = Blocks(165 + width / 8 * i, 90, 2)
        all_sprite_list.add(block)
        block_list.add(block)

    for i in range(6):
        block = Blocks(165 + width / 8 * i, 150, 3)
        all_sprite_list.add(block)
        block_list.add(block)


def level_two(block_list, all_sprite_list, width):

    for i in range(2):
        for j in range(4):
            block = Blocks(325 + width / 8 * j, 60 * i, 1)
            all_sprite_list.add(block)
            block_list.add(block)

    for i in range(2, 4):
        for j in range(4):
            block = Blocks(325 + width / 8 * j, 60 * i, 2)
            all_sprite_list.add(block)
            block_list.add(block)

    for i in range(4, 6):
        for j in range(4):
            block = Blocks(325 + width / 8 * j, 60 * i, 3)
            all_sprite_list.add(block)
            block_list.add(block)

    for i in range(6, 8):
        for j in range(4):
            block = Blocks(325 + width / 8 * j, 60 * i, 4)
            all_sprite_list.add(block)
            block_list.add(block)


def level_tree(block_list, all_sprite_list, walls_list, width):

    for i in range(2):
        a = 0
        for j in range(6):
            if j == 3:
                a += 100
            block = Blocks(115 + width / 8 * j + a, 30 + 70 * i, 1)
            all_sprite_list.add(block)
            block_list.add(block)

    for i in range(2, 4):
        a = 0
        for j in range(6):
            if j == 3:
                a += 100
            block = Blocks(115 + width / 8 * j + a, 30 + 70 * i, 2)
            all_sprite_list.add(block)
            block_list.add(block)

    for i in range(4, 6):
        a = 0
        for j in range(6):
            if j == 3:
                a += 100
            block = Blocks(115 + width / 8 * j + a, 30 + 70 * i, 3)
            all_sprite_list.add(block)
            block_list.add(block)

    wall = Wall(625, 0, 1)
    all_sprite_list.add(wall)
    walls_list.add(wall)


def level_four(block_list, all_sprite_list, walls_list, width):
    while len(walls_list) > 0:
        walls_list.pop()

    for i in range(2):
        for j in range(8):
            block = Blocks(5 + width / 8 * j, 30 + 70 * i, 1)
            all_sprite_list.add(block)
            block_list.add(block)

    for j in range(2, 6):
        block = Blocks(5 + width / 8 * j, 170, 2)
        all_sprite_list.add(block)
        block_list.add(block)

    for i in range(3, 5):
        for j in range(8):
            block = Blocks(5 + width / 8 * j, 30 + 70 * i, 3)
            all_sprite_list.add(block)
            block_list.add(block)

    for j in range(2, 6):
        block = Blocks(5 + width / 8 * j, 380, 4)
        all_sprite_list.add(block)
        block_list.add(block)

    for i in 0, 980:
        for j in 170, 380:
            h_wall = HorWall(i, j, 1)
            all_sprite_list.add(h_wall)
            walls_list.add(h_wall)


def level_five(block_list, all_sprite_list, walls_list):
    while len(walls_list) > 0:
        walls_list.pop()

    for i in 300, 477, 654, 831:
        for j in 100, 170:
            block = Blocks(i, j, 1)
            all_sprite_list.add(block)
            block_list.add(block)

    for i in 50, 1080:
        for j in 100, 170, 240, 310, 380:
            block = Blocks(i, j, 2)
            all_sprite_list.add(block)
            block_list.add(block)

    for i in 300, 477, 654, 831:
        for j in 240, 310, 380:
            block = Blocks(i, j, 3)
            all_sprite_list.add(block)
            block_list.add(block)

    h_wall2 = HorWall(300, 450, 2)
    all_sprite_list.add(h_wall2)
    walls_list.add(h_wall2)

    for i in 250, 1000:
        wall2 = Wall(i, 240, 2)
        all_sprite_list.add(wall2)
        walls_list.add(wall2)
