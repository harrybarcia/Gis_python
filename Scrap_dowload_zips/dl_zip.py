import requests
from bs4 import BeautifulSoup
import os
import zipfile

def get_file_links(url):
    """
    Fetches all zip file links from a given URL.
    
    Args:
    url (str): URL to fetch zip file links from.
    
    Returns:
    list of str: List of file names.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    
    links = [link.get('href') for link in soup.find_all('a') if link.get('href') and link.get('href').endswith('.zip')]
    print("links", links)
    return links

def download_file(url_base, file_name, save_dir):
    """
    Download a file from a given URL and save it to a specified local path.
    
    Args:
    url_base (str): Base URL where files are located.
    file_name (str): Name of the file to be downloaded.
    save_dir (str): Directory to save the downloaded file.
    """
    full_url = f"{url_base}/{file_name}"
    save_path = os.path.join(save_dir, file_name)
    print(f"Starting the download process for {file_name}...")

    response = requests.get(full_url)
    if response.status_code == 200:
        print(f"Downloading {file_name}...")
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Download complete! {file_name} saved to: {save_path}")
        unzip_file(save_path, save_dir)
    else:
        print(f"Failed to download {file_name}. Status code: {response.status_code}")

def unzip_file(zip_path, extract_to):
    """
    Unzips a zip file into a specified subdirectory named 'unzippedfiles' within the given directory.

    Args:
    zip_path (str): Path to the zip file.
    extract_to (str): Base directory to which the files will be extracted.
    """
    # Define the path of the subfolder where the files will be extracted
    subfolder_path = os.path.join(extract_to, 'unzippedfiles')
    
    # Create the subfolder if it does not already exist
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)

    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(subfolder_path)
        print(f"Unzipped {os.path.basename(zip_path)} successfully to {subfolder_path}")
    except zipfile.BadZipFile:
        print(f"Failed to unzip {zip_path}. The file may be corrupted.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Base URL where the files are located
url_base = "https://www2.census.gov/geo/tiger/TIGER2023/BG"
save_directory = "./downloaded_files"

# Ensure the save directory exists
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Get the list of file names to download
file_names = get_file_links(url_base)[:2]

print("Script started.")
for file_name in file_names:
    download_file(url_base, file_name, save_directory)
print("Script finished.")
