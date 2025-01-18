from fetch_data import fetch_video_data
from download_thumbnails import download_thumbnails
from export_csv import save_to_csv
import config

def main():
    # Fetch video data
    print("Fetching video data...")
    video_data = fetch_video_data(config.API_KEY, config.CHANNEL_ID)
    
    # Download thumbnails
    print("Downloading thumbnails...")
    video_data_with_thumbnails = download_thumbnails(video_data, config.THUMBNAILS_DIR)
    
    # Save data to CSV
    print("Saving data to CSV...")
    save_to_csv(video_data_with_thumbnails, config.CSV_FILE)

    print("All done! The data is ready for visualization.")

if __name__ == "__main__":
    main()
