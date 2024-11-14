# IA Assistant - Voice Assistant Module

The IA Assistant project is designed for testing Text-to-Speech (TTS) and Language Translation (LLT) functionalities. 
The primary code is organized under the `voice_assistant` folder, with main scripts residing in `assistant`.

## Features

- **Text-to-Speech (TTS)**: Converts text inputs to spoken audio.
- **Language Translation (LLT)**: Processes language translation tasks.
- **Logging**: Stores logs for each session in the `logs/` folder.
- **Audio Samples**: Provides example audio files in `samples/` for testing.
- **Configurable Settings**: Adjustable configurations for customization in `config.py`.

## Directory Structure

The core functionality is implemented in the `voice_assistant` folder:

```plaintext
voice_assistant/
│
├── assistant/
│   ├── __init__.py                 # Initialization file for the assistant module
│   ├── f5tts_handler.py            # Handler for interacting with the F5 TTS service
│   ├── ollama_handler.py           # Interface for Ollama API interactions
│   └── voice_assistant.py          # Main assistant orchestration for TTS and LLT tasks
│
├── logs/                           # Stores log files for each session
├── samples/                        # Example audio files for testing
├── utils/                          # Utility scripts
├── config.py                       # Configuration file for customizing API keys and settings
└── main.py                         # Main entry point for running assistant functions
```

## Script Descriptions

Each script in the `assistant` folder serves a unique purpose:

- **`f5tts_handler.py`**  
  Provides an interface to the F5 TTS service. This script includes functions for sending text input and receiving audio output, enabling testing of the F5 TTS capabilities.

- **`ollama_handler.py`**  
  Interfaces with the Ollama API to facilitate translation and other language-based functions. It manages communication with the API, including sending requests and handling responses.

- **`voice_assistant.py`**  
  The main orchestration module for the voice assistant, integrating TTS and LLT functionalities. This script acts as the core assistant logic, managing both the F5 TTS and Ollama API handlers to provide a unified assistant interface.

## Setup

### Prerequisites

- **Python 3.10 or higher**
- Dependencies specified in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/rivascf/ia-assistant.git
   cd ia-assistant/voice_assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r ../requirements.txt
   ```

## Usage

1. **Run Main Script**:
   Use the main script to test TTS and LLT functionalities:
   ```bash
   python main.py
   ```

2. **Configurations**:
   Configure settings in `config.py` as required for API keys and log levels.

3. **Logs**:
   Logs are saved in `logs/`, capturing details of each interaction.

## Contributing

Contributions are welcome. Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](./LICENSE).
