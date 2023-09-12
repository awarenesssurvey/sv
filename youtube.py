from youtube_transcript_api import YouTubeTranscriptApi

# YouTube video URL or video ID
# video_url = "https://www.youtube.com/watch?v=7RWgy8YoXJ4"
video_url =  "https://www.youtube.com/watch?v=WbzJgPJ8bos"

# Function to get the transcript
def get_transcript(video_url):
    # Extract the video ID from the URL
    video_id = video_url.split("v=")[1]

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)

        # Save the transcript to a text file
        with open("Transcript/transcript.txt", "w", encoding="utf-8") as file:
            for entry in transcript:
                text = entry['text']
                file.write(text + "\n")

        print("Transcript downloaded and saved as 'transcript.txt'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Call the function to get the transcript
get_transcript(video_url)
