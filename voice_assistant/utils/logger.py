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
    # format type 01: [INFO] [1731956279.407480733] [service_server]: Server initialized...
    # format type 02:
    # [DEBUG] [launch]: processing event: '<launch.events.process.process_started.ProcessStarted object at 0x7bee6cf47430>'
    logging.basicConfig(
        filename=f'./logs/voice_assistant_{datetime.datetime.now():%d%m%y}.log',
        level=logging.INFO,
        #format='%(asctime)s - %(levelname)s - %(message)s'
        format='[%(levelname)s] [%(asctime)s]: %(message)s'
    )
