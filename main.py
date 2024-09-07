import pyxel
import time
from Mill import Mill
from Market import Market

SCREEN_WIDTH = 256
SCREEN_HEIGHT = 356
FRAME_COLOR = 13
BACKGROUND_COLOR = 0

class App:

    def __init__(self):
        pyxel.init(SCREEN_HEIGHT, SCREEN_WIDTH)
        pyxel.mouse(True)

        pyxel.images[0].load(0, 0, "resources/interior1_tileset.png")

        self.mill = Mill()
        self.market = Market()
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
            
            if ((dx >= 290 and dx <=316) and (dy >= 152 and dy <=166) and self.show_furnace_gui):
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
        pyxel.rectb(10, 10, 248, 172, FRAME_COLOR)
        pyxel.rectb(11, 11, 246, 170, FRAME_COLOR)
        pyxel.rectb(12, 12, 244, 168, FRAME_COLOR)
        pyxel.text(290, 15, "Money: " + str(self.mill.money), FRAME_COLOR)
        pyxel.text(290, 22, "Ore: " + str(self.mill.ore), FRAME_COLOR)
        pyxel.text(290, 29, "Fuel: " + str(self.mill.fuel), FRAME_COLOR)
        pyxel.text(290, 36, "Billets: " + str(self.mill.billets), FRAME_COLOR)
        pyxel.text(290, 43, "Blooms: " + str(self.mill.blooms), FRAME_COLOR)
        pyxel.text(290, 50, "Slabs: " + str(self.mill.slabs), FRAME_COLOR)

        if self.show_furnace_gui:
            pyxel.rectb(10, 195, 23, 15, FRAME_COLOR)
            pyxel.text(12, 200, "Forge", FRAME_COLOR)
            pyxel.text(36, 200, str(self.mill.steelProduced * self.mill.workers) + " tons of steel billets with " + str(self.mill.oreToSteel * self.mill.workers) + " tons ore " + str(self.mill.fuelToSteel * self.mill.workers) + " tons fuel", FRAME_COLOR)

            pyxel.rectb(10, 213, 23, 15, FRAME_COLOR)
            pyxel.text(12, 218, "Forge", FRAME_COLOR)
            pyxel.text(36, 218, str(self.mill.steelProduced * self.mill.workers) + " tons of steel blooms with " + str(self.mill.oreToSteel * self.mill.workers) + " tons ore " + str(self.mill.fuelToSteel * self.mill.workers) + " tons fuel", FRAME_COLOR)

            pyxel.rectb(10, 231, 23, 15, FRAME_COLOR)
            pyxel.text(12, 236, "Forge", FRAME_COLOR)
            pyxel.text(36, 236, str(self.mill.steelProduced * self.mill.workers) + " tons of steel slabs with " + str(self.mill.oreToSteel * self.mill.workers) + " tons ore " + str(self.mill.fuelToSteel * self.mill.workers) + " tons fuel", FRAME_COLOR)


            pyxel.rectb(290, 152, 27, 15, FRAME_COLOR)
            pyxel.text(292, 157, "Return", FRAME_COLOR)

            frame = pyxel.frame_count // 30 % 4
            if frame == 0:
                pyxel.blt(98, 70, 0, 0, 1, 75, 52, None, None, 3.2)
            elif frame == 1:
                pyxel.blt(98, 70, 0, 0, 56, 75, 52, None, None, 3.2)
            elif frame == 2:
                pyxel.blt(98, 70, 0, 0, 111, 75, 52, None, None, 3.2)
            elif frame == 3:
                pyxel.blt(98, 70, 0, 0, 56, 75, 52, None, None, 3.2)


        if self.show_railyard_gui:
            pyxel.rectb(10, 195, 15, 15, FRAME_COLOR)
            pyxel.text(12, 200, "Buy", FRAME_COLOR)
            pyxel.text(19, 193, str(self.mill.rail_cap) + "  tons ore for $" + str(self.mill.rail_cap * self.market.ore_cost), FRAME_COLOR)

            pyxel.rectb(10, 213, 15, 15, FRAME_COLOR)
            pyxel.text(12, 218, "Buy", FRAME_COLOR)
            pyxel.text(26, 218, str(self.mill.rail_cap) + " tons Fuel for $" + str(self.mill.rail_cap * self.market.fuel_cost), FRAME_COLOR)

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