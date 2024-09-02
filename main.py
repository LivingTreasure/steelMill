import pyxel
from Mill import Mill

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 356
FRAME_COLOR = 13
BACKGROUND_COLOR = 0

class App:

    def __init__(self):
        pyxel.init(SCREEN_HEIGHT, SCREEN_WIDTH)
        pyxel.mouse(True)

        self.mill = Mill()
        self.show_furnace_gui = False
        self.show_railyard_gui = False
        self.show_mill_gui = True
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
            ## Furnace button set
            if ((dx >= 75 and dx <=109) and (dy >= 123 and dy <=137) and self.show_mill_gui):
                print("there")
                self.show_furnace_gui = True
                self.show_mill_gui = False
            
            if ((dx >= 10 and dx <=36) and (dy >= 213 and dy <=227) and self.show_furnace_gui):
                self.show_furnace_gui = False
                self.show_mill_gui = True

            ## railyard button set
            if ((dx >= 37 and dx <=71) and (dy >= 95 and dy <=109) and self.show_mill_gui):
                self.show_railyard_gui = True
                self.show_mill_gui = False

            if ((dx >= 10 and dx <=36) and (dy >= 232 and dy <=246) and self.show_railyard_gui):
                self.show_railyard_gui = False
                self.show_mill_gui = True

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

        if self.show_furnace_gui:
            pyxel.rectb(10, 195, 23, 15, FRAME_COLOR)
            pyxel.text(12, 200, "Forge", FRAME_COLOR)
            pyxel.text(34, 200, str(self.mill.steelProduced * self.mill.workers) + " tons of steel with " + str(self.mill.oreToSteel * self.mill.workers) + " tons ore " + str(self.mill.fuelToSteel * self.mill.workers) + " tons fuel", FRAME_COLOR)

            pyxel.rectb(10, 213, 27, 15, FRAME_COLOR)
            pyxel.text(12, 218, "Return", FRAME_COLOR)

        if self.show_railyard_gui:
            pyxel.rectb(10, 195, 15, 15, FRAME_COLOR)
            pyxel.text(12, 200, "Buy", FRAME_COLOR)
            pyxel.text(26, 200, str(self.mill.rail_cap) + "  tons ore for $" + str(self.mill.rail_cap * self.mill.ore_cost), FRAME_COLOR)

            pyxel.rectb(10, 213, 15, 15, FRAME_COLOR)
            pyxel.text(12, 218, "Buy", FRAME_COLOR)
            pyxel.text(26, 218, str(self.mill.rail_cap) + " tons Fuel for $" + str(self.mill.rail_cap * self.mill.fuel_cost), FRAME_COLOR)

            pyxel.rectb(10, 232, 27, 15, FRAME_COLOR)
            pyxel.text(12, 237, "Return", FRAME_COLOR)

        if self.show_mill_gui:
            pyxel.rectb(75, 123, 35, 15, FRAME_COLOR)
            pyxel.text(77, 128, "Furnaces", FRAME_COLOR)

            pyxel.rectb(37, 95, 35, 15, FRAME_COLOR)
            pyxel.text(39, 100, "Railyard", FRAME_COLOR)

            pyxel.rectb(209, 66, 35, 15, FRAME_COLOR)
            pyxel.text(211, 71, "workshop", FRAME_COLOR)

            pyxel.rectb(213, 131, 43, 15, FRAME_COLOR)
            pyxel.text(215, 136, "Management", FRAME_COLOR)
App()