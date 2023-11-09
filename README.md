# Video Narration with OpenAI GPT and TTS API

This project demonstrates how to create a video narration using OpenAI's GPT model for generating a script and the Text-to-Speech (TTS) API to produce a voiceover. The final output is a video with a voiceover.
## Project Structure

- `video_narration/`
  - `frames/`: Directory where extracted frames from the video are stored as JPEG files.
  - `audio/`: Directory where the generated audio files are stored.
  - `describe_frames.py`: Script to extract descriptions from video frames using OpenAI's GPT.
  - `generate_voiceover.py`: Script to generate a voiceover from the frame descriptions.
  - `final_video_with_voiceover.mp4`: The final video file with the voiceover.

## Setup

1. Clone the repository to your local machine.

    ```bash
    git clone https://github.com/doyeninnit/OpenAIVisionModelTest.git
    cd video_narration
    ```

2. Install the required Python packages.

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the `OPENAI_API_KEY` in your environment variables.

    ```bash
    export OPENAI_API_KEY='your-api-key'
    ```

## Usage

1. Place the video file you want to narrate in the `video_narration/` directory.

2. Run the `describe_frames.py` script to extract frames and get their descriptions.

    ```bash
    python describe_frames.py
    ```

3. Run the `generate_voiceover.py` script to generate the voiceover and overlay it onto the original video.

    ```bash
    python generate_voiceover.py
    ```

4. The final video with the voiceover will be saved as `output.mp4` in the project directory.

## Configuration

- To change the style of narration or the voice used in the TTS, modify the `generate_voiceover.py` script.
- For adjusting the rate limits and request size, refer to the OpenAI API documentation.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your proposed changes.

## License

This project is open-sourced under the MIT License. See the LICENSE file for more information.

## Acknowledgements

- OpenAI for providing the GPT and TTS API.
- David Attenborough for inspiration.

## Contact

<!-- For support or queries, reach out to `contact@example.com`. -->
