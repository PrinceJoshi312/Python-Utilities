import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse

def download_images(url, output_folder="images"):
    """
    Download all images from a webpage into a folder.

    Args:
        url (str): The webpage URL
        output_folder (str): Folder to save images

    Returns:
        int: Number of images downloaded
    """
    os.makedirs(output_folder, exist_ok=True)

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ Failed to fetch webpage: {e}")
        return 0

    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all("img")

    downloaded = 0
    urls_seen = set()

    for img in img_tags:
        img_url = img.get("src")
        if not img_url:
            continue

        # Convert relative URL to absolute
        img_url = urljoin(url, img_url)
        if img_url in urls_seen:
            continue
        urls_seen.add(img_url)

        # Create a filename from the URL
        parsed = urlparse(img_url)
        filename = os.path.basename(parsed.path)
        if not filename:
            filename = f"image_{downloaded + 1}.jpg"

        filepath = os.path.join(output_folder, filename)

        try:
            img_data = requests.get(img_url).content
            with open(filepath, "wb") as f:
                f.write(img_data)
            downloaded += 1
            print(f"✅ Downloaded: {filename}")
        except Exception as e:
            print(f"❌ Failed to download {img_url}: {e}")

    print(f"\n🌟 Total images downloaded: {downloaded}")
    return downloaded

if __name__ == "__main__":
    print("🖼️ Webpage Image Downloader")
    url = input("Enter the webpage URL: ").strip()
    folder = input("Enter folder to save images (default=images): ").strip() or "images"

    download_images(url, output_folder=folder)
