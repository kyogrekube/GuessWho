import pygame
import os
import random

pygame.init()

WIDTH = 1310
HEIGHT = 750
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

fps = 60
timer = pygame.time.Clock()
rows = 4
cols = 10
guessed_faces = [] #tracks which faces have been guessed or not
options_list = []
new_board = True

#create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Fiji Guess Who")
title_font = pygame.font.Font("freesansbold.ttf", 56)
small_font = pygame.font.Font("freesansbold.ttf", 26)

def generate_images():
    #Finds current working directory and images to use in game
    current_directory = os.getcwd()
    img_directory = current_directory + "\\" + "faces"
    img_list = os.listdir(img_directory)
    random.shuffle(img_list)

    return img_directory, img_list


def draw_backgrounds():
    #top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 10) #makes hollow white square with black border w thickness based on last param
    #top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 2, 100) #Last param changes border radius
    top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 0)
    title_text = title_font.render("Fiji Guess Who", True, white)
    screen.blit(title_text, (450, 20))
    board_space=pygame.draw.rect(screen, gray, [0, 100, WIDTH, HEIGHT-200], 0) 
    bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT-100, WIDTH, 100], 0)

def draw_board(rows, cols, img_directory, img_list):
    #ddraws the 40 white squares
    board_list = []
    for i in range(rows):
        for j in range(cols):
            piece = pygame.draw.rect(screen, white, [20 + j * 130, (i+1) *130, 100, 100], 0, 4) # (top x, top y, bottom x, bottom y)
    board_list.append(piece)

    img_counter = 0
    for i in range(rows):
        for j in range(cols):
            if img_counter < len(img_list):
                imp = pygame.image.load(img_directory+"\\"+img_list[img_counter])
                scaled_image = pygame.transform.scale(imp, (100, 100))
                screen.blit(scaled_image, (20 + j * 130, (i+1) *130))
                img_counter = img_counter + 1
            else:
                break
 
    # Using blit to copy content from one surface to other

    return board_list


running = True
img_list = []
img_directory = ""
while running:
    timer.tick(fps)
    screen.fill(white)
    if new_board == True:
        img_directory, img_list = generate_images()
        new_board = False
    draw_backgrounds()
    draw_board(rows, cols, img_directory, img_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
pygame.quit()