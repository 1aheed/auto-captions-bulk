# Auto-captions-bulk
The script is a Python tool designed to enhance videos by automatically adding subtitles and a watermark. It utilizes audio transcription through the OpenAI API (whisper) to generate subtitles, and then overlays them onto the video along with a customizable watermark. This automation simplifies the process of creating subtitled videos with branding.

# Requirements:
Python 3.x
<br>FFmpeg

# Run the script:
Clone this repository
<br>Navigate to the directory containing the script
<br>Place the videos you want to process in folder "input"
<br>Add your logo in png format in script folder (120x120px)
<br>Name the logo file "logo.png"
Obtain an OpenAI API key and replace the placeholder API key ("sk-key") in the script (run.py)
<br>Open a terminal or command prompt.
<br>pip install moviepy requests
<br>Run the script using the following command:
<br>python run.py

# Check the output:
The processed videos with subtitles and watermark will be saved in a folder named "output" within the same directory as the script.
By following these steps, you can easily use the script to enhance your videos with subtitles and watermark in an automated manner.
