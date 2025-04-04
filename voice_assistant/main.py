"""
voice_assistant/main.py

Main entry point for running the voice assistant application. This script
initializes and runs the assistant in continuous mode, enabling it to respond
to user input through speech.

License: MIT
Copyright (c) Advanced Robotics Research Group
Developer: Felipe Rivas
"""

from assistant.voice_assistant import VoiceAssistant
from config import REF_AUDIO_PATH, REF_TEXT_INPUT, WAKE_WORD, WAKE_UP_PHRASE, TIMEOUT, TERMINATION_PHRASE

if __name__ == "__main__":
    # Initialize and run the voice assistant in continuous mode
    assistant = VoiceAssistant(
        ref_audio_path=REF_AUDIO_PATH,
        ref_text_input=REF_TEXT_INPUT,
        wake_word=WAKE_WORD,
        wake_up_phrase=WAKE_UP_PHRASE,
        timeout=TIMEOUT,
        termination_phrase=TERMINATION_PHRASE,
        debug=True
    )
    assistant.run()
