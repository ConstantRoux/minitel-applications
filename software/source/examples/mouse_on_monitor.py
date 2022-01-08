# +------------------------------------------------------+ #
# | Title: mouse_on_monitor.py                           | #
# | Author: Constant ROUX                                | #
# | Date: 01 / 01 / 2022                                 | #
# | Contents : A file example which creates a mouse for  | #
# | the Minitel 2 Alcatel.                               | #
# +------------------------------------------------------+ #

import pyautogui
import ctypes
from serial.serialutil import SerialException
from software.source.Minitel import Minitel


def main():
    # create the Minitel object connected on the COM5 at 1200 bauds by default
    minitel = None

    try:
        minitel = Minitel('COM5')
    except SerialException:
        print("Error opening Minitel communication.")
        exit()

    # change the baudrate communication of the source from 1200 to 9600
    minitel.set_baudrate(9600)

    # reset the Minitel screen
    minitel.start_new_screen()

    # activate the source cursor
    minitel.active_cursor(True)

    # get the active window size
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    print("Press Ctrl-C to terminate while statement")
    try:
        while True:
            minitel.move_cursor(int(pyautogui.position().x / screensize[0] * 40),
                                int(pyautogui.position().y / screensize[1] * 25))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
