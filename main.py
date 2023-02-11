import moviepy.editor
from pathlib import Path
from pyfiglet import Figlet

"""Программа вырезает из видео аудио дорожку и создает
    mp3 файл из видео"""


def cut_audio_from_video(name):
    video_file = Path(name)
    video = moviepy.editor.VideoFileClip(video_file)
    audio = video.audio
    audio.write_audiofile(f'{video_file.stem}.mp3')

if __name__ == "__main__":
    preview_text = Figlet(font='slant')
    print(preview_text.renderText("AUDIO CUTTER"))
    video_file_name = input("Please put here video file adress ...")
    cut_audio_from_video(video_file_name)
