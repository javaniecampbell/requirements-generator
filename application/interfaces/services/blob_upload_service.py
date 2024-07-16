from abc import ABC, abstractmethod


class BlobUploadService(ABC):
    """
    Interface for uploading blobs to a storage service.
    """

    @abstractmethod
    def upload_blob(self, blob_name: str, blob_data: bytes) -> str:
        """
        Uploads a blob to a storage service.

        Args:
            blob_name (str): The name of the blob.
            blob_data (bytes): The data of the blob.

        Returns:
            str: The URL of the uploaded blob.
        """
        ...

    @abstractmethod
    def upload_blob(self, container_name: str, blob_name: str, blob_data: bytes) -> str:
        """
        Uploads a blob to a storage service.

        Args:
            container_name (str): The name of the container.
            blob_name (str): The name of the blob.
            blob_data (bytes): The data of the blob.

        Returns:
            str: The URL of the uploaded blob.
        """
        ...
