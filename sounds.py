import arcade

class sounds(arcade.sound.Player):
    def __init__(self,dir_name):
        super().__init__()
        self.load_dir(dir_name)

