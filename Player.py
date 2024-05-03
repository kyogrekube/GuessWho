from Face import *

class Player(object): #Player class
    def __init__ (self, background_color, text_color, name, player_name_color):
        self.faces_list = []
        self.hidden_face = None
        self.background_color = background_color
        self.text_color = text_color
        self.name = name
        self.player_name_color = player_name_color
        self.face_buttons = []
