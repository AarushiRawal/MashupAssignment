import sys
import os
import yt_dlp
from moviepy.editor import VideoFileClip
from pydub import AudioSegment

# -------------------------
# Check Command Line Inputs
# -------------------------

if len(sys.argv) != 5:
    print("Usage: python <program.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
    sys.exit(1)

singer = sys.argv[1]

try:
    num_videos = int(sys.argv[2])
    duration = int(sys.argv[3])
except ValueError:
    print("Number of videos and duration must be integers")
    sys.exit(1)

output_file = sys.argv[4]

if num_videos <= 10:
    print("Number of videos must be greater than 10")
    sys.exit(1)

if duration <= 20:
    print("Duration must be greater than 20 seconds")
    sys.exit(1)

# -------------------------
# Create Folders
# -------------------------

os.makedirs("videos", exist_ok=True)
os.makedirs("audios", exist_ok=True)
os.makedirs("trimmed", exist_ok=True)

# -------------------------
# Download Videos
# -------------------------

def download_videos():
    search_query = f"ytsearch{num_videos}:{singer} songs"

    ydl_opts = {
        'format': 'best',
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

# -------------------------
# Convert to Audio
# -------------------------

def convert_to_audio():
    for file in os.listdir("videos"):
        if file.endswith(".mp4"):
            video_path = os.path.join("videos", file)
            audio_path = os.path.join("audios", file.replace(".mp4", ".mp3"))

            video = VideoFileClip(video_path)
            video.audio.write_audiofile(audio_path)
            video.close()

# -------------------------
# Trim Audio
# -------------------------

def trim_audio():
    for file in os.listdir("audios"):
        if file.endswith(".mp3"):
            audio_path = os.path.join("audios", file)
            trimmed_path = os.path.join("trimmed", file)

            sound = AudioSegment.from_mp3(audio_path)
            trimmed = sound[:duration * 1000]
            trimmed.export(trimmed_path, format="mp3")

# -------------------------
# Merge Audio
# -------------------------

def merge_audio():
    combined = AudioSegment.empty()

    for file in os.listdir("trimmed"):
        if file.endswith(".mp3"):
            audio_path = os.path.join("trimmed", file)
            sound = AudioSegment.from_mp3(audio_path)
            combined += sound

    combined.export(output_file, format="mp3")

# -------------------------
# Main Execution
# -------------------------

try:
    print("Downloading videos...")
    download_videos()

    print("Converting to audio...")
    convert_to_audio()

    print("Trimming audio...")
    trim_audio()

    print("Merging audio...")
    merge_audio()

    print("Mashup created successfully:", output_file)

except Exception as e:
    print("An error occurred:", e)
