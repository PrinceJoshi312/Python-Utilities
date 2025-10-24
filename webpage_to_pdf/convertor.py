import pdfkit
import os

def webpage_to_pdf(url, output_folder="downloads", output_filename=None):
    """
    Convert a webpage to a PDF file.

    Args:
        url (str): URL of the webpage to convert.
        output_folder (str): Folder to save the PDF (default="downloads").
        output_filename (str): Name of the PDF file (default derived from URL).

    Returns:
        str: Path to the generated PDF file.
    """
    os.makedirs(output_folder, exist_ok=True)

    # Derive filename if not provided
    if not output_filename:
        sanitized_url = url.replace("https://", "").replace("http://", "").replace("/", "_")
        output_filename = f"{sanitized_url}.pdf"

    output_path = os.path.join(output_folder, output_filename)

    try:
        pdfkit.from_url(url, output_path)
        print(f"\n✅ Webpage successfully converted to PDF: {output_path}")
        return output_path
    except Exception as e:
        print(f"\n❌ Failed to convert webpage to PDF: {e}")
        return None


if __name__ == "__main__":
    print("🌐 Webpage to PDF Converter")
    url = input("Enter the webpage URL: ").strip()
    folder = input("Enter output folder (default=downloads): ").strip() or "downloads"
    filename = input("Enter output filename (optional, default=derived from URL): ").strip() or None

    webpage_to_pdf(url, output_folder=folder, output_filename=filename)
