import pygame
import os
import random
import pygame.time
from Player import *
from Face import *

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

rows = 4
cols = 10
new_board = True
current_player = 0 #this is either 1 or 2 after being set

#create screen
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Guess Who")

#Generates images, creates faces, fills each player's face list, and associates secret faces
def generateImages(player1, player2, all_faces):
    current_directory = os.getcwd()
    img_directory = current_directory + "\\" + "faces"
    img_list = os.listdir(img_directory)
    action_counter = 0
    img_counter = 0
    for i in img_list:
        #We can only have at most 40 faces on the board
        if img_counter >= 40:
            break
        player1.faces_list.append(Face(i, img_directory))
        player2.faces_list.append(Face(i, img_directory))
        img_name = i.split(".")[0][:12]
        img_name = img_name[0].upper() + img_name[1:].lower()
        all_faces[img_name] = pygame.image.load(img_directory + "\\"+ i)
        action_counter = action_counter + 1
        #Adds animation to the loop to avoid the look of a frozen screen while images load in
        if action_counter == 1:
            black_screen=pygame.draw.rect(screen, black, [0, 100, WIDTH, HEIGHT], 0) 
            title_text = title_font.render("Loading", True, red)
            screen.blit(title_text, (500, 350))
        elif action_counter == 2:
            period1 = title_font.render(".", True, red)
            screen.blit(period1, (750, 350))
        elif action_counter == 3:
            period2 = title_font.render(".", True, red)
            screen.blit(period1, (770, 350))
        elif action_counter == 4:
            period3 = title_font.render(".", True, red)
            screen.blit(period3, (790, 350))
            action_counter = 0
        pygame.display.flip()
        img_counter = img_counter + 1

def draw_backgrounds(current_player, toggle_names_condition, ask_condition, guess_condition, restart_button_change, toggle_hidden_face_condition, all_faces):
    #top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 10) #makes hollow white square with black border w thickness based on last param
    #top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 2, 100) #Last param changes border radius

    #Building menu
    top_menu = pygame.draw.rect(screen, black, [0, 0, WIDTH, 100], 0) #(top x, top y, bottom x, bottom y)
    title_text = title_font.render("Guess Who", True, white)
    screen.blit(title_text, (500, 20))
    bottom_menu = pygame.draw.rect(screen, black, [0, HEIGHT-100, WIDTH, 100], 0)
    #restart button
    if restart_button_change == True:
        restart_button = pygame.draw.rect(screen, dark_gray, [30, HEIGHT-90, 220, 75], 0, 8)
    else:
        restart_button = pygame.draw.rect(screen, gray, [30, HEIGHT-90, 220, 75], 0, 8)
    title_text = title_font.render("Restart", True, white)
    screen.blit(title_text, (40, 670))
    #Ask button
    if ask_condition == True:
        ask_button = pygame.draw.rect(screen, dark_gray, [280, HEIGHT-90, 125, 75], 0, 8)
    else:
        ask_button = pygame.draw.rect(screen, gray, [280, HEIGHT-90, 125, 75], 0, 8)
    title_text = title_font.render("Ask", True, white)
    screen.blit(title_text, (290, 670))
    #guess button
    if guess_condition == True:
        guess_button = pygame.draw.rect(screen, dark_gray, [435, HEIGHT-90, 195, 75], 0, 8)
    else:
        guess_button = pygame.draw.rect(screen, gray, [435, HEIGHT-90, 195, 75], 0, 8)
    title_text = title_font.render("Guess", True, white)
    screen.blit(title_text, (445, 670))
    #toggle names button
    if toggle_names_condition == True:
        toggle_names_button = pygame.draw.rect(screen, dark_gray, [660, HEIGHT-90, 410, 75], 0, 8)
    else:
        toggle_names_button = pygame.draw.rect(screen, gray, [660, HEIGHT-90, 410, 75], 0, 8)
    title_text = title_font.render("Toggle Names", True, white)
    screen.blit(title_text, (670, 670))
    #toggle hidden face button
    if toggle_hidden_face_condition == True:
        toggle_hidden_face_button = pygame.draw.rect(screen, dark_gray, [30, 10, 195, 75], 0, 8)
        scaled_image = pygame.transform.scale(all_faces[current_player.hidden_face.name], (80, 80))
        screen.blit(scaled_image, (270, 10))
    else:
        toggle_hidden_face_button = pygame.draw.rect(screen, gray, [30, 10, 195, 75], 0, 8)
    title_text = small_font.render("Toggle Secret", True, white)
    screen.blit(title_text, (40, 20)) 
    title_text = small_font.render("Face", True, white)
    screen.blit(title_text, (100, 55))
    #quit button
    quit_button = pygame.draw.rect(screen, gray, [1135, 10, WIDTH-30-1135, 75], 0, 8)
    title_text = title_font.render("Quit", True, white)
    screen.blit(title_text, (1145, 20))

    #player label (shows which player's data is on the board)
    curr_player_text = small_font.render("Current Player:", True, white)
    screen.blit(curr_player_text, (1090, 670))
    board_space=pygame.draw.rect(screen, current_player.background_color, [0, 100, WIDTH, HEIGHT-200], 0) 
    curr_player_text = small_font.render(f"Player {current_player.name}", True, current_player.player_name_color)
    screen.blit(curr_player_text, (1140, 705))

    return restart_button, ask_button, guess_button, toggle_names_button, toggle_hidden_face_button, quit_button

def draw_board(rows, cols, guessed_faces, toggle_names_condition, current_player, all_faces, first_turn_animation):
    #draws the 40 white squares
    img_counter = 0
    current_player.face_buttons.clear()
    for i in range(rows):
        for j in range(cols):
            if img_counter < len(guessed_faces):
                piece = pygame.draw.rect(screen, current_player.background_color, [20 + j * 130, (i+1) *130, 100, 100], 0, 4) # (top x, top y, bottom x, bottom y)
                current_player.face_buttons.append(piece) 
                if guessed_faces[img_counter].guessed == False:
                    scaled_image = pygame.transform.scale(all_faces[guessed_faces[img_counter].name], (100, 100))
                    screen.blit(scaled_image, (20 + j * 130, (i+1) *130))
                if toggle_names_condition == True:
                    period3 = tiny_font.render(f"{guessed_faces[img_counter].name}", True, current_player.text_color)
                    text_rect = period3.get_rect(center=(21 + j * 130+50, (i+1) *130 + 105+10))
                    screen.blit(period3, text_rect)
                img_counter = img_counter + 1
                if first_turn_animation == True:
                    pygame.time.wait(50)
                pygame.display.flip()
            else:
                break
    pygame.display.flip()

def restart_button_logic():
    pygame.time.wait(200)
    black_screen=pygame.draw.rect(screen, black, [0, 100, WIDTH, HEIGHT], 0) 
    title_text = title_font.render("Restarting", True, red)
    screen.blit(title_text, (500, 350))
    pygame.display.flip()
    pygame.time.wait(200)
    period1 = title_font.render(".", True, red)
    screen.blit(period1, (800, 350))
    pygame.display.flip()
    pygame.time.wait(200)
    period2 = title_font.render(".", True, red)
    screen.blit(period1, (820, 350))
    pygame.display.flip()
    pygame.time.wait(200)
    period3 = title_font.render(".", True, red)
    screen.blit(period3, (840, 350))
    pygame.display.flip()
    pygame.time.wait(200)
    pygame.display.flip() #may not be needed


if __name__=="__main__":
    player1 = Player(maroon, black, 1, red)
    player2 = Player(navy, white, 2, blue)
    all_faces = {}
    restart_screen = True
    running = True
    ask_condition = False
    guess_condition = False
    toggle_names_condition = False
    redraw_condition = True
    restart_condition = True
    images_loaded = False
    end_screen = False
    toggle_hidden_face_condition = False
    first_turn_animation = True

    #Game Loop
    while running:
        timer.tick(fps)
        screen.fill(white)
        black_screen=pygame.draw.rect(screen, black, [0, 0, WIDTH, HEIGHT], 0) 
        title_text = title_font.render("Guess Who", True, white)
        screen.blit(title_text, (500, 20))
        if (images_loaded == False):
            generateImages(player1, player2, all_faces)
            images_loaded = True
        if restart_screen == True:
            start_button = pygame.draw.rect(screen, red, [560, 225, 200, 100], 0, 8)
            start_text = title_font.render("Start", True, white)
            screen.blit(start_text, (595, 250))
            quit_button = pygame.draw.rect(screen, red, [560, 375, 205, 100], 0, 8)
            title_text = title_font.render("Quit", True, white)
            screen.blit(title_text, (600, 400))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        restart_screen = False
                        start_button = pygame.draw.rect(screen, maroon, [560, 225, 200, 100], 0, 8)
                        start_text = title_font.render("Start", True, white)
                        screen.blit(start_text, (595, 250))
                        pygame.display.flip()
                    if quit_button.collidepoint(event.pos):
                        running = False

        elif end_screen == True:
            title_text = title_font.render(f"Player {current_player.name} Wins!", True, current_player.player_name_color)
            screen.blit(title_text, (460, 150))

            start_button = pygame.draw.rect(screen, red, [485, 325, 350, 100], 0, 8)
            start_text = title_font.render("Play Again", True, white)
            screen.blit(start_text, (515, 350))

            quit_button = pygame.draw.rect(screen, red, [560, 500, 205, 100], 0, 8)
            title_text = title_font.render("Quit", True, white)
            screen.blit(title_text, (600, 525))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.collidepoint(event.pos):
                        end_screen = False
                        restart_condition = True
                        redraw_condition = True
                        start_button = pygame.draw.rect(screen, maroon, [485, 325, 350, 100], 0, 8)
                        start_text = title_font.render("Play Again", True, white)
                        screen.blit(start_text, (515, 350))
                        pygame.display.flip()
                    if quit_button.collidepoint(event.pos):
                        running = False

        #Game screen takes effect
        else:
            if redraw_condition == True:
                if restart_condition == True:
                    current_player = random.choice([player1, player2])
                    random.shuffle(player1.faces_list)
                    random.shuffle(player2.faces_list)
                    player1.hidden_face = random.choice(player1.faces_list)
                    player2.hidden_face = random.choice(player2.faces_list)
                    #Prevents players from having the same secret face
                    while (player1.hidden_face.name == player2.hidden_face.name):
                        player2.hidden_face = random.choice(player2.faces_list)
                    for i in player1.faces_list:
                        i.guessed = False
                    for j in player2.faces_list:
                        j.guessed = False
                    restart_condition = False
                    toggle_hidden_face_condition = False
                    toggle_names_condition = False
                redraw_condition = False
                restart_button, ask_button, guess_button, toggle_names_button, toggle_hidden_face_button, quit_button = draw_backgrounds(current_player, toggle_names_condition, ask_condition, guess_condition, restart_condition, toggle_hidden_face_condition, all_faces)
                draw_board(rows, cols, current_player.faces_list, toggle_names_condition, current_player, all_faces, first_turn_animation)
                first_turn_animation = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if toggle_names_button.collidepoint(event.pos):
                        toggle_names_condition = not toggle_names_condition
                        redraw_condition = True
                    if restart_button.collidepoint(event.pos):
                        restart_button_logic()
                        redraw_condition = True
                        restart_condition = True
                        first_turn_animation = True
                    #Prevents players from guessing and asking at the same time
                    if ask_button.collidepoint(event.pos) and guess_condition == False:
                        ask_condition = not ask_condition
                        redraw_condition = True
                        if (ask_condition == False):
                            if current_player == player1:
                                current_player = player2
                            else:
                                current_player = player1
                            toggle_hidden_face_condition = False
                            first_turn_animation = True
                    if ask_condition == True:
                        for i in range(len(current_player.face_buttons)):
                            if current_player.face_buttons[i].collidepoint(event.pos) and current_player.faces_list[i].guessed == False:
                                current_player.faces_list[i].guessed = True
                                redraw_condition = True
                    #Prevents players from guessing and asking at the same time
                    if guess_button.collidepoint(event.pos) and ask_condition == False:
                        guess_condition = True
                        redraw_condition = True
                    if guess_condition == True:
                        for i in range(len(current_player.face_buttons)):
                            if current_player.face_buttons[i].collidepoint(event.pos) and current_player.faces_list[i].guessed == False:
                                guess_condition = False
                                end_screen = True
                                first_turn_animation = True
                                #If the guess was incorrect
                                if current_player.faces_list[i] != current_player.hidden_face:
                                    if current_player == player1:
                                        current_player = player2
                                    else:
                                        current_player = player1
                                    toggle_hidden_face_condition = False
                                break
                    if toggle_hidden_face_button.collidepoint(event.pos):
                        toggle_hidden_face_condition = not toggle_hidden_face_condition
                        redraw_condition = True
                    if quit_button.collidepoint(event.pos):
                        running = False
    pygame.quit()