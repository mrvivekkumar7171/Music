# Visit https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z
# download and extract ffmpeg
# add path like C:\ffmpeg\bin to the system environment variable Path
# restart the terminal or IDE to apply the changes and verify by running ffmpeg -version
# run this script

import os
import subprocess

# Input and output folders
input_folder = 'assets\music'
output_folder = 'assets\compressed'

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# List all audio files in the folder
audio_files = [f for f in os.listdir(input_folder) if f.endswith(('.mp3', '.webm'))]

for file in audio_files:
    input_path = os.path.join(input_folder, file)
    
    # Set output filename and path
    name, ext = os.path.splitext(file)
    output_path = os.path.join(output_folder, f"{name}{ext}")

    # Choose settings based on format
    if ext == '.mp3':
        # Compress MP3 using variable bitrate (V2 ~ 192 kbps)
        cmd = [
            'ffmpeg', '-i', input_path,
            '-c:a', 'libmp3lame',
            '-qscale:a', '2',  # V2 quality
            output_path
        ]
    elif ext == '.webm':
        # Compress WebM using Opus at 96 kbps
        cmd = [
            'ffmpeg', '-i', input_path,
            '-c:a', 'libopus',
            '-b:a', '96k',
            output_path
        ]
    else:
        print(f"Skipping unsupported file: {file}")
        continue

    # Run the command
    print(f"Compressing {file}...")
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)

print("Compression completed.")