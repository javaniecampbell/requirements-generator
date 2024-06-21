from openai import OpenAI

from ai.tools.ai_helper_functions import GPT_3_5_TURBO_0613


def chat_openai(client: OpenAI, prompt: str, model=GPT_3_5_TURBO_0613):
    """
    chat_openai sends a prompt to the OpenAI API and returns the
    response along with the conversation history.

    Parameters:
      client (OpenAI): The OpenAI API client
      prompt (str): The prompt to send to the API
      model (str): The API model to use (default is GPT-3.5 Turbo)

    Returns:
      dict:
        answer (str): The API response
        conversation (list): The conversation history
        response (OpenAI object): The full API response
    """
    conversation = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model, messages=conversation, temperature=0
    )
    answer += response.choices[0].message.content
    conversation.append({"role": response.choices[0].message.role, "content": answer})
    return {"answer": answer, "conversation": conversation, "response": response}
