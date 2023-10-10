import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Mensch Ärgere Dich Nicht"

class MADN(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, center_window = True)

        arcade.set_background_color((255, 0, 255))

    def setup(self):
        pass
    
    def on_draw(self):
        self.clear()
    

def main():
    window = MADN()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()