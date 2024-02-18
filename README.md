# auto-captions-bulk
The script is a Python tool designed to enhance videos by automatically adding subtitles and a watermark. It utilizes audio transcription through the OpenAI API to generate subtitles, and then overlays them onto the video along with a customizable watermark. This automation simplifies the process of creating subtitled videos with branding.

Requirements:
Python 3.x installed on your system.
Installation of the following Python packages:
moviepy: For video editing functionalities.
requests: For making HTTP requests to the OpenAI API.
FFmpeg: Required for audio extraction (ensure it's installed and accessible in your system's PATH).
An OpenAI API key to transcribe audio (replace the placeholder API key in the script with your actual key).
A watermark image named "logo.png" placed in the same directory as the script.
How to Run:
Install Python dependencies:

Copy code
pip install moviepy requests
Ensure FFmpeg is installed: Make sure FFmpeg is installed and available in your system's PATH.

Obtain an OpenAI API key: Get an API key from OpenAI and replace the placeholder API key ("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") in the script with your actual key.

Prepare your input videos:

Place the video files you want to process in a folder named "input" within the same directory as the script.
Run the script:

Open a terminal or command prompt.
Navigate to the directory containing the script.
Run the script using the following command:
Copy code
python script_name.py
Replace script_name.py with the actual name of the script file.
Check the output:

The processed videos with subtitles and watermark will be saved in a folder named "output" within the same directory as the script.
By following these steps, you can easily use the script to enhance your videos with subtitles and watermark in an automated manner.
