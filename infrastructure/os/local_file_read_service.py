import os
from application.interfaces.services.read_file_service import ReadFileService


class LocalFileReadService(ReadFileService):
    """
    A service for reading files from the local file system.

    Inherits from the ReadFileService base class.
    """

    def __init__(self):
        super().__init__()

    def read(self, file_path: str) -> bytes:
        """
        Read the contents of a file from the local file system.

        Args:
            file_path (str): The path to the file to be read.

        Returns:
            bytes: The contents of the file as bytes.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        # Read the file and return the contents as bytes
        with open(file_path, "rb") as data:
            return data.read()
