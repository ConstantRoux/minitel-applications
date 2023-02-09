# +----------------------------------------------------------+ #
# | Title: Minitel.py                                        | #
# | Author: Constant ROUX                                    | #
# | Reference : https://github.com/eserandour/Minitel1B_Hard | #
# | Date: 30 / 12 / 2021                                     | #
# | Contents : A class file to use necessary features of the | # 
# | Minitel 2 Alcatel to print image in semi graphic mode    | #
# +----------------------------------------------------------+ #

import time
import serial
from serial.serialutil import SerialException


class Minitel:
    # socket constants
    PROG = b'\x6B'
    SPEED_STATUS = b'\x74'

    # cursor
    CON = b'\x11'
    COFF = b'\x14'

    # screen constants
    CSI = "1B5B"
    FF = b'\x0C'

    # gray levels constants
    GRAY_FOREGROUND_HEXACODE = [b'\x47',
                                b'\x43',
                                b'\x46',
                                b'\x42',
                                b'\x45',
                                b'\x41',
                                b'\x44',
                                b'\x40']

    GRAY_BACKGROUND_HEXACODE = [b'\x57',
                                b'\x53',
                                b'\x56',
                                b'\x52',
                                b'\x55',
                                b'\x51',
                                b'\x54',
                                b'\x50']

    # extension constants
    SI = b'\x0F'
    SO = b'\x0E'
    ESC = b'\x1B'

    # buzzer constant
    BUZZER = b'\x07'

    def __init__(self, port):
        try:
            self.port = port
            self.minitel_com = serial.Serial(port=port, baudrate=1200, parity=serial.PARITY_EVEN,
                                             bytesize=serial.SEVENBITS, stopbits=serial.STOPBITS_ONE, timeout=None)
        except SerialException:
            print("Error opening port " + port + " at " + str(1200) + " bauds.")
            raise
        self.minitel_com.reset_output_buffer()

    def write_byte(self, byte):
        self.minitel_com.write(byte)

    def write_word(self, word):
        self.minitel_com.write(word)

    def write_bytes_PRO(self, n):
        self.write_byte(self.ESC)
        if n == 1:
            self.write_byte(b'\x39')
        elif n == 2:
            self.write_byte(b'\x3A')
        elif n == 3:
            self.write_byte(b'\x3B')
        else:
            print(n + " PRO value not supported")

    def write_bytes_p(self, n):
        if n <= 9:
            self.write_byte(bytes([48 + n]))
        else:
            self.write_byte(bytes([48 + n // 10]))
            self.write_byte(bytes([48 + n % 10]))

    def write_semigraphical(self, sg_code, foreground, background):
        self.color_semigraphical(self.GRAY_BACKGROUND_HEXACODE[7 - background],
                                 self.GRAY_FOREGROUND_HEXACODE[7 - foreground])
        if sg_code != b'\x20':
            self.write_byte(sg_code)
        else:
            self.write_byte(b'\x5f')

    def set_baudrate(self, baudrate):
        sg_list = [300, 1200, 4800, 9600]
        if baudrate not in sg_list:
            print("Baudrate " + str(baudrate) + " not supported. Set to default.")
            baudrate = 1200

        self.write_bytes_PRO(2)
        self.write_byte(self.PROG)

        if baudrate == 300:
            self.write_byte(b'\x52')
        elif baudrate == 1200:
            self.write_byte(b'\x7F')
        elif baudrate == 4800:
            self.write_byte(b'\x7F')
        else:
            self.write_byte(b'\x7F')

        self.minitel_com.close()

        time.sleep(1)  # sleep is necessary on Linux

        try:
            self.minitel_com = serial.Serial(port=self.port, baudrate=baudrate, parity=serial.PARITY_EVEN,
                                             bytesize=serial.SEVENBITS, stopbits=serial.STOPBITS_ONE, timeout=None)
        except SerialException:
            print("Error opening port " + self.port + " at " + str(baudrate) + " bauds.")

    def read(self):
        return self.minitel_com.read().decode("utf-8")

    def read_string(self, size):
        return self.minitel_com.read(size).decode("utf-8")

    def set_mode(self, n):
        # graphical mode
        if n == 1:
            self.write_byte(self.SO)
        # text mode
        elif n == 2:
            self.write_byte(self.SI)
        else:
            print("Mode not supported.")

    def clear_screen(self):
        self.write_word(bytearray.fromhex(self.CSI))
        self.write_byte(b'\x32')
        self.write_byte(b'\x4A')

    def start_new_screen(self):
        self.write_byte(self.FF)

    def active_cursor(self, cursor):
        if cursor:
            self.write_byte(self.CON)
        else:
            self.write_byte(self.COFF)

    def move_cursor(self, x, y):
        self.write_word(bytearray.fromhex(self.CSI))
        self.write_bytes_p(y)
        self.write_byte(b'\x3B')
        self.write_bytes_p(x)
        self.write_byte(b'\x48')

    def buzz(self):
        self.write_byte(self.BUZZER)

    def color_foreground(self, level):
        self.write_byte(self.ESC)
        self.write_byte(level)

    def color_background(self, level):
        self.write_byte(self.ESC)
        self.write_byte(level)

    def color_semigraphical(self, back_level, fore_level):
        self.color_background(back_level)
        self.color_foreground(fore_level)
