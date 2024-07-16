from abc import ABC, abstractmethod


from abc import ABC, abstractmethod


class ReadFileService(ABC):
    """Interface for reading files."""

    @abstractmethod
    def read_file(self, file_path: str) -> bytes:
        """Reads the contents of a file and returns them as bytes.

        Args:
            file_path (str): The path to the file.

        Returns:
            bytes: The contents of the file as bytes.
        """
        pass
