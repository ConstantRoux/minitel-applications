# +------------------------------------------------------+ #
# | Title: video_to_semigraphical.py                     | #
# | Author: Constant ROUX                                | #
# | Date: 01 / 01 / 2022                                 | #
# | Contents : A file example which display a video on   | #
# | the Minitel 2 Alcatel.                               | #
# +------------------------------------------------------+ #

from serial import SerialException

from software.source.Imager import Imager
from software.source.VideoToSemiGraphical import VideoToSemiGraphical
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

    # change Minitel mode to semi-graphic mode
    minitel.set_mode(1)

    video_to_sg = VideoToSemiGraphical("C:/Users/Constant/Desktop/projects/minitel/software/assets/rubiks_cube.mp4", 50)
    video_to_sg.convert_video_to_sg()

    # frame by frame
    for j in range(len(video_to_sg.diff_list_video)):
        for i in range(len(video_to_sg.diff_list_video[j])):
            if video_to_sg.diff_list_video[j]:
                minitel.move_cursor(video_to_sg.diff_list_video[j][i][0],
                                    video_to_sg.diff_list_video[j][i][1])

                minitel.write_semigraphical(video_to_sg.diff_list_video[j][i][2],
                                            video_to_sg.diff_list_video[j][i][3],
                                            video_to_sg.diff_list_video[j][i][4])


if __name__ == "__main__":
    main()
