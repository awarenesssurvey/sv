from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import os
from datetime import datetime

user = 'developer1'

video_url = input('Enter video URL: ')

# Function to sanitize a string to be used as a filename
def sanitize_filename(filename):
    # Replace characters that are not allowed in filenames with underscores
    invalid_chars = '<>:"/\\|?*'
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    return filename

def get_transcript(video_url):
    try:
        # Get the video ID from the URL
        video_id = video_url.split("v=")[1]

        # Fetch the video title using pytube
        yt = YouTube(video_url)
        video_title = yt.title
        #

        sanitized_title = sanitize_filename(video_title)

        # Get the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Generate a timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        folder_path = f"/Users/{user}/Google Drive/My Drive/Transcript"

        # Check if the folder exists, and create it if it doesn't
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"Folder '{folder_path}' created successfully.")

        google_drive_path = f"/Users/{user}/Google Drive/My Drive/Transcript"

        # Save the transcript to a text file with sanitized video title and timestamp as the file name
        with open(f"{google_drive_path}/{sanitized_title}_{timestamp}_transcript.docx", "w", encoding="utf-8") as file:
            for entry in transcript:
                text = entry['text']
                file.write(text + "\n")

        print(f"Transcript downloaded and saved as '{sanitized_title}_{timestamp}_transcript.docx'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function to get the transcript
