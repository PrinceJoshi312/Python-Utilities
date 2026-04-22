# Usage

1. Install dependencies:

```bash
pip install pdfkit
```

2. Install **wkhtmltopdf** (required):

* Windows: [https://wkhtmltopdf.org/downloads.html](https://wkhtmltopdf.org/downloads.html)
* Linux/macOS: `sudo apt install wkhtmltopdf`

3. Run the script:

```bash
python webpage_to_pdf.py
```

4. Follow prompts:

```
Enter the webpage URL: https://example.com
Enter output folder (default=downloads):
Enter output filename (optional, default=derived from URL):
```

✅ Result: The webpage is saved as a PDF in your chosen folder.

---

Install wkhtmltopdf
Windows

Download the installer: https://wkhtmltopdf.org/downloads.html

Install it (keep default settings).

Make sure the path to wkhtmltopdf.exe is added to your system PATH:

Press Win + R → type sysdm.cpl → Advanced → Environment Variables

Under System variables → Path → Edit → Add the folder containing wkhtmltopdf.exe

Open a new terminal and test:

wkhtmltopdf --version


You should see a version number.

Linux / macOS
# Ubuntu/Debian
sudo apt install wkhtmltopdf

# MacOS with Homebrew
brew install wkhtmltopdf

2️⃣ Optional: Specify the path manually in Python

If wkhtmltopdf is installed but not in PATH, you can tell pdfkit where it is:

import pdfkit

config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
pdfkit.from_url("https://example.com", "output.pdf", configuration=config)



Replace the path with your actual wkhtmltopdf.exe location.
