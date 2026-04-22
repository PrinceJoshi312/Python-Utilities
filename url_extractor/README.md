📌 YouTube Video URL Extractor (Browser-Attached)

This script extracts the URL of an already open YouTube video tab from your browser and saves it as a .txt file inside the urls/ folder.

⚠️ Important:
For security reasons, modern browsers do not allow external programs to read open tabs unless the browser is started with remote debugging enabled.

This is expected behavior, not a bug.

✅ What this script does

Attaches to an already running browser

Finds an open YouTube video tab

Extracts the video URL

Saves it as a .txt file in urls/

Names the file using the video title

Exits immediately

📁 Folder Structure
url_extractor/
│
├─ vid_url_extractor.py
├─ README.md
└─ urls/
   └─ Video Title.txt

⚙️ Requirements

Python 3.9+

Packages:

pip install selenium webdriver-manager

🔴 Why Remote Debugging Is Required

Operating systems block programs from spying on browser tabs for privacy and security.

Remote debugging:

Opens a controlled DevTools port

Allows Selenium to attach safely

Does NOT bypass DRM

Does NOT download videos

Does NOT violate YouTube ToS

Without it, the script cannot work.

🌐 Browser Setup (Major Browsers)
🟢 Brave (Recommended)

Close all Brave windows, then start Brave using:

"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222


✅ Best stability
✅ Chromium-based
✅ Minimal Google background services

🟢 Google Chrome
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222


⚠️ Slightly less stable on newer versions
⚠️ More background services

🟢 Microsoft Edge
"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe" --remote-debugging-port=9222


✅ Works same as Chrome
✅ Preinstalled on Windows

🔴 Firefox (Limited Support)

Firefox does not allow attaching to an already running instance.

❌ Remote debugging attach: NOT supported
✅ Only works if Firefox is launched by Selenium itself

Because of this limitation, Firefox is not recommended for this workflow.

⭐ Best Practice (One-Time Setup)

To avoid running commands every time:

Create a desktop shortcut

Set target to (example for Brave):

"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" --remote-debugging-port=9222


Use only this shortcut to open your browser

Now the script will work every time.

▶️ How to Use the Script

Start your browser using the remote-debugging shortcut

Open YouTube

Play any video

Run:

python vid_url_extractor.py


Check the urls/ folder

🟢 Output Examples
When a video is open:
urls/My Favorite Coding Video.txt


Contents:

https://www.youtube.com/watch?v=VIDEO_ID

When no YouTube tab is open:
No YouTube video tab open

⚠️ Known Limitations

Cannot detect audio state reliably (browser security)

Cannot attach if browser was started normally

Does not extract stream/media URLs

Only reads page URL (safe & legal)