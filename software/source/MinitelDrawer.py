# +----------------------------------------------------------+ #
# | Title: MinitelDrawer.py                                  | #
# | Author: Constant ROUX                                    | #
# | Date: 30 / 12 / 2021                                     | #
# | Contents : A class file to create tkinter interface      | #
# | necessary to draw on the Minitel 2 Alcatel in semi       | #
# | graphic mode                                             | #
# +----------------------------------------------------------+ #

import tkinter
import numpy
from .Imager import Imager


class MinitelDrawer:
    def __init__(self, minitel, grid_width=80, grid_height=75, levels=8, size_case=10):
        self.imager = Imager(None, mode="image_drawer")

        self.minitel = minitel

        self.display_grid = []

        self.grid_saved = numpy.empty(shape=(grid_width, grid_height))
        self.grid_saved.fill(7)

        self.colors = ("#000000", "#808080", "#949494", "#a9a9a9", "#bdbebd", "#d3d3d3", "#e9e9e9", "#ffffff")
        self.size_case = size_case
        self.levels = levels
        self.grid_width = grid_width
        self.grid_height = grid_height

        self.app = tkinter.Tk()

        self._init_window()
        self._create_grid()
        self._create_color_scale()

    def _init_window(self):
        self.app.title("Minitel Drawer")
        self.app.geometry("925x800")

    def _create_grid(self):
        self.canvas = tkinter.Canvas(self.app, width=self.grid_width * self.size_case,
                                     height=self.grid_height * self.size_case)
        self.canvas.grid(row=0, column=0, padx=20, pady=20)

        for i in range(self.grid_width):
            self.display_grid.append([])
            for j in range(self.grid_height):
                self.display_grid[i].append(self.canvas.create_rectangle(i * self.size_case,
                                                                         j * self.size_case,
                                                                         self.size_case * (i + 1),
                                                                         self.size_case * (j + 1),
                                                                         fill=self.colors[7],
                                                                         outline=""))

        for i in range(self.grid_height // 3):
            for j in range(self.grid_width // 2):
                self.minitel.write_semigraphical(b'\x5F', 7, 7)
        self.minitel.move_cursor(1, 1)

    def _create_color_scale(self):
        self.cursor_color_bar = tkinter.Scale(self.app,
                                              label='Couleur',
                                              from_=0,
                                              to=self.levels - 1,
                                              sliderrelief='flat',
                                              length=self.grid_height * self.size_case)

        self.cursor_color_bar.grid(row=0, column=1)

    def _on_mouse_click(self, event):
        # update case of grid
        grid_x = event.x // self.size_case
        grid_y = event.y // self.size_case

        # check mouse position
        if not (grid_x < 0 or grid_x >= self.grid_width or grid_y < 0 or grid_y >= self.grid_height):
            # buf old color
            color1 = self.canvas.itemcget(self.display_grid[grid_x][grid_y], 'fill')

            # update display
            self.canvas.itemconfig(self.display_grid[grid_x][grid_y], fill=self.colors[self.cursor_color_bar.get()])

            # if color has changed
            if color1 != self.canvas.itemcget(self.display_grid[grid_x][grid_y], 'fill'):
                # update grid
                self.grid_saved[grid_x][grid_y] = self.cursor_color_bar.get()
                new_sg = self.imager.update_semigraphical(self.grid_saved, grid_x, grid_y)
                self.minitel.move_cursor(grid_x // 2 + 1, grid_y // 3 + 1)
                self.minitel.write_semigraphical(new_sg[0], int(new_sg[1]), int(new_sg[2]))

    def run(self):
        self.canvas.bind("<B1-Motion>", self._on_mouse_click)
        self.app.mainloop()
