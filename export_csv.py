import csv

def save_to_csv(video_data, filename='data/video_data.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=video_data[0].keys())
        writer.writeheader()
        writer.writerows(video_data)
