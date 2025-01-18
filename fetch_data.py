from googleapiclient.discovery import build

def fetch_video_data(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    video_data = []
    next_page_token = None

    while True:
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=50,
            type="video",
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response['items']:
            video_data.append({
                "Video ID": item['id']['videoId'],
                "Title": item['snippet']['title'],
                "Thumbnail URL": item['snippet']['thumbnails']['high']['url']
            })

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return video_data
