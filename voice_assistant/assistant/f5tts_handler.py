"""
voice_assistant/assistant/f5tts_handler.py

Manages interaction with the F5TTS API for text-to-speech synthesis and plays
back generated audio.

License: MIT
Copyright (c) Advanced Robotics Research Group
Developer: Felipe Rivas
"""

import logging
import wave
import pyaudio
import asyncio
from gradio_client import Client, handle_file


class F5TTSHandler:
    """Handles text-to-speech synthesis with F5TTS and audio playback."""

    def __init__(self, api_url="http://127.0.0.1:7860/", audio_chunk=1024, debug=False):
        self.client = Client(api_url)
        self.audio_chunk = audio_chunk
        self.__debug_mode = debug

    async def synthesize_speech(self, ref_audio, ref_text, generated_text):
        """Generate audio using F5TTS API."""
        try:
            if self.__debug_mode:
                print(f"On DEBUG mode, F5TTS [to generate]: '{generated_text}'")
            result = await asyncio.to_thread(self.client.predict, ref_audio_input=handle_file(ref_audio), ref_text_input=ref_text, gen_text_input=generated_text, remove_silence=False, cross_fade_duration_slider=0.15, speed_slider=1.2, api_name="/basic_tts")
            return result
        except Exception as e:
            logging.error(f"Error synthesizing speech with F5TTS: {e}")
            return None

    async def play_audio(self, audio_file_path):
        """Play audio file using PyAudio."""
        try:
            with wave.open(audio_file_path, "rb") as audio_file:
                p = pyaudio.PyAudio()
                frames = audio_file.getnframes()
                rate = audio_file.getframerate()
                if self.__debug_mode:
                    print(f"On DEBUG mode: Playing audio file {(frames/float(rate)):.2f} secs.")
                stream = p.open(
                    format=p.get_format_from_width(audio_file.getsampwidth()),
                    channels=audio_file.getnchannels(),
                    rate=rate,
                    output=True
                )
                data = audio_file.readframes(self.audio_chunk)
                while data:
                    await asyncio.to_thread(stream.write, data)
                    data = audio_file.readframes(self.audio_chunk)
                stream.stop_stream()
                stream.close()
                p.terminate()
        except Exception as e:
            logging.error(f"Error playing audio: {e}")

