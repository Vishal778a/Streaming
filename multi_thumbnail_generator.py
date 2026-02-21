import os
import re
import requests
import datetime
import sys

def download_thumbnail(video_url, folder):
    # Extract video ID from URL
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", video_url)
    if not match:
        print(f"❌ Could not extract video ID from: {video_url}")
        return
    video_id = match.group(1)

    # Construct thumbnail URL
    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    # Save path inside batch subfolder
    save_path = os.path.join(folder, f"{video_id}.jpg")

    # Download the thumbnail
    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Saved thumbnail at: {os.path.abspath(save_path)}")
    else:
        print(f"⚠️ Max resolution not available for {video_id}. Try hqdefault.jpg instead.")

def batch_download(file_path, custom_name=None):
    # Create 'thumbnails' base folder if it doesn't exist
    base_folder = os.path.join(os.getcwd(), "thumbnails")
    os.makedirs(base_folder, exist_ok=True)

    # Decide subfolder name
    if custom_name:
        batch_folder = os.path.join(base_folder, custom_name)
    else:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        batch_folder = os.path.join(base_folder, f"batch_{timestamp}")

    os.makedirs(batch_folder, exist_ok=True)

    # Read URLs from text file
    with open(file_path, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    # Process each URL
    for url in urls:
        download_thumbnail(url, batch_folder)

    print(f"\n📂 All thumbnails saved in: {os.path.abspath(batch_folder)}")

if __name__ == "__main__":
    # Usage:
    # python thumbnail_generator.py urls.txt MyCustomFolder
    # or just: python thumbnail_generator.py urls.txt
    if len(sys.argv) < 2:
        print("Usage: python thumbnail_generator.py <urls.txt> [custom_folder_name]")
    else:
        txt_file = sys.argv[1]
        custom_name = sys.argv[2] if len(sys.argv) > 2 else None
        batch_download(txt_file, custom_name)
