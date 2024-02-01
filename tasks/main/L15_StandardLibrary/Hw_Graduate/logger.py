import logging

LEVELS = {
    logging.NOTSET: "notset",
    logging.DEBUG: "debug",
    logging.INFO: "info",
    logging.WARNING: "warnings",
    logging.ERROR: "errors",
    logging.CRITICAL: "criticals"
}

FORMAT = "{asctime} | {levelname:<10} | {message}"


def init_logger(name: str, level_: int=logging.INFO, file_access: str = "a", encoding_: str="utf-8"):
    logging.basicConfig(filename=f"{name}_{LEVELS[level_]}.log",
                        filemode=file_access,
                        # encoding=encoding_,   # Actual if Python v3.9+
                        format=FORMAT,
                        style="{",
                        level=level_)
