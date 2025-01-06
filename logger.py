import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger("SerialComm")
        handler = logging.FileHandler("communication.log")
        handler.setLevel(logging.INFO)
        self.logger.addHandler(handler)

    def log_message(self, direction, message):
        self.logger.info(f"{direction}: {message}")
