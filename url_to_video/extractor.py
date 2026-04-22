import subprocess
import os

VIDEO_URL = "YOUR_PATH_HERE"

DOWNLOAD_DIR = r"YOUR_DOWNLOAD_FOLDER_PATH_HERE" 
# '''you can also place the folder in the same file structure'''

FFMPEG_PATH = (
    r"YOUR_FFMPEG_PATH_HERE\ffmpeg-8.0.1-essentials_buil"
    r"\ffmpeg-8.0.1-essentials_build\bin"
)

os.makedirs(DOWNLOAD_DIR, exist_ok=True)

cmd = [
    "yt-dlp",
    "--ffmpeg-location", FFMPEG_PATH,
    "-f", "bv*+ba/b",
    "--merge-output-format", "mp4",
    "--force-overwrites",
    "-o", os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s"),
    VIDEO_URL
]

print("⬇ Downloading video WITH audio (forced ffmpeg)...")
subprocess.run(cmd, check=True)
print("✅ DONE — video has audio")
