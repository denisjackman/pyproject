''' extra audio from movie files '''

import moviepy
import moviepy.editor

VIDEO_FILE = "G:\\MA Leadership\\dissertation\\data\\Store\\DJ-YC-Video-2022"\
             "0902.mp4"
AUDIO_FILE = "Z:\\Store\\audio.mp3"


def main():
    ''' main '''
    video = moviepy.editor.VideoFileClip(VIDEO_FILE)
    audio = video.audio
    audio.write_audiofile(AUDIO_FILE)


if __name__ == "__main__":
    main()
