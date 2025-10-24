
# Python Utilities 🐍

Welcome to **Python Utilities** — a collection of handy Python scripts for everyday tasks, automation, and scraping.

This repository contains:

- **Audio Extractor** 🎵: Download audio from YouTube, Twitter, Instagram, and playlists.
- **Web Scraper** 🌐: Scrape text and links from websites, fully customizable.
- **File Sorter** 📂: Organize and sort files in directories automatically.
- **Other Utilities** 🛠️: Various Python scripts for productivity and automation.


## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher  
- Each utility may have its own dependencies listed in `requirements.txt`

### Clone this repository
```bash
git clone https://github.com/PrinceJoshi312/Python-Utilities.git
cd Python-Utilities
````

---

## 🛠️ Utilities Overview

### 1. Audio Extractor 🎵

Download audio from videos or playlists.

```bash
cd audio_extractor
pip install -r requirements.txt
python extractor.py
```

Follow the prompts to:

* Enter video or playlist URL
* Choose audio format (mp3/wav/m4a)
* Decide if you want the whole playlist or single video

**Note:** Make sure **FFmpeg** is installed on your system (required by yt-dlp).

---

### 2. Web Scraper 🌐

Scrape text or links from any website.

```bash
cd web_scraper
pip install -r requirements.txt
python scraper.py
```

* Enter the URL
* Enter the HTML tag to extract (default: `p`)
* Optionally enter a CSS class to filter elements
* Extracted content is printed in the console

---

### 3. File Sorter 📂

Automatically organize files in a directory by file type.

```bash
cd file_sorter
pip install -r requirements.txt
python sorter.py
```

* Enter the directory path you want to sort
* The script will create folders for each file type (Images, Documents, Videos, etc.)
* Files are moved into their respective folders

---

## 📦 Contributing

Contributions are welcome!

* Fork the repo
* Create a feature branch
* Submit a pull request

---

## ⚠️ Notes

* Some utilities require external programs (like **FFmpeg** for audio extractor).
* Ensure system paths are properly set if required.

---

## 📜 License

MIT License © PrinceJoshi
