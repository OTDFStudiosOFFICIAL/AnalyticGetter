from googleapiclient.discovery import build
from config import API_KEY

def youtube_api_client(api_key):
    return build('youtube', 'v3', developerKey=api_key)

def fetch_video_data(api_key, channel_id, start_date, end_date):
    youtube = youtube_api_client(api_key)
    video_data = []
    
    # YouTube API request for channel's videos
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        publishedAfter=start_date,
        publishedBefore=end_date,
        maxResults=50  # Adjust based on your needs (max 50 per request)
    )
    response = request.execute()
    
    for item in response['items']:
        video_id = item['id']['videoId']
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

    return video_data
