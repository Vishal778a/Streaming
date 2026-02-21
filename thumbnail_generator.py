import os
import re
import requests
import sys

def download_thumbnail(video_url):
    match = re.search(r"v=([a-zA-Z0-9_-]{11})", video_url)
    if not match:
        print("❌ Could not extract video ID. Please check the URL.")
        return
    video_id = match.group(1)

    thumbnail_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"

    folder = os.path.join(os.getcwd(), "thumbnails")
    os.makedirs(folder, exist_ok=True)

    save_path = os.path.join(folder, f"{video_id}.jpg")

    response = requests.get(thumbnail_url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Thumbnail saved at:\n{os.path.abspath(save_path)}")
    else:
        print("⚠️ Max resolution not available. Try hqdefault.jpg instead.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python thumbnail_generator.py <YouTube URL>")
    else:
        download_thumbnail(sys.argv[1])
