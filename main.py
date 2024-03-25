import pygame
import os
import random
import pygame.time

pygame.init()

WIDTH = 1310
HEIGHT = 750
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
red = (255, 0, 0)
lime = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
silver = (192, 192, 192)
maroon = (128, 0, 0)
olive = (128, 128, 0)
green = (0, 128, 0)
purple = (128, 0, 128)
teal = (0, 128, 128)
navy = (0, 0, 128)
dark_gray = (64, 64, 64)
title_font = pygame.font.Font("freesansbold.ttf", 56)
small_font = pygame.font.Font("freesansbold.ttf", 26)
tiny_font = pygame.font.Font("freesansbold.ttf", 16)

fps = 60
timer = pygame.time.Clock()

def generate_images(p1_selected_face, p2_selected_face):
    #Finds current working directory and images to use in game
    current_directory = os.getcwd()
    img_directory = current_directory + "\\" + "faces"
    img_list = os.listdir(img_directory)
    random.shuffle(img_list)
    p1_guessed_faces = []
    p2_guessed_faces = []
    for i in img_list:
        p1_guessed_faces.append([i, False]) #First item in the inner list of p1 and p2 are the image, the second is the boolean if it was guessed or not
        p2_guessed_faces.append([i, False])
    
    #Selecting random face for each player
    p1_selected_face = random.choice(img_list)
    img_list.remove(p1_selected_face)
    p2_selected_face = random.choice(img_list)

    return img_directory, p1_guessed_faces, p2_guessed_faces, p1_selected_face, p2_selected_face

def toggle_names_button_creation(toggle_names_condition):
    if toggle_names_condition == True:
        toggle_names_button = pygame.draw.rect(screen, dark_gray, [660, HEIGHT-90, 410, 75], 0, 8)
    else:
        toggle_names_button = pygame.draw.rect(screen, gray, [660, HEIGHT-90, 410, 75], 0, 8)
    title_text = title_font.render("Toggle Names", True, white)
    screen.blit(title_text, (670, 670))

    return toggle_names_button

def ask_button_creation(ask_condition):
    if ask_condition == True:
        ask_button = pygame.draw.rect(screen, dark_gray, [280, HEIGHT-90, 125, 75], 0, 8)
    else:
        ask_button = pygame.draw.rect(screen, gray, [280, HEIGHT-90, 125, 75], 0, 8)
    title_text = title_font.render("Ask", True, white)
    screen.blit(title_text, (290, 670))

    return ask_button

def guess_button_creation(guess_condition):
    if guess_condition == True:
        guess_button = pygame.draw.rect(screen, dark_gray, [435, HEIGHT-90, 195, 75], 0, 8)
    else:
        guess_button = pygame.draw.rect(screen, gray, [435, HEIGHT-90, 195, 75], 0, 8)
    title_text = title_font.render("Guess", True, white)
    screen.blit(title_text, (445, 670))

    return guess_button



def draw_backgrounds(current_player, toggle_names_condition, ask_condition, guess_condition):
    #top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 10) #makes hollow white square with black border w thickness based on last param
    #top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 2, 100) #Last param changes border radius

    #Building menu
    top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 0) #(top x, top y, bottom x, bottom y)
    title_text = title_font.render("Fiji Guess Who", True, white)
    screen.blit(title_text, (450, 20))
    bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT-100, WIDTH, 100], 0)
    #restart button
    restart_button = pygame.draw.rect(screen, gray, [30, HEIGHT-90, 220, 75], 0, 8)
    title_text = title_font.render("Restart", True, white)
    screen.blit(title_text, (40, 670))
    #Ask button
    ask_button = ask_button_creation(ask_condition)
    #guess button
    guess_button = guess_button_creation(guess_condition)
    #toggle names button
    toggle_names_button = toggle_names_button_creation(toggle_names_condition)
    #player label (shows which player's data is on the board)
    curr_player_text = small_font.render("Current Player:", True, white)
    screen.blit(curr_player_text, (1090, 670))
    if current_player == 1:
        board_space=pygame.draw.rect(screen, maroon, [0, 100, WIDTH, HEIGHT-200], 0) 
        curr_player_text = small_font.render(f"Player {current_player}", True, red)
    else:
        board_space=pygame.draw.rect(screen, navy, [0, 100, WIDTH, HEIGHT-200], 0) 
        curr_player_text = small_font.render(f"Player {current_player}", True, blue)
    screen.blit(curr_player_text, (1140, 705))

    return restart_button, ask_button, guess_button, toggle_names_button


def draw_board(rows, cols, img_directory, guessed_faces, first_generation, toggle_names_condition, current_player):
    #ddraws the 40 white squares
    board_list = []
    """for i in range(rows):
        for j in range(cols):
            piece = pygame.draw.rect(screen, white, [20 + j * 130, (i+1) *130, 100, 100], 0, 4) # (top x, top y, bottom x, bottom y)
    board_list.append(piece)"""

    img_counter = 0
    for i in range(rows):
        for j in range(cols):
            if img_counter < len(guessed_faces):
                piece = pygame.draw.rect(screen, white, [20 + j * 130, (i+1) *130, 100, 100], 0, 4) # (top x, top y, bottom x, bottom y)
                imp = pygame.image.load(img_directory+"\\"+guessed_faces[img_counter][0])
                scaled_image = pygame.transform.scale(imp, (100, 100))
                screen.blit(scaled_image, (20 + j * 130, (i+1) *130))
                board_list.append(piece)
                if toggle_names_condition == True:
                    file_name_list = guessed_faces[img_counter][0].split(".")
                    face_name = file_name_list[0][:12]
                    if current_player == 1:
                        period3 = tiny_font.render(f"{face_name}", True, black)
                    else:
                        period3 = tiny_font.render(f"{face_name}", True, white)
                    #period3 = tiny_font.render("abcdefghijkl", True, black) #12 letters -> 98 pixels _> 8 pix per -> 4 pix per side
                    #screen.blit(period3, (20 + j * 130, (i+1) *130 + 105))
                    text_rect = period3.get_rect(center=(21 + j * 130+50, (i+1) *130 + 105+10))
                    screen.blit(period3, text_rect)
                if first_generation == True:
                    pygame.display.flip()
                    pygame.time.wait(500)
                img_counter = img_counter + 1
            else:
                break
 
    # Using blit to copy content from one surface to other

    return board_list

def restart_button_logic(first_generation, new_board):
    first_generation = True
    new_board = True
    ###
    restart_button = pygame.draw.rect(screen, dark_gray, [30, HEIGHT-90, 220, 75], 0, 8)
    title_text = title_font.render("Restart", True, white)
    screen.blit(title_text, (40, 670))
    pygame.display.flip()
    pygame.time.wait(500)
    black_screen=pygame.draw.rect(screen, black, [0, 100, WIDTH, HEIGHT], 0) 
    title_text = title_font.render("Restarting", True, red)
    screen.blit(title_text, (500, 350))
    pygame.display.flip()
    pygame.time.wait(500)
    period1 = title_font.render(".", True, red)
    screen.blit(period1, (800, 350))
    pygame.display.flip()
    pygame.time.wait(1000)
    period2 = title_font.render(".", True, red)
    screen.blit(period1, (820, 350))
    pygame.display.flip()
    pygame.time.wait(1000)
    period3 = title_font.render(".", True, red)
    screen.blit(period3, (840, 350))
    pygame.display.flip()
    pygame.time.wait(1000)
    pygame.display.flip() #may not be needed

    return first_generation, new_board

rows = 4
cols = 10
new_board = True
current_player = 0 #this is either 1 or 2 after being set
p1_selected_face = ""
p2_selected_face = ""
p1_guessed_faces = []
p2_guessed_faces = []

#create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Fiji Guess Who")

running = True
img_directory = ""
restart_screen = True
first_generation = False
#WWWWWWWWWWWWWWW make firstgeneration True again
toggle_names_condition = False
selection_screen = True
ask_condition = False
guess_condition = False
border_cords = []
border_condition = False

while running:
    timer.tick(fps)
    screen.fill(white)
    if new_board == True:
        img_directory, p1_guessed_faces, p2_guessed_faces, p1_selected_face, p2_selected_face = generate_images(p1_selected_face, p2_selected_face)
        new_board = False
        current_player = random.choice([1, 2])
    
    if restart_screen == True:
        black_screen=pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT], 0) 
        title_text = title_font.render("Fiji Guess Who", True, white)
        screen.blit(title_text, (450, 20))

        start_button = pygame.draw.rect(screen, red, [550, 325, 200, 100], 0, 8)
        start_text = title_font.render("Start", True, white)
        screen.blit(start_text, (580, 350))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    restart_screen = False
                    start_button = pygame.draw.rect(screen, maroon, [550, 325, 200, 100], 0, 8)
                    start_text = title_font.render("Start", True, white)
                    screen.blit(start_text, (580, 350))
                    pygame.display.flip()
        
    else:
        restart_button, ask_button, guess_button, toggle_names_button = draw_backgrounds(current_player, toggle_names_condition, ask_condition, guess_condition)
        draw_board(rows, cols, img_directory, p1_guessed_faces, first_generation, toggle_names_condition, current_player)
        first_generation = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if toggle_names_button.collidepoint(event.pos):
                    if toggle_names_condition == True:
                        toggle_names_condition = False
                    else:
                        toggle_names_condition = True
                if restart_button.collidepoint(event.pos):
                    first_generation, new_board = restart_button_logic(first_generation, new_board)
                if ask_button.collidepoint(event.pos):
                    if ask_condition == True:
                        ask_condition = False
                        if current_player == 1:
                            current_player = 2
                        else:
                            current_player = 1
                    else:
                        ask_condition = True
                if guess_button.collidepoint(event.pos):
                    if guess_condition == True:
                        guess_condition = False
                        if current_player == 1:
                            current_player = 2
                        else:
                            current_player = 1
                    else:
                        guess_condition = True

    pygame.display.flip() #may not be needed
pygame.quit()

#THINGS TO DO:
#ADD WAY TO CHOOSE YOUR HEAD -> CLICK "CHOOSE HEAD" BUTTON AND THEN AS U HOVER OVER PHOTOS THEY GAIN A BORDER, THEN CLICK THE ONE U WANT. AFTE RIT SHOULD SAY HEAD SELECTED BUT NOT DISPLAY IT
#ADD GUESS BUTTON -> WHEN SELECTED IT SHOULD BE HIGHLIGHTED AND LETS YOU CLICK A PHOTO TO GUESS. AS YOU HOVER OVER PHOTOS THEY SHOULD CHANGE BORDER COLOR. WIN OR LOSE SCREEN APPEARS BASED ON IF YOU GUESSED CORRECT OR NOT (game ends when a guess is made by a player)
#ADD RESTART BUTTOn
#ADD ASK BUTTON -> WHEN SELECTED IT SHOULD BE HIGHLIGHTED AND LETS YOU CLICK ON PHOTOS TO REMOVE THEM AND REPLACE THEM WITH A BLACK SQUARE, AS YOU HOVER OVER THEM THEY SHOULD CHANGE BORDER COLORS
#ADD TOGGLE BUTTON WHICH IS HIGHLIGHTED WHEN SELECTED TO DISPLAY NAMES UNDER THE PHOTOS, THESE WOULD BE THE FILE NAMES WITHOUT THE ENDING JPG
#IF POSSIBLE, ADD A LABEL WHICH SAYS WHO IS PLAYING (PLAYER1 OR 2) AND WHEN THE TURN ENDS, IT MOVES TO THE NEXT PLAYER! EACH OF THEM SHOULD HAVE DIFFERENT LISTS TO KEEP TRACK OF PHOTOS THAT WERE REMOVED DIFFERENTLY FROM EACH PLAYER
#start video again at 42 mins for button collision
#start video again at 1 hour 2 mins and 33 seconds for how to change borders