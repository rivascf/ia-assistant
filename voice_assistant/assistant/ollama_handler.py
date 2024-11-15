"""
voice_assistant/assistant/ollama_handler.py

Handles interaction with the Ollama API, generating text responses
based on user prompts.

License: MIT
Copyright (c) Advanced Robotics Research Group
Developer: Felipe Rivas
"""

import logging
import ollama
import asyncio

class OllamaHandler:
    """Manages calls to the Ollama API for generating AI-based responses."""

    def __init__(self, model="llama3.2", temperature=0.8, debug=False):
        # temperature=0.8, num_predict=100
        self.__debug_mode = debug
        self.client = ollama.Client()
        self.model = model
        self.options = {
            "temperature": temperature
            #"num_predict": num_predict
        }

    async def generate_response(self, prompt):
        """Generate response from Ollama API based on a prompt."""
        try:
            response = await asyncio.to_thread(self.client.generate, model=self.model, prompt=prompt, raw=True)
            if self.__debug_mode:
                print(f"On DEBUG mode, Ollama [{self.model}]: '{response}'")
                print(f"On DEBUG mode: Ollama stats ['{response.get("created_at")}', '{response.get("total_duration")}']")
            return response.get("response")
        except Exception as e:
            logging.error(f"Error generating response from Ollama: {e}")
            return None

