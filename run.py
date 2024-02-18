import os
import requests
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, ImageClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

def extract_audio(video_path, audio_path):
    ffmpeg_extract_audio(video_path, audio_path)

def transcribe_audio(audio_path, output_format='verbose_json'):
    api_key = "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"
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    files = {
        'file': open(audio_path, 'rb')
    }
    data = {
        'timestamp_granularities[]': 'word',
        'model': 'whisper-1',
        'response_format': output_format
    }
    response = requests.post(url, headers=headers, files=files, data=data)
    response_data = response.json()
    return response_data

def add_subtitles_with_watermark(video_path, subtitles, output_path, watermark_path, top_padding=20, left_padding=20, text_padding=30):
    video = VideoFileClip(video_path)
    video = video.subclip(0, min(video.duration, subtitles[-1]['end_time']))

    # Create a list to hold TextClips
    text_clips = []

    # Define how many words you want to display per TextClip
    words_per_clip = 3

    # Group words into chunks
    for i in range(0, len(subtitles), words_per_clip):
        chunk = subtitles[i:i + words_per_clip]
        text = ' '.join(sub['text'] for sub in chunk).upper()  # Convert text to uppercase
        start_time = chunk[0]['start_time']
        end_time = chunk[-1]['end_time']

        # Create a TextClip for this chunk of words
        txt_clip = TextClip(text, fontsize=54, font='Arial-Bold', color='white', bg_color='black')
        # Adjust position to incorporate padding
        txt_clip = txt_clip.set_position(('center', 'center')).set_start(start_time).set_end(end_time)
        # Add padding to the text box
        txt_clip = txt_clip.margin(top=text_padding, bottom=text_padding, left=text_padding, right=text_padding, color=(0, 0, 0))
        text_clips.append(txt_clip)

    # Overlay the TextClips onto the video
    video_with_subtitles = CompositeVideoClip([video] + text_clips)

    # Load the watermark image
    watermark = ImageClip(watermark_path)
    watermark = watermark.set_duration(video.duration)
    watermark = watermark.set_opacity(1.0)  # Adjust opacity as needed

    # Calculate position for the watermark
    watermark_position = (left_padding, top_padding)

    # Add the watermark to the video
    video_with_watermark = CompositeVideoClip([video_with_subtitles.set_position('center'), watermark.set_position(watermark_position)])

    # Write the final video file
    video_with_watermark.write_videofile(output_path, codec="libx264", audio_codec="aac")



def process_video_folder(video_folder, output_folder):
    for filename in os.listdir(video_folder):
        if filename.endswith(".mp4"):
            video_path = os.path.join(video_folder, filename)
            audio_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.mp3")
            output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.mp4")
            
            watermark_path = "logo.png"
            top_padding = 40
            left_padding = 40

            # Extract audio from video
            extract_audio(video_path, audio_path)

            # Transcribe audio
            transcriptions = transcribe_audio(audio_path)

            # Extract transcriptions with timestamps
            subtitles = []
            for word in transcriptions['words']:
                subtitles.append({
                    'text': word['word'],
                    'start_time': word['start'],
                    'end_time': word['end']
                })

            # Add subtitles and watermark to video
            add_subtitles_with_watermark(video_path, subtitles, output_path, watermark_path, top_padding, left_padding)

            # Clean up temporary audio file
            os.remove(audio_path)

if __name__ == "__main__":
    video_folder = "input"
    output_folder = "output"
    process_video_folder(video_folder, output_folder)
