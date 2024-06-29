from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import re


app = Flask(__name__)


def extract_youtube_video_id(url: str):
    match = re.search(
        r'(?:https?:\/\/)?(?:www\.)?youtu(?:be)?\.(?:com|be)\/(?:watch\?v=|embed\/|v\/|live\/|shorts\/|)([^#&?]+)', url)
    return match.group(1) if match else None


@app.route("/")
def hello_world():
    return render_template('index.html', text=123)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route('/submit', methods=['POST'])
def get_captions():
    if request.method == 'POST':
        data = request.form.to_dict()
        video_id = extract_youtube_video_id(data['url'])
        if video_id:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            final_transcript = ''
            space = ' '
            if transcript:
                for trans in transcript:
                    final_transcript += space + trans['text']
            else:
                final_transcript = 'Sorry, but the transcript is not available.'
        else:
            final_transcript = 'Sorry, but the transcript is not available.'
    else:
        return 'Oops! Something went wrong, try again later!'
    return render_template('transcript.html', transcript=final_transcript)
