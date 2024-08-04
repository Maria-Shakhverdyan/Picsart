def make_logger(level):
    log_levels = {
        "info": "INFO",
        "warning": "WARNING",
        "error": "ERROR",
        "debug": "DEBUG"
    }

    level_str = log_levels.get(level.lower(), "INFO")

    def logger(message):
        print(f"[{level_str}, {message}]")
    return logger

info_logger = make_logger("info")
info_logger("This is an information message")

info_logger = make_logger("warning")
info_logger("This is a warning message")

info_logger = make_logger("error")
info_logger("This is an error message")

info_logger = make_logger("degub")
info_logger("This is a debug message")