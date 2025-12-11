"""
Logging configuration for the automation framework
"""
import logging
import os
from config.settings import LOG_LEVEL, LOG_FORMAT, REPORT_FOLDER


def setup_logger(name):
    """
    Setup logger for the given name
    
    Args:
        name: Logger name
        
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(REPORT_FOLDER, "logs")
    os.makedirs(logs_dir, exist_ok=True)
    
    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    console_formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(console_formatter)
    
    # File Handler
    log_file = os.path.join(logs_dir, "automation_tests.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(LOG_LEVEL)
    file_formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(file_formatter)
    
    # Add handlers to logger
    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger
