import requests
from bs4 import BeautifulSoup

def scrape_website(url, element_tag="p", class_name=None):
    """
    Scrape a website and extract specific elements.

    Args:
        url (str): The website URL to scrape.
        element_tag (str): HTML tag to extract (default: "p").
        class_name (str, optional): Specific class to filter by.

    Returns:
        list: List of extracted text elements.
    """
    try:
        # Fetch the webpage
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Find elements
        if class_name:
            elements = soup.find_all(element_tag, class_=class_name)
        else:
            elements = soup.find_all(element_tag)

        # Extract text
        extracted = [el.get_text(strip=True) for el in elements]

        return extracted

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

if __name__ == "__main__":
    url = input("Enter website URL to scrape: ").strip()
    tag = input("Enter HTML tag to extract (default=p): ").strip() or "p"
    class_name = input("Enter class name to filter (optional): ").strip() or None

    data = scrape_website(url, element_tag=tag, class_name=class_name)

    if data:
        print(f"\nExtracted {len(data)} elements:\n")
        for i, text in enumerate(data, start=1):
            print(f"{i}. {text}")
    else:
        print("No data found or failed to scrape the site.")
