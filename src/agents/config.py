import os
import logging

def get_logger(agent_name: str):
    log_dir = os.path.expanduser("~/enitorpay-backend/src/logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "agents.log")

    logger = logging.getLogger(agent_name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # File handler
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] [%(name)s] %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

