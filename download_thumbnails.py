# download_thumbnails.py

import os
import requests

def download_thumbnails(video_data, save_dir="data/thumbnails"):
    # Create thumbnails folder if it doesn't exist
    os.makedirs(save_dir, exist_ok=True)
    
    for video in video_data:
        thumbnail_url = video["Thumbnail URL"]
        file_name = f"{video['Video ID']}.jpg"
        file_path = os.path.join(save_dir, file_name)

        # Download and save the thumbnail image
        response = requests.get(thumbnail_url)
        with open(file_path, "wb") as file:
            file.write(response.content)

        # Optionally add the local file path back to video data
        video["Thumbnail Path"] = file_path

    return video_data
