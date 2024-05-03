class Face(object): #Player class
    def __init__ (self, img_name, img_directory):
        self.guessed = False #False by default
        self.img = img_name
        self.img_location = img_directory + "\\"+ img_name
        self.name = img_name.split(".")[0][:12]
        self.name = self.name[0].upper() + self.name[1:].lower()