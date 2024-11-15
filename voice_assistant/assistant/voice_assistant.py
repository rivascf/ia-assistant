"""
voice_assistant/assistant/voice_assistant.py

Defines the main VoiceAssistant class, which manages interaction between
speech recognition, the Ollama API, and the F5TTS API. The assistant listens
for specific trigger phrases and responds with synthesized speech.

License: MIT
Copyright (c) Advanced Robotics Research Group
Developer: Felipe Rivas
"""

import asyncio
import time
import sys
import logging
import speech_recognition as sr
from .ollama_handler import OllamaHandler
from .f5tts_handler import F5TTSHandler
from voice_assistant.utils.logger import configure_logging
from voice_assistant.config import WAKE_WORD, WAKE_UP_PHRASE, TERMINATION_PHRASE, TIMEOUT

configure_logging()

class VoiceAssistant:
    """Main assistant class that listens for user input and provides responses."""

    def __init__(self, ref_audio_path, ref_text_input, wake_word=WAKE_WORD, wake_up_phrase=WAKE_UP_PHRASE, timeout=TIMEOUT, termination_phrase=TERMINATION_PHRASE, debug=False):
        self.recognizer = sr.Recognizer()
        self.ollama_handler = OllamaHandler(debug=debug)
        self.f5tts_handler = F5TTSHandler(debug=debug)
        self.ref_audio_path = ref_audio_path
        self.ref_text_input = ref_text_input
        self.wake_word = wake_word.lower()
        self.wake_up_phrase = wake_up_phrase.lower()
        self.timeout = timeout
        self.termination_phrase = termination_phrase.lower()
        self.sleeping = False  # Indicates if assistant is in sleep mode
        self.__debug_mode = debug

    async def listen_for_trigger(self):
        """Listen for wake word, wake-up phrase, or termination phrase to initiate interaction."""
        start_time = time.time()
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while True:
                if not self.sleeping and time.time() - start_time > self.timeout:
                    await self.respond("Entering sleep mode due to inactivity.")
                    self.sleeping = True

                try:
                    audio = self.recognizer.listen(source)
                    transcript = self.recognizer.recognize_google(audio).lower()
                    if self.__debug_mode:
                        print(f"On DEBUG: {transcript}")
                        logging.debug(f"On DEBUG: {transcript}")
                    if self.wake_word in transcript and not self.sleeping:
                        await self.respond("How can I assist you?")
                        return "wake_word"
                    elif self.wake_up_phrase in transcript and self.sleeping:
                        self.sleeping = False
                        await self.respond("I'm awake now. How can I assist you?")
                        return "wake_up_phrase"
                    elif self.termination_phrase in transcript:
                        await self.respond("Goodbye, have a nice day... Shutting down now.")
                        sys.exit(0)
                except sr.UnknownValueError:
                    pass
                except sr.RequestError as e:
                    logging.error(f"Speech recognition service error: {e}")

    async def listen_to_user(self):
        """Capture user's query after activation and convert it to text."""
        if self.__debug_mode:
            print("On DEBUG mode: listening user...")
        with sr.Microphone() as source:
            audio_data = self.recognizer.listen(source)
            try:
                return self.recognizer.recognize_google(audio_data)
            except sr.UnknownValueError:
                await self.respond("Sorry, I did not understand that.")
                return None

    async def respond(self, text):
        """Provide synthesized response to the user."""
        req_start = time.time()
        result = await self.f5tts_handler.synthesize_speech(self.ref_audio_path, self.ref_text_input, text)
        req_stop = time.time()
        if result:
            if self.__debug_mode:
                print(f"On DEBUG mode: Speech Generation elapsed time = '{(req_stop-req_start):.2f} seg.'")
            await self.f5tts_handler.play_audio(result[0])

    async def handle_user_interaction(self):
        """Generate and speak response based on user's query."""
        prompt = await self.listen_to_user()
        if prompt:
            if self.__debug_mode:
                print(f"On DEBUG mode: User's prompt '{"In 100 words or less. " + prompt}'")
            response = await self.ollama_handler.generate_response("In 100 words or less. " + prompt)
            if response:
                await self.respond(response)
            else:
                if self.__debug_mode:
                    print("On DEBUG mode: No response generated for user's prompt.")
                await self.respond("Sorry, I could not generate a response.")

    async def run(self):
        """Runs the assistant in a continuous loop, waiting for triggers and handling interactions."""
        if self.__debug_mode:
            print("On DEBUG mode: VoiceAssistant running...")
            await self.respond("Hello, Voice assistant running on debug mode.")
        else:
            await self.respond("Hello, Voice assistant running.")
        while True:
            trigger = await self.listen_for_trigger()
            if trigger == "wake_word":
                await self.handle_user_interaction()
            elif trigger == "wake_up_phrase":
                logging.info("Resuming from sleep mode. Listening for user input.")

