# export_csv.py

import csv
import os

def save_to_csv(video_data):
    # Ensure the 'data' directory exists
    if not os.path.exists('data'):
        os.makedirs('data')

    filename = 'data/video_data.csv'
    
    # Writing video data to CSV
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=video_data[0].keys())
        writer.writeheader()
        writer.writerows(video_data)
    
    print(f"Data saved to {filename}")
