from ._logger import CustomLogger
from ._settings import Settings

settings = Settings()
logger = CustomLogger(
    __name__, 
    log_to_file=True, 
    log_file_path=settings.LOG_FILE_PATH
)