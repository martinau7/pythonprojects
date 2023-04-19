# for audio
# python mp4downloader.py -a -v "YouTube video URL"

# for videos
# python mp4downloader.py -v "YouTube video URL"

import argparse
from pytube import YouTube

# Directories for storing downloaded videos and audio.

VIDEO_DOWNLOAD_DIR = "Downloads/videos"
AUDIO_DOWNLOAD_DIR = "Downloads/audio"


# Download audio only.
def YoutubeAudioDownload(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio=True).first()

    try:
        audio.download(AUDIO_DOWNLOAD_DIR)
    except:
        print("Failed to download audio. ")

    print("Audio was downloaded successfully. ")


# Download video only.
def YoutubeVideoDownload(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(VIDEO_DOWNLOAD_DIR)
    except:
        print("Unable to download video at this time! ")

    print("Video downloaded! ")


# Checking if the file downloaded should be audio or video.

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required=True, help="Youtube video URL")
    ap.add_argument("-a", "--audio", required=False, help="Audio only", action=argparse.BooleanOptionalAction)
    args = vars(ap.parse_args())

    if args["audio"]:
        YoutubeAudioDownload(args["video"])
    else:
        YoutubeVideoDownload(args["video"])
