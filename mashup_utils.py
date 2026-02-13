import os
import yt_dlp
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

def download_videos(singer, num_videos):
    os.makedirs("videos", exist_ok=True)

    search_query = f"ytsearch{num_videos}:{singer} songs"

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


def convert_to_audio():
    os.makedirs("audios", exist_ok=True)

    for file in os.listdir("videos"):
        if file.endswith(".mp4"):
            video_path = os.path.join("videos", file)
            audio_path = os.path.join("audios", file.replace(".mp4", ".mp3"))

            video = VideoFileClip(video_path)
            video.audio.write_audiofile(audio_path)
            video.close()


def trim_audio(duration):
    os.makedirs("trimmed", exist_ok=True)

    for file in os.listdir("audios"):
        if file.endswith(".mp3"):
            audio_path = os.path.join("audios", file)
            trimmed_path = os.path.join("trimmed", file)

            sound = AudioSegment.from_mp3(audio_path)
            trimmed = sound[:duration * 1000]
            trimmed.export(trimmed_path, format="mp3")


def merge_audio(output_file):
    combined = AudioSegment.empty()

    for file in os.listdir("trimmed"):
        if file.endswith(".mp3"):
            audio_path = os.path.join("trimmed", file)
            sound = AudioSegment.from_mp3(audio_path)
            combined += sound

    combined.export(output_file, format="mp3")
