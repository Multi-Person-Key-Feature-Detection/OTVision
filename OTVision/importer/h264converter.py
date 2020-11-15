# OTVision: Converts a h264 file to a different container format
# Copyright (C) 2020 OpenTrafficCam Contributors
# <https://github.com/OpenTrafficCam
# <team@opentrafficcam.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import subprocess
from pathlib import Path
from urllib.request import urlretrieve
from zipfile import ZipFile
from helpers.files import remove_dir

ffmpeg_url = "https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2020-11-14-12-28/ffmpeg-n4.3.1-25-g1936413eda-win64-gpl-4.3.zip"
ffmpeg_zip = "./ffmpeg.zip"
ffmpeg_dir = "./ffmpeg"
ffmpeg_exe = "./ffmpeg.exe"


def convert(
    path: str,
    filetype: str = "mkv",
    framerate: str = None,
    outputpath: str = None,
    overwrite: bool = False,
):
    # check if ffmpeg exists
    try:
        msg = subprocess.call("ffmpeg.exe")
    except FileNotFoundError:
        # download ffmpeg
        print("ffmpeg nicht da")
        download_ffmpeg()

    if Path(path).is_dir:
        pass
    elif Path(path).is_file:
        pass

    print("else")
    # download ffmpeg (license?)
    # check if path is file or dir
    # get framerate from filename, otherwise use framerate, otherwise use 20
    # save as/to outputpath or, if None, use filename of file
    # a. if file: call ffmpeg to convert path to filetype with framerate
    # b. if dir: call ffmpeg to concat and convert path to filetype with framerate
    # c. overwrite file if overwrite


def download_ffmpeg():
    try:
        urlretrieve(ffmpeg_url, ffmpeg_zip)
    except Exception as inst:
        print(inst)
        print("Can't download ffmpeg. Please download manual.")
    else:
        with ZipFile(ffmpeg_zip, "r") as zip:
            zip.extractall(ffmpeg_dir)
        for exe in Path(ffmpeg_dir).glob("**/ffmpeg.exe"):
            exe.replace(ffmpeg_exe)
        remove_dir(ffmpeg_dir)
        Path(ffmpeg_zip).unlink()


def get_fps(file: str, fps: int):
    fps = 20
    if "fps" in file:
        for filepart in file.split("_"):
            if "fps" in filepart:
                fps = filepart.split("fps")[0]
    print(fps)
    return fps
