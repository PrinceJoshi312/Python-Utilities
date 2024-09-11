import os         # Import the os module for interacting with the operating system
import shutil     # Import the shutil module for high-level file operations like copying and moving files

# Set the path to the directory containing the files you want to organize
path = r'C:/Users/HP/OneDrive/Pictures/'

# Get a list of all files and directories in the specified path
file_names = os.listdir(path)

# Define the names of folders for categorizing different file types
folder_names = ['video_files', 'excel_files', 'csv_files', 'image_files', 'text_files', 'pdf_files', 'docx_files', 'powerbi_files', 'pptx_files']

# Create the folders for each file type if they don't already exist
for folder in folder_names:
    # Construct the full path for the folder
    folder_path = os.path.join(path, folder)
    # Check if the folder does not exist at the specified path
    if not os.path.exists(folder_path):
        # Create the folder since it doesn't exist
        os.makedirs(folder_path)

# Loop through each item (file or directory) in the list of file names
for file in file_names:
    # Construct the full path to the current item
    file_path = os.path.join(path, file)

    # Check if the current item is a file (not a directory)
    if os.path.isfile(file_path):
        # Check if the file is a CSV file and not already in the csv_files folder
        if file.endswith('.csv') and not os.path.exists(os.path.join(path, 'csv_files', file)):
            # Move the CSV file to the csv_files folder
            shutil.move(file_path, os.path.join(path, 'csv_files', file))

        # Check if the file is an image file (PNG, JPG, or JPEG) and not already in the image_files folder
        elif file.endswith(('.png', '.jpg', '.jpeg')) and not os.path.exists(os.path.join(path, 'image_files', file)):
            # Move the image file to the image_files folder
            shutil.move(file_path, os.path.join(path, 'image_files', file))

        # Check if the file is an Excel file (.xlsx) and not already in the excel_files folder
        elif file.endswith('.xlsx') and not os.path.exists(os.path.join(path, 'excel_files', file)):
            # Move the Excel file to the excel_files folder
            shutil.move(file_path, os.path.join(path, 'excel_files', file))

        # Check if the file is a PDF file and not already in the pdf_files folder
        elif file.endswith('.pdf') and not os.path.exists(os.path.join(path, 'pdf_files', file)):
            # Move the PDF file to the pdf_files folder
            shutil.move(file_path, os.path.join(path, 'pdf_files', file))

        # Check if the file is a text file (.txt) and not already in the text_files folder
        elif file.endswith('.txt') and not os.path.exists(os.path.join(path, 'text_files', file)):
            # Move the text file to the text_files folder
            shutil.move(file_path, os.path.join(path, 'text_files', file))
        
        # Check if the file is a docx file (.docx) and not already in the docx_files folder
        elif file.endswith('.docx') and not os.path.exists(os.path.join(path, 'docx_files', file)):
            # Move the text file to the text_files folder
            shutil.move(file_path, os.path.join(path, 'docx_files', file))
        
         # Check if the file is a pptx file (.pptx) and not already in the pptx_files folder
        elif file.endswith('.pptx') and not os.path.exists(os.path.join(path, 'pptx_files', file)):
            # Move the text file to the text_files folder
            shutil.move(file_path, os.path.join(path, 'pptx_files', file))
        
         # Check if the file is a pbix file (.pbix) and not already in the powerbi_files folder
        elif file.endswith('.pbix') and not os.path.exists(os.path.join(path, 'powerbi_files', file)):
            # Move the text file to the text_files folder
            shutil.move(file_path, os.path.join(path, 'powerbi_files', file))

        # Check if the file is a video file (GIF or MP4) and not already in the video_files folder
        elif file.endswith(('.gif', '.mp4')) and not os.path.exists(os.path.join(path, 'video_files', file)):
            # Move the video file to the video_files folder
            shutil.move(file_path, os.path.join(path, 'video_files', file))
