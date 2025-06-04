# Install the Get cookies.txt browser extension and download cookies.txt and keep in same directory
# https://chromewebstore.google.com/detail/get-cookiestxt-locally/cclelndahbckbenkjhflpdbgdldlbecc
# NOTE: download the cookies.txt file just before running using yt-dlp to download the url in the json file.

# To install the yt-dlp package
# pip install yt-dlp

# To download the liked videos from YouTube using yt-dlp into a json file.
# yt-dlp --cookies cookies.txt --flat-playlist -J "https://www.youtube.com/playlist?list=LL" > liked_videos.json

# To extract only url of video from the json file and save it into a .txt file.
import json
# Load JSON file with UTF-16 encoding
with open("liked_videos.json", "r", encoding="utf-16") as f:
    data = json.load(f)

# Extract video URLs
video_urls = [entry["url"] for entry in data["entries"] if "url" in entry]

# Save to a .txt file
with open("liked_videos_links.txt", "w", encoding="utf-8") as out_file:
    for url in video_urls:
        out_file.write(url + "\n")

    # for i , url in enumerate(video_urls):
    #     url_with_index = str(i)+' : '+str(url)
    #     out_file.write(url_with_index + "\n")

print(f"✅ Saved {len(video_urls)} video links to liked_videos_links.txt")