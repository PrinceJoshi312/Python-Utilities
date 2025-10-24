import yt_dlp
import os

def extract_audio(url, output_path="audio", audio_format="mp3", download_playlist=False):
    """
    Extract audio from a video or playlist using yt-dlp.

    Args:
        url (str): The video or playlist URL.
        output_path (str): Directory to save audio files.
        audio_format (str): Audio format (mp3, wav, etc.).
        download_playlist (bool): Whether to download entire playlist.
    """
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'noplaylist': not download_playlist,  # ✅ Toggle based on user input
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': audio_format,
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            
            # For playlist: no single filename
            if 'entries' in info:
                print(f"\n✅ Downloaded {len(info['entries'])} tracks to '{output_path}'")
                return output_path
            else:
                filename = ydl.prepare_filename(info)
                base_filename = os.path.splitext(filename)[0]
                audio_filename = f"{base_filename}.{audio_format}"
                print(f"\n✅ Audio extracted successfully: {audio_filename}")
                return audio_filename
    except Exception as e:
        print(f"\n❌ Error extracting audio: {e}")
        return None


if __name__ == "__main__":
    video_url = input("🎥 Enter the video or playlist URL: ").strip()
    audio_format = input("🎧 Enter audio format (mp3/wav/m4a, default=mp3): ").strip() or "mp3"
    output_path = input("📁 Enter output folder (default=downloads): ").strip() or "downloads"

    choice = input("🟡 Do you want to download (v) current video or (p) full playlist? [v/p]: ").strip().lower()
    download_playlist = True if choice == 'p' else False

    extract_audio(video_url, output_path=output_path, audio_format=audio_format, download_playlist=download_playlist)
