import pdfkit
import os
import shutil

def get_wkhtmltopdf_config():
    """
    Detects wkhtmltopdf executable.
    Returns a pdfkit configuration object or None if not found.
    """
    # Try to find in PATH
    path = shutil.which("wkhtmltopdf")
    if path:
        return pdfkit.configuration(wkhtmltopdf=path)
    
    # If not found, ask user to enter path manually
    print("\n❌ wkhtmltopdf executable not found!")
    print("Please install wkhtmltopdf from: https://wkhtmltopdf.org/downloads.html")
    print("Or enter the full path to wkhtmltopdf executable manually.")
    manual_path = input("Enter wkhtmltopdf path (or leave blank to exit): ").strip()
    if manual_path:
        if os.path.exists(manual_path):
            return pdfkit.configuration(wkhtmltopdf=manual_path)
        else:
            print("❌ The path you entered does not exist. Exiting.")
            return None
    else:
        return None

def webpage_to_pdf(url, output_folder="downloads", output_filename=None):
    """
    Convert a webpage to a PDF file.
    """
    os.makedirs(output_folder, exist_ok=True)

    # Derive filename if not provided
    if not output_filename:
        sanitized_url = url.replace("https://", "").replace("http://", "").replace("/", "_")
        output_filename = f"{sanitized_url}.pdf"

    output_path = os.path.join(output_folder, output_filename)

    config = get_wkhtmltopdf_config()
    if not config:
        print("\n❌ Cannot convert webpage to PDF without wkhtmltopdf. Exiting.")
        return None

    try:
        pdfkit.from_url(url, output_path, configuration=config)
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
