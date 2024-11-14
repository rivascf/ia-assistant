"""
voice_assistant/utils/logger.py

Configures logging settings for the voice assistant application.

License: MIT
Copyright (c) Advanced Robotics Research Group
Developer: Felipe Rivas
"""

import logging
import datetime

def configure_logging():
    """Sets up logging configuration for the application."""
    logging.basicConfig(
        filename=f'./logs/voice_assistant_{datetime.datetime.now():%d%m%y}.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
