import tkinter
import numpy
from tkinter import *
from Imager import Imager

class MinitelDrawer:
    def __init__(self, minitel, grid_width=80, grid_height=75, levels=8, size_case=10):
        self.imager = Imager(None, mode="image_drawer")

        self.minitel = minitel

        self.grid_saved = numpy.empty(shape=(75, 80))
        self.grid_saved.fill(7)
        self.old_grid_saved = numpy.empty(shape=(75, 80))
        self.old_grid_saved.fill(7)

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
        self.canvas = tkinter.Canvas(self.app, width=self.grid_width * self.size_case, height=self.grid_height * self.size_case)
        self.canvas.grid(row=0, column=0, padx=20, pady=20)

        for i in range(self.grid_width):
            for j in range(self.grid_height):
                self.canvas.create_rectangle(   i * self.size_case,
                                                j * self.size_case,
                                                self.size_case * (i + 1),
                                                self.size_case * (j + 1),
                                                fill=self.colors[7],
                                                outline="")
        
        for i in range(self.grid_height//3):
            for j in range((self.grid_width)//2):
                if j == 39:
                    self.minitel.write_semigraphical(b'\n\r', 7, 7)    
                else:
                    self.minitel.write_semigraphical(b'\x5F', 7, 7)
        self.minitel.move_cursor(0, 0)    

    def _create_color_scale(self):
        self.cursor_color_bar = tkinter.Scale(self.app, 
                                        label='Couleur',
                                        from_=0,    
                                        to=self.levels-1, 
                                        sliderrelief='flat', 
                                        length=self.grid_height * self.size_case)
                                        
        self.cursor_color_bar.grid(row=0, column=1)
    
    def _compare_list(self, old_list, new_list):
        list = []
        for i in range(self.grid_height // 3):
            for j in range(self.grid_width // 2):
                if old_list[j + i * (self.grid_width // 2)] != new_list[j + i * (self.grid_width // 2)]:
                    list.append((j, i, new_list[j + i * (self.grid_width // 2)]))
        
        return list
  
    def _on_mouse_click(self, event):
        # update case of grid
        grid_x = event.x // self.size_case
        grid_y = event.y // self.size_case
        
        # check mouse position
        if not(grid_x < 0 or grid_x >= self.grid_width or grid_y < 0 or grid_y >= self.grid_height):
            

            self.canvas.create_rectangle(   grid_x * self.size_case,
                                            grid_y * self.size_case,
                                            self.size_case * (grid_x + 1),
                                            self.size_case * (grid_y + 1),
                                            fill=self.colors[self.cursor_color_bar.get()],
                                            outline="")
            
            # update list
            if self.grid_saved[grid_y][grid_x] != self.cursor_color_bar.get():
                self.grid_saved[grid_y][grid_x] = self.cursor_color_bar.get()
                list_comparison = self._compare_list(self.imager.convert_list_to_semigraphical(self.old_grid_saved), self.imager.convert_list_to_semigraphical(self.grid_saved))
                for i in range(len(list_comparison)):
                    self.minitel.move_cursor(list_comparison[i][0], list_comparison[i][1])
                    self.minitel.write_semigraphical(list_comparison[i][2][0], int(list_comparison[i][2][1]), int(list_comparison[i][2][2]))
                self.old_grid_saved = self.grid_saved.copy()
        
    def run(self):
        self.canvas.bind("<B1-Motion>", self._on_mouse_click)
        self.app.mainloop()