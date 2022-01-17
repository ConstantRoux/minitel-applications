from serial.serialutil import SerialException
from source.objects.Minitel import Minitel
from source.objects.MinitelDrawer import MinitelDrawer


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

    # change Minitel mode to semi-graphic mode
    minitel.set_mode(1)

    # deactivate cursor display
    minitel.active_cursor(False)

    # create the Minitel drawer
    drawer = MinitelDrawer(minitel)

    # start the drawer
    drawer.run()


if __name__ == "__main__":
    main()
