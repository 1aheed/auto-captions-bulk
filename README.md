# auto-captions-bulk
The script is a Python tool designed to enhance videos by automatically adding subtitles and a watermark. It utilizes audio transcription through the OpenAI API to generate subtitles, and then overlays them onto the video along with a customizable watermark. This automation simplifies the process of creating subtitled videos with branding.

# Requirements:
Python 3.x

# How to Run:
Install Python dependencies:
1. pip install moviepy requests
Ensure FFmpeg is installed: Make sure FFmpeg is installed and available in your system's PATH.

Obtain an OpenAI API key: Get an API key from OpenAI and replace the placeholder API key ("sk-key") in the script with your actual key.

# Prepare your input videos:
Place the video files you want to process in a folder named "input" within the same directory as the script.

# Run the script:
Navigate to the directory containing the script.
Open a terminal or command prompt.
Run the script using the following command:
python run.py

# Check the output:
The processed videos with subtitles and watermark will be saved in a folder named "output" within the same directory as the script.
By following these steps, you can easily use the script to enhance your videos with subtitles and watermark in an automated manner.
