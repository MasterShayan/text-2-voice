import os
from logging import INFO, FileHandler, Formatter, Logger, StreamHandler
from logging.handlers import RotatingFileHandler
from typing import Optional


class CustomLogger(Logger):
    """Custom logger with console and file output, and formatted messages."""
    def __init__(self,
                 name: str,
                 level: int = INFO,
                 log_to_file: bool = False,
                 log_file_path: Optional[str] = None,
                 max_log_size: int = 10 * 1024 * 1024,  # Default: 10MB
                 backup_count: int = 5):  # Default: 5 backups
        """
        Initializes a custom logger with configurable handlers.

        :param name: Name of the logger.
        :param level: Logging level (e.g., INFO, DEBUG, ERROR).
        :param log_to_file: Whether to log to a file (default: False).
        :param log_file_path: Path to the log file (if logging to a file).
        :param max_log_size: Maximum size of the log file before rotation (default: 10MB).
        :param backup_count: Number of backup log files to keep (default: 5).
        """
  
        super().__init__(name, level)

        # Formatter for log messages
        formatter = Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        # Console handler for standard output
        console_handler = StreamHandler()
        console_handler.setFormatter(formatter)

        # Add console handler if not already present
        if not self.hasHandlers():
            self.addHandler(console_handler)

        # File handler setup (if enabled)
        if log_to_file and log_file_path:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(log_file_path), exist_ok = True)

            # Use RotatingFileHandler to limit file size and rotate logs
            file_handler = RotatingFileHandler(log_file_path,
                                               maxBytes = max_log_size,
                                               backupCount = backup_count)
            file_handler.setFormatter(formatter)

            self.addHandler(file_handler)

        # Set the default logging level (INFO, DEBUG, etc.)
        self.setLevel(level)

        # Avoid duplicate handlers (handled by `hasHandlers()` check above)

    def log_to_console(self, level: int = INFO) -> None:
        """Logs a message to the console."""
        self.setLevel(level)
        for handler in self.handlers:
            if isinstance(handler, StreamHandler):
                handler.setLevel(level)

    def log_to_file(self, level: int = INFO) -> None:
        """Logs a message to the file."""
        self.setLevel(level)
        for handler in self.handlers:
            if isinstance(handler, FileHandler) or isinstance(handler, RotatingFileHandler):
                handler.setLevel(level)