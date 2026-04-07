# Advanced Local Business Scraper

A powerful Python-based tool designed to automate the collection of business leads from Google Maps using SerpApi. This script doesn't just pull basic info; it visits business websites to harvest contact emails and organizes everything into neatly categorized Excel files.

---

## 🚀 Features

* **Multi-Category Support:** Scrapes dozens of industries (hospitals, gyms, schools, etc.) in one go.
* **Email Enrichment:** Automatically crawls discovered websites to find contact email addresses.
* **Multithreaded:** Uses `ThreadPoolExecutor` to speed up email scraping.
* **Deduplication:** Ensures you don't get the same lead twice within a search.
* **Automated Organization:** Creates a folder for each category and names files based on the target location.
* **Excel Export:** Saves all data directly to `.xlsx` format for immediate use in CRM or outreach tools.

---

## 🛠️ Installation

1.  **Clone the repository** (or save the script to a folder).
2.  **Install the required dependencies:**
    ```bash
    pip install requests beautifulsoup4 openpyxl
    ```
3.  **Get a SerpApi Key:**
    * Sign up at [SerpApi](https://serpapi.com/).
    * Copy your API key.

---

## ⚙️ Configuration

Open the script and update the **EDITABLE PARAMETERS** section:

```python
# The target area for the search
LOCATION = "Haldwani, Uttarakhand, India"

# Your API key from SerpApi
SERPAPI_KEY = "YOUR_SERPAPI_KEY_HERE"

# How many results to fetch per category (max)
MAX_RESULTS_PER_CATEGORY = 200

# Number of concurrent threads for email scraping
THREADS = 8
```

---

## 📖 How to Use

1.  **Run the script:**
    ```bash
    python scraper_script.py
    ```
2.  **Monitor Progress:** The console will display which category is currently being scraped and when a file is saved.
3.  **Find your Data:** Results will appear in the `scraped_businesses/` directory, organized like this:
    ```text
    scraped_businesses/
    ├── restaurants/
    │   └── Haldwani_Uttarakhand_India.xlsx
    ├── hospitals/
    │   └── Haldwani_Uttarakhand_India.xlsx
    └── ...
    ```

---

## 📊 Data Captured

| Field | Description |
| :--- | :--- |
| **Name** | The official name of the business. |
| **Location** | Full physical address. |
| **Phone** | Contact phone number (if available). |
| **Website** | Official URL. |
| **Email** | Scraped email(s) found on the business website. |

---

## ⚠️ Important Notes

* **SerpApi Quota:** Each search consumes credits on your SerpApi account. Be mindful of the `MAX_RESULTS_PER_CATEGORY` setting.
* **Ethical Scraping:** This tool is for lead generation. Please ensure you comply with local laws (like GDPR or CAN-SPAM) when contacting businesses via scraped emails.
* **Website Blocking:** Some websites may block the scraper. The script includes a timeout and basic headers to minimize this, but it won't bypass advanced bot protections like Cloudflare.
