import logging

class Logger:
    config = None;

    def __init__(self, config):
        self.config = config

    def get_logger(self, logger_name):
        logger_path = self.config["logger_path"]
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s [%(levelname)s] %(module)s:%(lineno)d - %(message)s",
                            datefmt="%Y-%m-%d %H:%M:%S",
                            handlers=[logging.FileHandler(logger_path + "/" + logger_name),logging.StreamHandler()])
        return logging.getLogger(logger_name)