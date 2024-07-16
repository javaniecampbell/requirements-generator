from application.interfaces.services.blob_upload_service import BlobUploadService
from azure.storage.blob import BlobServiceClient

storage_account_name = "your_storage_account_name"
storage_account_key = "your_storage_account_key"
connection_string = f"DefaultEndpointsProtocol=https;AccountName={storage_account_name};AccountKey={storage_account_key};EndpointSuffix=core.windows.net"
container_name = "your_container_name"


class StorageBlobUploadService(BlobUploadService):
    """
    A class that provides methods to upload blobs to Azure Blob Storage.
    """

    def __init__(self, connection_string):
        """
        Initializes a new instance of the StorageBlobUploadService class.

        Args:
            connection_string (str): The connection string for the Azure Blob Storage account.
        """
        self.blob_service_client = BlobServiceClient.from_connection_string(
            connection_string
        )

    def upload_blob(self, container_name, blob_name, data) -> str:
        """
        Uploads a blob to the specified container in Azure Blob Storage.

        Args:
            container_name (str): The name of the container.
            blob_name (str): The name of the blob.
            data (bytes): The data to be uploaded.

        Returns:
            str: The URL of the uploaded blob.
        """
        # If the container does not exist, create a new container with the name specified
        container_client = self.blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()

        # Create a blob client using the local file name as the name for the blob
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )
        blob_client.upload_blob(data)
        return blob_client.url

    def upload_blob(self, blob_name, data) -> str:
        """
        Uploads a blob to the default container in Azure Blob Storage.

        Args:
            blob_name (str): The name of the blob.
            data (bytes): The data to be uploaded.

        Returns:
            str: The URL of the uploaded blob.
        """
        blob_client = self.blob_service_client.get_blob_client(
            container=container_name, blob=blob_name
        )
        blob_client.upload_blob(data)
        return blob_client.url
