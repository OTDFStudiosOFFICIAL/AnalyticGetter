# fetch_data.py

from googleapiclient.discovery import build
from config import API_KEY

def youtube_api_client(api_key):
    return build('youtube', 'v3', developerKey=api_key)

def fetch_video_data(api_key, channel_id):
    youtube = youtube_api_client(api_key)
    video_data = []

    # Fetch the uploads playlist ID from the channel
    channels_request = youtube.channels().list(
        part="contentDetails",
        id=channel_id
    )
    channels_response = channels_request.execute()

    # Get the playlistId of the "uploads" playlist
    uploads_playlist_id = channels_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

    # Fetch all videos from the uploads playlist
    next_page_token = None
    while True:
        request = youtube.playlistItems().list(
            part="snippet",
            playlistId=uploads_playlist_id,
            maxResults=50,  # Max results per request
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            video_title = item['snippet']['title']
            video_thumbnail_url = item['snippet']['thumbnails']['high']['url']

            # Get video statistics (views, likes, comments, etc.)
            stats_request = youtube.videos().list(
                part="statistics",
                id=video_id
            )
            stats_response = stats_request.execute()
            
            stats = stats_response['items'][0]['statistics']
            views = stats.get('viewCount', 0)
            likes = stats.get('likeCount', 0)
            comments = stats.get('commentCount', 0)
            
            video_data.append({
                'Video ID': video_id,
                'Title': video_title,
                'Thumbnail URL': video_thumbnail_url,
                'Views': views,
                'Likes': likes,
                'Comments': comments
            })

        # If there are more pages, continue fetching them
        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return video_data
