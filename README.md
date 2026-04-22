
# 🐍 Python Utilities  
A collection of practical Python scripts for automation, scraping, media processing, and productivity. Each folder is a **standalone tool** built to solve real-world tasks quickly and efficiently.

---

## 📦 Available Utilities

| Folder | Description |
|--------|------------|
| `API_KEY_TESTER` | Test and validate API keys across services |
| `Filesorter` | Automatically organize files by type |
| `audio_extractor` | Extract audio from videos (YouTube & more) |
| `emailAutomation` | Automate email sending workflows |
| `location_data_scraper` | Scrape location-based data from web sources |
| `url_extractor` | Extract URLs from text or web content |
| `url_to_img` | Convert webpage/URL into image |
| `url_to_video` | Download videos using `yt-dlp` + `ffmpeg` |
| `web_scraper` | Scrape structured/unstructured website data |
| `webpage_to_pdf` | Convert webpages into PDF files |
| `websearch` | Simple automated web search tool |

---

## 🚀 Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/PrinceJoshi312/Python-Utilities.git
cd Python-Utilities
````

### 2. Run Any Utility

Each tool is independent:

```bash
cd folder_name
python script.py
```

**Example:**

```bash
cd url_to_video
python extractor.py
```

---

## ⚙️ Requirements

* Python **3.8+**
* pip

Install dependencies (if available):

```bash
pip install -r requirements.txt
```

---

## 🔧 External Tools (Required for Some Scripts)

* **FFmpeg** (for media processing)
* **yt-dlp** (for video downloads)
* **Browser drivers** (for scraping automation)

👉 Make sure they are:

* Added to system **PATH**
* OR configured manually in scripts

---

## 📂 Project Structure

```
Python-Utilities/
│
├── API_KEY_TESTER/
├── Filesorter/
├── audio_extractor/
├── emailAutomation/
├── location_data_scraper/
├── url_extractor/
├── url_to_img/
├── url_to_video/
├── web_scraper/
├── webpage_to_pdf/
├── websearch/
│
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🧠 Usage Pattern

Most utilities follow a simple workflow:

1. Navigate to the folder
2. Configure inputs (if needed)
3. Run the script
4. Get output automatically

---

## ⚠️ Important Notes

* Some scripts require **FFmpeg installed**
* Use raw paths on Windows:

  ```python
  r"C:\path\to\file"
  ```
* Ensure dependencies/tools are properly set up before running

---

## 🛠️ Purpose

This repository is built for:

* ⚡ Automation tasks
* 🌐 Web scraping
* 🎬 Media processing
* 🧩 Quick utility scripts
* 🚀 Productivity workflows

---

## 📈 Future Improvements

* CLI-based unified tool
* Central launcher for all utilities
* Shared dependency management
* GUI versions for key tools

---

## 🤝 Contributing

Contributions are welcome:

* Fork the repo
* Improve existing tools
* Add new utilities
* Submit a pull request

---

## 📜 License

MIT License © PrinceJoshi 
