

import openai
import os
import base64

# Ensure your OPENAI_API_KEY environment variable is set
openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

frames_folder_path = 'frames/'

# Load and encode your frames in base64 format
base64_frames = []
for frame_file in sorted(os.listdir(frames_folder_path)):
    frame_path = os.path.join(frames_folder_path, frame_file)
    with open(frame_path, 'rb') as f:
        base64_frames.append(base64.b64encode(f.read()).decode('utf-8'))

# Create the prompt messages, including your base64 encoded frames
# Here, it's sending every 10th frame to reduce the number of API calls
PROMPT_MESSAGES = [
    {
        "role": "user",
        "content": [
            "These are frames from a video that I want to upload. Generate a compelling description that I can upload along with the video.",
            *map(lambda x: {"image": x, "resize": 768}, base64_frames[0::20]),
        ],
    },
]

# Set your parameters for the API call
params = {
    "model": "gpt-4-vision-preview",  # Model name can be different based on availability
    "messages": PROMPT_MESSAGES,
    "max_tokens": 200,
}

# Make the API call to get the description
result = openai.ChatCompletion.create(**params)
description = result.choices[0].message.content

# Save the description to a text file
with open('description.txt', 'w') as f:
    f.write(description)

print("The video description has been saved to description.txt.")

