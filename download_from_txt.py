# download_and_categorize.py

import os
import yt_dlp
import time

# Paths
LINK_FILE     = "liked_videos_links.txt"
SUCCESS_FILE  = "downloaded_successfully.txt"
FAILURE_FILE  = "download_failure.txt"
DOWNLOAD_DIR  = r"C:\Users\Vivek\Desktop\youtube\music"

# Ensure download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Read all URLs from the success file before modifying it
if os.path.exists(SUCCESS_FILE):
    with open(SUCCESS_FILE, "r", encoding="utf-8-sig") as f:
        success_urls = [line.strip() for line in f if line.strip()]
else:
    success_urls = []

# Read all URLs from the master list
with open(LINK_FILE, "r", encoding="utf-8-sig") as f:
    urls = [line.strip() for line in f if line.strip()]

print('━' * 120)
print(f"🎯 Found {len(urls)} URLs to process\n")

def download_audio(url, out_dir):
    """Download the best audio track using yt-dlp and return the video title."""
    ydl_opts = {
        'outtmpl': os.path.join(out_dir, '%(title)s.%(ext)s'),
        'format': 'bestaudio/best',
        'quiet': True,
        'retries': 10,
        'fragment_retries': 10,
        'socket_timeout': 15,
        'geo_bypass': True,
        'nocheckcertificate': True,
        'noplaylist': True,
        'cookiefile': 'cookies.txt',
        'http_headers': {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/115.0.0.0 Safari/537.36'
            )
        }
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
    time.sleep(2)
    return info.get("title", url)


# Process each URL
for i,url in enumerate(urls):
    if not url in success_urls:
        print(i+1, end='\n')
        print(f"⬇️  Downloading: {url}")
        try:
            title = download_audio(url, DOWNLOAD_DIR)
            print(f"✅ Downloaded: {title}\n")
            # log success
            with open(SUCCESS_FILE, "a", encoding="utf-8") as sf:
                sf.write(url + "\n")
        except Exception as e:
            print(f"❌ Failed: {url} — {e}\n")
            # log failure
            with open(FAILURE_FILE, "a", encoding="utf-8") as ff:
                ff.write(url + "\n")
    else:
        print(f"✅ Already downloaded: {url}\n")

# Optionally, count how many succeeded/failed by counting lines
def count_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

success_count = count_lines(SUCCESS_FILE)
failure_count = count_lines(FAILURE_FILE)

print(f"🎉 Done! {success_count} succeeded, {failure_count} failed.")
print('━' * 120)