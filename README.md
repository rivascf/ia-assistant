# IA Assistant

## Overview

IA Assistant is a general-purpose AI assistant designed to perform testing for Language-to-Language Translation (LLT) and Text-to-Speech (TTS) capabilities. This repository includes scripts and resources for testing TTS and interaction with various AI models.

## Features

- **Language Translation (LLT)**: Provides a testing setup for language translation.
- **Text-to-Speech (TTS)**: Includes scripts for converting text to speech.
- **Audio Samples**: Contains example audio files used for TTS testing.
- **Logging**: Logs activities and interactions to a dedicated folder.

## Directory Structure

- **`audios/`**: Contains audio files used for TTS testing.
- **`logs/`**: Stores log files generated during test execution.
- **`f5tts_client_v1.py`**: Main client for testing TTS.
- **`ollama_client.py`**: Client for interaction with the Ollama API.
- **`pinokio_f5tts_api_test.py`**: Script for testing the F5 TTS API.
- **`pinokio_f5tts_ollama_test.py`**: Script for testing interactions between the F5 TTS and Ollama.
- **`requirements.txt`**: Lists required Python libraries and dependencies.

## Setup

### Prerequisites

- **Python 3.10 or higher**
- Required Python packages listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/rivascf/ia-assistant.git
    cd ia-assistant
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the `f5tts_client_v1.py` to test TTS capabilities:
    ```bash
    python f5tts_client_v1.py
    ```

2. To test interactions with the Ollama API:
    ```bash
    python ollama_client.py
    ```

3. For additional testing, use the `pinokio_f5tts_api_test.py` and `pinokio_f5tts_ollama_test.py` scripts.

### Logs

All interactions and results are logged in the `logs/` directory. Check this directory for detailed logs of each test run.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the [MIT License](LICENSE).


