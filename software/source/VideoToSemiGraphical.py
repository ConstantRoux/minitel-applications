# +----------------------------------------------------------+ #
# | Title: Minitel.py                                        | #
# | Author: Constant ROUX                                    | #
# | Date: 30 / 12 / 2021                                     | #
# | Contents : A class file to manipulate video and          | #
# | transform it in semigraphical characters variations for  | #
# | the Minitel 2 Alcatel to print image in semi graphic mode| #
# +----------------------------------------------------------+ #

import cv2
from .Imager import Imager


class VideoToSemiGraphical:
    def __init__(self, path, width):
        self._capture = None
        self.diff_list_video = []
        self._open_video_capture(path)
        self._width = width
        self._height = int(self._capture.get(4) * (self._width / self._capture.get(3)))
        self.length = self._get_video_length()

    def _open_video_capture(self, path):
        self._capture = cv2.VideoCapture(path)
        if not self._capture.isOpened():
            print("Error opening video file", end="")
            while not self._capture.isOpened():
                cv2.waitKey(1000)
                print(".", end="")
            print()

    def _close_video_capture(self):
        self._capture.release()

    def _convert_frame_to_sg(self, frame):
        imager = Imager(None, "image_drawer")
        imager.image = frame
        return imager.convert_image_to_semigraphical(self._width)

    def _compare_list(self, old_list, new_list):
        diff_list = []
        for i in range(self._height // 3):  # heigth
            for j in range(self._width // 2):  # width
                if old_list[j + i * (self._width // 2)] != new_list[j + i * (self._width // 2)]:
                    diff_list.append((j + 1,
                                      i + 1,
                                      new_list[j + i * (self._width // 2)][0],
                                      new_list[j + i * (self._width // 2)][1],
                                      new_list[j + i * (self._width // 2)][2]))

        return diff_list

    def _get_video_length(self):
        return int(self._capture.get(cv2.CAP_PROP_FRAME_COUNT))

    def convert_video_to_sg(self):
        old_sg_list = []

        if self._capture.isOpened():
            ret, frame = self._capture.read()
            if ret:
                old_sg_list = self._convert_frame_to_sg(frame)

        for i in range(len(old_sg_list)):
            y = list(old_sg_list[i])
            y[2] += 10
            old_sg_list[i] = y

        for i in range(self.length):
            if self._capture.isOpened():
                ret, frame = self._capture.read()
                if ret:
                    new_sg_list = self._convert_frame_to_sg(frame)
                    self.diff_list_video.append(self._compare_list(old_sg_list, new_sg_list))
                    old_sg_list = new_sg_list.copy()

        self._close_video_capture()
