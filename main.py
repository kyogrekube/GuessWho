import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)

fps = 60
timer = pygame.time.Clock()
rows = 6
cols = 8
guessed_faces = [] #tracks which faces have been guessed or not
options_list = []
new_board = True

#create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Fiji Guess Who")
title_font = pygame.font.Font("freesansbold.ttf", 56)
small_font = pygame.font.Font("freesansbold.ttf", 26)

def generate_board(rows, cols):
    for item in range(rows * cols):
        options_list.append(item)


def draw_backgrounds():
    #top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 10) #makes hollow white square with black border w thickness based on last param
    #top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 2, 100) #Last param changes border radius
    top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 0)
    title_text = title_font.render("Fiji Guess Who", True, white)
    screen.blit(title_text, (100, 20))
    board_space=pygame.draw.rect(screen, gray, [0, 100, WIDTH, HEIGHT-200], 0) 
    bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT-100, WIDTH, 100], 0)

def draw_board(rows, cols):
    board_list = []
    for i in range(cols):
        for j in range(rows):
            piece = pygame.draw.rect(screen, white, [i * 75 + 12, j * 65 + 112, 50 , 50], 0, 4)
            board_list.append(piece)

    return board_list


running = True
while running:
    timer.tick(fps)
    screen.fill(white)
    if new_board == True:
        #generate_board(rows, cols)
        new_board = False

    draw_backgrounds()
    draw_board(rows, cols)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
pygame.quit()