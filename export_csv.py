import pandas as pd

def save_to_csv(video_data, output_file):
    df = pd.DataFrame(video_data)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
