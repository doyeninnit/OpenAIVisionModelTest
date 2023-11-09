# # from IPython.display import display, Image, Audio

# import cv2  # We're using OpenCV to read video
# import base64
# import time
# import openai
# import os
# import requests

# descr = '/description'

# response = requests.post(
#     "https://api.openai.com/v1/audio/speech",
#     headers={
#         "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
#     },
#     json={
#         "model": "tts-1",
#         "input": descr,
#         "voice": "onyx",
#     },
# )

# audio = b""
# for chunk in response.iter_content(chunk_size=1024 * 1024):
#     audio += chunk
# openai.Audio(audio)


import requests
import os

# Set your description text
description_text = "Join me in my latest video where I dive deep into [topic/discussion point]. Whether you're looking for insights, laughs, or just a moment to pause and reflect, there’s something here for everyone. Don't forget to hit the like button if you enjoy the content and subscribe for more videos like this one. Share your thoughts in the comments below, and let's get the conversation started!"


# Make sure to set your OpenAI API key in your environment variables or load it securely
api_key = os.getenv('OPENAI_API_KEY')

response = requests.post(
    "https://api.openai.com/v1/audio/speech",
    headers={
        "Authorization": f"Bearer {api_key}",
    },
    json={
        "model": "tts-1",
        "input": description_text,
        "voice": "onyx",
    },
)

# Check if the request was successful
if response.status_code == 200:
    audio = response.content
    # Save the audio to a file
    with open('output.mp3', 'wb') as audio_file:
        audio_file.write(audio)
    print("The audio was saved to 'output.mp3'.")
else:
    print(f"Failed to generate audio. Status code: {response.status_code}")
    print(f"Response: {response.text}")
