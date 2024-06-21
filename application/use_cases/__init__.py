from abc import ABC, abstractmethod
from typing import Any


class UseCase(ABC):
    """
    Base abstract class for use cases.
    """

    @abstractmethod
    def execute(self, request: Any) -> Any:
        """
        Execute the use case logic.

        Args:
            request (Any): The request object containing the necessary data for the use case.

        Returns:
            Any: The response object containing the result of the use case execution.
        """
        raise NotImplementedError

    def validate_request(self, request: Any) -> None:
        """
        Validate the request object before executing the use case logic.

        Args:
            request (Any): The request object to be validated.

        Raises:
            ValueError: If the request is invalid.
        """
        pass

    def handle_response(self, response: Any) -> Any:
        """
        Handle the response object after executing the use case logic.

        Args:
            response (Any): The response object to be handled.

        Returns:
            Any: The processed response object.
        """
        return response
