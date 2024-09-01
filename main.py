import pyxel
from Mill import Mill

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 356
FRAME_COLOR = 13
BACKGROUND_COLOR = 0

class App:

    mill = Mill()
    color = 11
    test = "Money: "

    def __init__(self):
        pyxel.init(SCREEN_HEIGHT, SCREEN_WIDTH)
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def get_cursor_pos(self):
        return (pyxel.mouse_x, pyxel.mouse_y)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            dx =  pyxel.mouse_x
            dy = pyxel.mouse_y
            print(dx, dy)
            if (dx >= 10 and dx <=30) and (dy >= 10 and dy <=30):
                print("there")
                self.color = 5
                self.test = "This is an updated sentence!" 

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(0, 0, 256, 256, BACKGROUND_COLOR)
        pyxel.rectb(10, 10, 275, 175, FRAME_COLOR)
        pyxel.rectb(11, 11, 273, 173, FRAME_COLOR)
        pyxel.rectb(12, 12, 271, 171, FRAME_COLOR)
        pyxel.text(290, 15, "Money: " + str(self.mill.money), FRAME_COLOR)
        pyxel.text(290, 22, "Ore: " + str(self.mill.ore), FRAME_COLOR)
        pyxel.text(290, 29, "Fuel: " + str(self.mill.fuel), FRAME_COLOR)
        pyxel.text(290, 36, "Steel: " + str(self.mill.steel), FRAME_COLOR)
        pyxel.rectb(10, 200, 35, 15, FRAME_COLOR)
        pyxel.text(12, 205, "Workshop", FRAME_COLOR)
App()