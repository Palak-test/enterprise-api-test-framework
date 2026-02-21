import logging
import os

class LoggingUtility:
    @staticmethod
    def setup_logging(log_file="app.log", level=logging.INFO):
        os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
        logging.basicConfig(
            filename=log_file,
            filemode='a',
            format='%(asctime)s %(levelname)s %(message)s',
            level=level
        )
        return logging.getLogger()

    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_error(message):
        logging.error(message)

    @staticmethod
    def log_debug(message):
        logging.debug(message)
