#!/usr/bin/env python
import PySimpleGUI as sg
import cv2 as cv

"""
Demo program to open and play a file using OpenCV
It's main purpose is to show you:
1. How to get a frame at a time from a video file using OpenCV
2. How to display an image in a PySimpleGUI Window
For added fun, you can reposition the video using the slider.
"""


def load_video(filename):
    if filename is None:
        return
    vidFile = cv.VideoCapture(filename)
    # ---===--- Get some Stats --- #
    num_frames = vidFile.get(cv.CAP_PROP_FRAME_COUNT)
    fps = vidFile.get(cv.CAP_PROP_FPS)
    return vidFile, num_frames, fps


def frame_videoplayer(num_frames):
    # ---===--- define the window layout --- #
    layout = [
        [sg.Text("OpenCV Demo", size=(15, 1), font="Helvetica 20")],
        [sg.Image(filename="", key="-image-")],
        [
            sg.Slider(
                range=(0, num_frames), size=(60, 10), orientation="h", key="-slider-"
            )
        ],
        [sg.Button("Exit", size=(7, 1), pad=((600, 0), 3), font="Helvetica 14")],
    ]
    frame_video_player = sg.Frame("Video Player", layout)

    return frame_video_player


def events_videoplayer(window, vidFile, cur_frame):
    if vidFile.isOpened():
        event, values = window.read(timeout=0)
        if event in ("Exit", None):
            return cur_frame, True
        ret, frame = vidFile.read()
        if not ret:  # if out of data stop looping
            return cur_frame, True
        # if someone moved the slider manually, the jump to that frame
        if int(values["-slider-"]) != cur_frame - 1:
            cur_frame = int(values["-slider-"])
            vidFile.set(cv.CAP_PROP_POS_FRAMES, cur_frame)
        window["-slider-"].update(cur_frame)
        cur_frame += 1

        imgbytes = cv.imencode(".png", frame)[1].tobytes()  # ditto
        window["-image-"].update(data=imgbytes)
        return cur_frame, False


def main():
    filename = r"C:\Users\Baerwolff\Desktop\Lenovo_Arbeit\2020-02-20_Validierungsmessung_Radeberg\Videos\raspberrypi_FR20_2020-02-20_12-00-00.flv"
    vidFile, num_frames, fps = load_video(filename)
    layout = [[frame_videoplayer(num_frames=num_frames)]]
    window = sg.Window(
        "Demo Application - OpenCV Integration",
        layout,
        no_titlebar=False,
        location=(0, 0),
    )

    # locate the elements we'll be updating. Does the search only 1 time
    # image_elem = window["-image-"]
    # slider_elem = window["-slider-"]

    # ---===--- LOOP through video file by frame --- #
    cur_frame = 0
    stop_gui = False
    while not stop_gui:
        cur_frame, stop_gui = events_videoplayer(window, vidFile, cur_frame)


if __name__ == "__main__":
    main()


# This was another way updates were being done, but seems slower than the above
# img = Image.fromarray(frame)    # create PIL image from frame
# bio = io.BytesIO()              # a binary memory resident stream
# img.save(bio, format= 'PNG')    # save image as png to it
# imgbytes = bio.getvalue()       # this can be used by OpenCV hopefully
# image_elem.update(data=imgbytes)
