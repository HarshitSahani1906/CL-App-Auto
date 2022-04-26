import logging
import time
from Logs.LogPath import log


class Logging:
    def __init__(self, logger, file_level=logging.INFO):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        logpath = log()
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        curr_time = time.strftime("%Y-%m-%d")
        self.LogFileName = logpath.log_path() + '/log' + curr_time + '.txt'
        print(self.LogFileName)
        # self.LogFileName = '..\\Logs\\log' + curr_time + '.txt'
        # "a" to append the logs in same file, "w" to generate new logs and delete old one
        fh = logging.FileHandler(self.LogFileName, mode="a")
        fh.setFormatter(fmt)
        fh.setLevel(file_level)
        self.logger.addHandler(fh)
