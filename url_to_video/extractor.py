import subprocess
import os

VIDEO_URL = "https://www.youtube.com/shorts/SBlJGQc-cUg"

DOWNLOAD_DIR = r"C:\Users\HP\OneDrive\Desktop\websearch\downloads"

FFMPEG_PATH = (
    r"C:\Users\HP\OneDrive\Pictures\ffmpeg-8.0.1-essentials_build"
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
