# +------------------------------------------------------+ #
# | Title: image_to_semigraphic.py                       | #
# | Author: Constant ROUX                                | #
# | Date: 30 / 12 / 2021                                 | #
# | Contents : A file example which prints a given image | #
# | on a Minitel 2 Alcatel in the semi graphic mode      | #
# +------------------------------------------------------+ #

from serial.serialutil import SerialException
from software.source.objects.Imager import Imager
from software.source.objects.Minitel import Minitel


def main():
    # create the Minitel object connected on the COM5 at 1200 bauds by default
    minitel = None

    try:
        minitel = Minitel('COM5')
    except SerialException:
        print("Error opening Minitel communication.")
        exit()

    # create the image converter (here example image is in assets folder)
    image_converter = None

    try:
        image_converter = Imager("../../assets/happy.jpg")
    except:
        print("Error opening the image.")
        exit()

    # change the baudrate communication of the source from 1200 to 9600
    minitel.set_baudrate(9600)

    # reset the Minitel screen
    minitel.start_new_screen()

    # change Minitel mode to semi-graphic mode
    minitel.set_mode(1)

    # convert classic image to semi-graphic image (max size parameter for Minitel is 79)
    sg_image = image_converter.convert_image_to_semigraphical(58)

    # print the semi-graphical image on Minitel char by char
    for i in range(len(sg_image)):
        minitel.write_semigraphical(sg_image[i][0], sg_image[i][1], sg_image[i][2])


if __name__ == "__main__":
    main()
