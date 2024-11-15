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
        self.__debug_mode = debug
        self.client = ollama.Client()
        self.model = model
        self.detailed_ans = False
        self.temperature = temperature

    async def generate_chat_response(self, conversation_context, detailed=False):
        flag_change = self.detailed_ans != detailed
        try:
            prompt_type = "detailed" if detailed else "concise"
            if self.__debug_mode:
                print(f"On DEBUG mode, Ollama chatting, prompt type '{prompt_type}'.")
            if flag_change:
                self.detailed_ans = flag_change
                conversation_context.insert(len(conversation_context) - 1, {"role": "system", "content": f"Please provide a {prompt_type} response."})
                # conversation_context.append({"role": "system", "content": f"Please provide a {prompt_type} response."})
            if self.__debug_mode:
                print(f"On DEBUG mode, Ollama chatting, current conversation messages '{conversation_context}'.")
                print(f"On DEBUG mode, Ollama chatting, generating a '{prompt_type}' response. Means temperature={0.8 if detailed else 0.2}")
            response = await asyncio.to_thread(
                self.client.chat,
                model=self.model,
                messages=conversation_context,
                options={
                    "temperature": 0.8 if detailed else 0.1
                },
                stream=False
            )
            if self.__debug_mode:
                print(f"On DEBUG mode, Ollama [{self.model}]: '{response}'")
                print(f"On DEBUG mode, Ollama [{self.model}]: returning '{response.get("message")}'")
                print(f"On DEBUG mode: Ollama stats ['{response.get("created_at")}', '{response.get("total_duration")}']")
            return response.get("message")
        except Exception as e:
            logging.error(f"Error generating response from Ollama: {e}")
            return None

    async def generate_response_with_context(self, conversation_context, detailed=False):
        """
        Async method to generate a conversational response from Ollama API using context.
        Supports short answers by default; if detailed=True, generates a longer response.

        Args:
            conversation_context (list): A list of dictionaries with roles and messages to maintain conversation.
            detailed (bool): If True, requests a detailed response; otherwise, requests a short response.

        Returns:
            str: Assistant's response based on conversation context.
        """
        try:
            prompt_type = "detailed" if detailed else "concise"
            if self.__debug_mode:
                print(f"On DEBUG mode, Ollama executing a '{prompt_type}' inference to model.")
            conversation_context.append({"role": "system", "content": f"Please provide a {prompt_type} response."})
            response = await asyncio.to_thread(
                self.client.generate,
                model=self.model,
                prompt=conversation_context[0],
                context=conversation_context[1],
                raw=True
            )
            if self.__debug_mode:
                print(f"On DEBUG mode, Ollama [{self.model}]: '{response}'")
                print(f"On DEBUG mode: Ollama stats ['{response.get("created_at")}', '{response.get("total_duration")}']")
            return response.get("response")
        except Exception as e:
            logging.error(f"Error generating response from Ollama: {e}")
            return None

