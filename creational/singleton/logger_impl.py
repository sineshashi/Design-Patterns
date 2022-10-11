class Logger:
    class _Logger:
        def __init__(self, filepath):
            self.filepath = filepath

        def _write_log(self, message, type):
            with open(self.filepath, "a") as fp:
                fp.write(f"[{type}!] {message}\n")

        def error(self, message):
            self._write_log(message, "ERROR")

        def critical(self, message):
            self._write_log(message, "CRITICAL")

        def warning(self, message):
            self._write_log(message, "WARNING")

    instance = None

    def __new__(cls, filepath):
        if not Logger.instance:
            Logger.instance = Logger._Logger(filepath)
        return Logger.instance

    def __getattribute__(self, __name: str):
        return getattr(Logger.instance, __name)

    def __setattr__(self, __name: str, __value) -> None:
        return setattr(Logger.instance, __name, __value)

logger = Logger("./singleton/log.log") #This instance can be imported anywhere and can be used to log.
#This manages whole logging in this file throughout the system at global level.


if __name__ == "__main__":
    logger.critical("This is critical.")
    logger.error("This is error")
    logger.warning("This is warning")