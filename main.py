# main.py

from fetch_data import fetch_video_data
from download_thumbnails import download_thumbnails
from export_csv import save_to_csv
from config import API_KEY, CHANNEL_ID

def main():
    # Fetch data from YouTube API
    video_data = fetch_video_data(API_KEY, CHANNEL_ID)
    
    # Save video data to CSV
    save_to_csv(video_data)
    
    # Download video thumbnails
    download_thumbnails(video_data)
    
    print("Data has been fetched, thumbnails downloaded, and CSV saved.")

if __name__ == "__main__":
    main()
