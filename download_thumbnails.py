import os
import requests

def download_thumbnails(video_data, save_dir):
    os.makedirs(save_dir, exist_ok=True)

    for video in video_data:
        thumbnail_url = video["Thumbnail URL"]
        file_path = os.path.join(save_dir, f"{video['Video ID']}.jpg")
        
        response = requests.get(thumbnail_url)
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        video["Thumbnail Path"] = file_path

    return video_data
