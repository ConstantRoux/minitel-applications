# +------------------------------------------------------+ #
# | Title: Imager.py                                     | #
# | Author: Constant ROUX                                | #
# | Date: 30 / 12 / 2021                                 | #
# | Contents : A class file to manipulate and transform  | #
# | an image in a semi graphic image                     | #
# +------------------------------------------------------+ #

import cv2
import statistics

class Imager:
    def __init__(self, path):
        self.image = cv2.imread(path, cv2.IMREAD_COLOR)
        if self.image is None:
            print("File at " + path + " doesn't exist or can't be read as an image.")
            raise

    def _resize_image(self, width):
        height = self.image.shape[0] * (width / self.image.shape[1])
        dim = (int(width), int(height))
        self.image = cv2.resize(self.image, dim, interpolation=cv2.INTER_AREA)

        cv2.imwrite("test/test_scaling.jpg", self.image)
    
    def _set_image_gray(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("test/test_gray_conversion.jpg", self.image)
    
    def _crop_image_2b6(self):
        height, width, channel = self.image.shape
        self.image = self.image[0:height - height % 3, 0:width - width % 2]

        cv2.imwrite("test/test_crope.jpg", self.image)

    def _create_semigraphical_image(self):
        list = [] # value, fore, back
        height, width = self.image.shape

        for i in range(0, height, 3):
            for j in range(0, width, 2):
                background_mean = 0
                foreground_mean = 0
                general_mean = 0
                general = []
                background = []
                foreground = []

                for n in range(3):
                    for m in range(2):
                        general.append(self.image[i + n, j + m])
                
                general_mean = int(statistics.mean(general))

                for n in range(3):
                    for m in range(2):
                        if self.image[i + n, j + m] <= general_mean:
                            background.append(self.image[i + n, j + m])
                        else:
                            foreground.append(self.image[i + n, j + m])
                            
                
                if background and foreground:
                    background_mean = statistics.mean(background)
                    foreground_mean = statistics.mean(foreground)
                elif background and not foreground:
                    background_mean = statistics.mean(background)
                    foreground_mean = background_mean
                else:
                    foreground_mean = statistics.mean(foreground)
                    background_mean = foreground_mean

                mask = 0x01
                value = 0x00

                for n in range(3):
                    for m in range(2):
                        if self.image[i + n, j + m] > general_mean:
                            self.image[i + n, j + m] = foreground_mean
                            value |= mask
                        else:
                            self.image[i + n, j + m] = background_mean   

                        mask <<= 1
                        if(mask == 0x20):
                            value |= mask
                            mask <<= 1               
                list.append((value.to_bytes(1, byteorder="big"), foreground_mean, background_mean))
            list.append((b'\n\r', foreground_mean, background_mean))
                  
        return list 
                                         
    def _level_gray_image(self, level):
        rows, cols = self.image.shape
        for i in range(rows):
            for j in range(cols):
                self.image[i][j] = self.image[i][j] / 255.0 * (level - 1)
        
        cv2.imwrite("test/test_leveling.jpg", self.image)

    def convert_image_to_semigraphical(self, width):
        self._resize_image(width)
        self._crop_image_2b6()
        self._set_image_gray()
        self._level_gray_image(8)
        return self._create_semigraphical_image()