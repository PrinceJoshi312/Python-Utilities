from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import os
import re

# Brave executable path
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

# Create "urls" folder in current script directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAVE_FOLDER = os.path.join(BASE_DIR, "urls")
os.makedirs(SAVE_FOLDER, exist_ok=True)

# Attach to running Brave
options = webdriver.ChromeOptions()
options.binary_location = BRAVE_PATH
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

try:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
except WebDriverException:
    print("Brave is not running with remote debugging enabled")
    exit()

video_url = None
video_title = None

# Find any YouTube video tab
for handle in driver.window_handles:
    driver.switch_to.window(handle)
    url = driver.current_url

    if "youtube.com/watch?v=" in url or "/shorts/" in url:
        video_url = url
        video_title = driver.title
        break

if video_url:
    safe_title = re.sub(r'[\\/*?:"<>|]', "", video_title)
    file_path = os.path.join(SAVE_FOLDER, f"{safe_title}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(video_url)

    print(f"Saved → {file_path}")
else:
    print("No YouTube video tab open")

driver.quit()
