from typing import List
import tiktoken

from models.models import ModelData

GPT_3_5_TURBO_0301 = "gpt-3.5-turbo-0301"
GPT_3_5_TURBO_0613 = "gpt-3.5-turbo-0613"
GPT_3_5_TURBO_16K_0613 = "gpt-3.5-turbo-16k-0613"
GPT_3_5_TURBO = "gpt-3.5-turbo"
GPT_4_0314 = "gpt-4-0314"
GPT_4_32K_0314 = "gpt-4-32k-0314"
GPT_4_0613 = "gpt-4-0613"
GPT_4_32K_0613 = "gpt-4-32k-0613"
GPT_4 = "gpt-4"


def num_tokens_from_messages(messages, model=GPT_3_5_TURBO_0613):
    """
    Return the number of tokens used by a list of messages.

    Args:
        messages (str or list): The messages to count the tokens for. If a string is provided, it will be wrapped in a list.
        model (str): The model to use for token counting. Defaults to GPT_3_5_TURBO_0613.

    Returns:
        int: The total number of tokens used by the messages.

    Raises:
        NotImplementedError: If the provided model is not supported.

    Notes:
        - The function counts the tokens based on the specified model and the structure of the messages.
        - The token count includes the tokens used for message content, names, and special tokens like <|im_start|> and <|im_sep|>.
        - For certain models, specific token counts are assigned based on the model type.

    Examples:
        >>> messages = [
        ...     {"content": "Hello, how are you?"},
        ...     {"content": "I'm doing great!", "name": "User"}
        ... ]
        >>> num_tokens_from_messages(messages)
        12
    """
    if isinstance(messages, str):
        # If messages is a string, wrap it in a list to make it iterable
        messages = [{"content": messages}]

    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print("Warning: model not found. Using cl100k_base encoding.")
        encoding = tiktoken.get_encoding("cl100k_base")
    if model in {
        GPT_3_5_TURBO_0613,
        GPT_3_5_TURBO_16K_0613,
        GPT_4_0314,
        GPT_4_32K_0314,
        GPT_4_0613,
        GPT_4_32K_0613,
    }:
        tokens_per_message = 3
        tokens_per_name = 1
    elif model == GPT_3_5_TURBO_0301:
        tokens_per_message = (
            4  # every message follows <|im_start|>{role/name}\n{content}<|end|>\n
        )
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif GPT_3_5_TURBO in model:
        print(
            "Warning: gpt-3.5-turbo may update over time. Returning num tokens assuming gpt-3.5-turbo-0613."
        )
        return num_tokens_from_messages(messages, model=GPT_3_5_TURBO_0613)
    elif GPT_4 in model:
        print(
            "Warning: gpt-4 may update over time. Returning num tokens assuming gpt-4-0613."
        )
        return num_tokens_from_messages(messages, model="gpt-4-0613")
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|im_start|>assistant<|im_sep|>
    return num_tokens


def calculate_cost(
    num_tokens: int, model_identifier: str, model_data_list: List[ModelData]
) -> float:
    """
    Calculates the cost based on the number of tokens and the specified model.

    Args:
        num_tokens (int): The number of tokens.
        model_identifier (str): The identifier of the model.
        model_data_list (List[ModelData]): The list of model data.

    Returns:
        float: The total cost.

    Raises:
        ValueError: If the specified model is not found in the provided data.
        ValueError: If the pricing information for the specified model is incomplete.
    """
    # Find the model data for the specified model
    selected_model_data = next(
        (data for data in model_data_list if data.model == model_identifier), None
    )

    if not selected_model_data:
        raise ValueError(f"Model '{model_identifier}' not found in provided data.")

    # Determine the pricing tier based on the number of tokens
    if num_tokens >= 1_000_000:
        cost_per_token = selected_model_data.input_per_1m_tokens / 1_000_000
    elif num_tokens >= 1_000:
        cost_per_token = selected_model_data.input_per_1k_tokens / 1_000
    else:
        cost_per_token = selected_model_data.input_per_token

    if cost_per_token is None:
        raise ValueError(f"Pricing information for '{model_identifier}' is incomplete.")

    # Calculate the total cost
    total_cost = num_tokens * cost_per_token

    return total_cost


# Example usage:
# num_tokens = num_tokens_from_messages(your_messages, your_model)
# model_data_list = read_csv_data('your_csv_file_path_here.csv')
# cost = calculate_cost(num_tokens, your_model, model_data_list)
# print(f"Total cost for {num_tokens} tokens using model '{your_model}': ${cost:.2f}")
