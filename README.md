# AnalyticGetter

AnalyticGetter is a tool for fetching YouTube channel analytics, that includes video details (titles, view counts, etc.), thumbnails, and exporting the data to a CSV format. This CSV can be used for visualization in tools like Processing v4.3.

## Features
- Fetch video details (ID, title, upload date, views over time).
- Download video thumbnails locally.
- Export all data to a CSV file.
- Ready for visualization in Processing.

## Setup
1. Clone this repository:
git clone https://github.com/yourusername/AnalyticGetter.git
2. Install dependencies:
pip install -r requirements.txt
3. Set up your YouTube Data API key in `config.py`.

## Usage
Run the script:
python main.py

## Outputs
- CSV file: `data/video_data.csv`
- Thumbnails saved in the `data/thumbnails/` directory.

## Dependencies
- Python 3.8+
- `google-api-python-client`
- `pandas`
- `requests`

## Example Output
- CSV: Example of exported data.
- Thumbnails: Saved locally for each video.
