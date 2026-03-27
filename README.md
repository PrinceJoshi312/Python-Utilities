# Python Utilities 🐍

A collection of **practical Python scripts** for automation, scraping, media processing, and productivity.
Each folder is a **self-contained utility** designed to solve a specific everyday task.

---

## 📦 Available Utilities

| Folder            | Description                                |
| ----------------- | ------------------------------------------ |
| `Filesorter`      | Automatically organizes files by type      |
| `audio_extractor` | Extract audio from videos (YouTube & more) |
| `emailAutomation` | Automate email sending workflows           |
| `url_extractor`   | Extract URLs from text or web content      |
| `url_to_img`      | Convert webpage/URL into image             |
| `url_to_video`    | Download videos using yt-dlp + ffmpeg      |
| `web_scraper`     | Scrape content from websites               |
| `webpage_to_pdf`  | Convert webpages to PDF                    |
| `websearch`       | Simple web search automation tool          |

---

## 🚀 Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/PrinceJoshi312/Python-Utilities.git
cd Python-Utilities
```

---

### 2. Navigate to Any Utility

Each utility runs independently:

```bash
cd folder_name
python script.py
```

Example:

```bash
cd url_to_video
python downloader.py
```

---

## ⚙️ Requirements

* Python 3.8+
* pip
* Some utilities require additional dependencies
* Some utilities require external tools like:

  * **FFmpeg**
  * **yt-dlp**
  * Browser drivers (for scraping)

Install dependencies if available:

```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure

```
Python-Utilities/
│
├── Filesorter/
├── audio_extractor/
├── emailAutomation/
├── url_extractor/
├── url_to_img/
├── url_to_video/
├── web_scraper/
├── webpage_to_pdf/
├── websearch/
└── README.md
```

---

## 🧠 Usage Pattern

Most utilities follow this pattern:

1. Navigate to folder
2. Configure variables (if required)
3. Run script
4. Output generated automatically

---

## ⚠️ Important Notes

* Some scripts require **FFmpeg installed**
* Windows users should use **raw paths** (`r"C:\path"`)
* Ensure external tools are either:

  * added to PATH
  * OR provided directly in script

---

## 🛠️ Purpose

This repository is designed for:

* automation tasks
* quick utilities
* scraping workflows
* media processing
* productivity scripting

---

## 📈 Future Additions

* CLI wrappers
* unified launcher
* shared requirements
* GUI versions

---

## 🤝 Contributing

Feel free to:

* fork the repo
* improve scripts
* add new utilities
* submit pull requests

---

## 📜 License

MIT License © PrinceJoshi
