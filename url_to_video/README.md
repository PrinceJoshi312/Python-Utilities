# Video Downloader (yt-dlp + ffmpeg)

Simple Python script to download videos **with audio** using `yt-dlp` and `ffmpeg`.

## Requirements

Make sure the following are installed:

* Python 3.8+
* `yt-dlp`
* `ffmpeg`

---

## Installation

### 1. Install yt-dlp

```bash
pip install yt-dlp
```

### 2. Download ffmpeg

* Download from: https://www.gyan.dev/ffmpeg/builds/
* Extract the folder
* Copy the path to the `bin` directory

Example:

```
C:\ffmpeg\ffmpeg-8.0.1-essentials_build\bin
```

---

## Script Configuration

Update the following variables in the script:

### 1. Video URL

```python
VIDEO_URL = "YOUR_PATH_HERE"
```

Paste the video link here.

---

### 2. Download Directory

```python
DOWNLOAD_DIR = r"YOUR_DOWNLOAD_FOLDER_PATH_HERE"
```

Example:

```python
DOWNLOAD_DIR = r"C:\Users\YourName\Downloads"
```

---

### 3. FFMPEG Path

```python
FFMPEG_PATH = r"YOUR_FFMPEG_PATH_HERE"
```

Example:

```python
FFMPEG_PATH = r"C:\ffmpeg\ffmpeg-8.0.1-essentials_build\bin"
```

---

## Run the Script

```bash
python script.py
```

---

## Output

* Video will be downloaded in MP4 format
* Audio will be merged automatically
* File name will match the video title

---

## Important Notes

* Make sure `yt-dlp` is accessible in PATH
* Ensure `ffmpeg` path points to the **bin** folder
* Use raw string (`r"path"`) for Windows paths
* Script overwrites existing files with same name

---

## Features

* Downloads best video + audio
* Forces ffmpeg merge
* Saves as MP4
* Auto creates download folder
* Overwrites duplicates
* Works with most yt-dlp supported sites

---

## Example

```python
VIDEO_URL = "https://www.youtube.com/watch?v=example"
DOWNLOAD_DIR = r"C:\Users\HP\Downloads"
FFMPEG_PATH = r"C:\ffmpeg\ffmpeg-8.0.1-essentials_build\bin"
```

---

## Expected Console Output

```
⬇ Downloading video WITH audio (forced ffmpeg)...
✅ DONE — video has audio
```

