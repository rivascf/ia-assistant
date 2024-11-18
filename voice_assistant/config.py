"""
voice_assistant/config.py

Configuration settings for the voice assistant application. This file defines
the constants for reference audio, wake word, timeout, and termination phrases.

License: MIT
Copyright (c) Advanced Robotics Research Group
Developer: Felipe Rivas
"""

REF_AUDIO_PATH = 'samples/viky_female.mp3'
REF_TEXT_INPUT = "The way you self-analyze, I've always admired it. But at some point, you have to forgive yourself. No one can undo the past."
WAKE_WORD = "assistant"
WAKE_UP_PHRASE = "hey assistant are you awake"
TIMEOUT = 60  # In seconds
TERMINATION_PHRASE = "bye-bye"
CHAT_MODE_TIMER = 60 # In seconds
