# Text-to-Speech Web App

## Overview
This project is a text-to-speech web application built using the Microsoft Edge TTS model. The user interface is created with the Gradio framework. Users can input text, set the pitch and speech rate, choose from various voices in the voice library, and download the generated audio file.
You can use this web app [here](https://huggingface.co/spaces/peaceout13/Text_to_speech)

## Features
- **Text-to-Speech Conversion:** Converts user-input text into speech.
- **Adjustable Pitch and Speech Rate:** Allows users to customize the pitch and speech rate of the generated audio.
- **Voice Library:** Users can choose from different voices available in the library.
- **Audio Download:** Users can download the generated audio file.

## Technologies Used
- **Python:** Programming language used for the backend.
- **Microsoft Edge TTS Model:** Model used for text-to-speech conversion.
- **Gradio:** Framework used for creating the user interface.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/abhisek-13/text-to-speech.git
    cd text-to-speech

    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # On Windows
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Gradio application:
    ```bash
    python src\app.py
    ```
2. Open your web browser and go to the URL provided by Gradio to access the web app.
3. Input your text, set the pitch and speech rate, choose a voice, and click the generate button to create the audio file.
4. Click the download button to save the generated audio file to your device.

## Project Structure
- `app.py`: Main application file for running the Gradio web app.
- `requirements.txt`: List of required Python packages.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any questions or feedback, please contact [abhisekmaharana9861@gmail.com](abhisekmaharana9861@gmail.com).
