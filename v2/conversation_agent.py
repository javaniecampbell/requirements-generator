from openai import OpenAI
from ai_helper_functions import GPT_3_5_TURBO_0613


class ConversationAgent:
    def __init__(self, client: OpenAI, model=GPT_3_5_TURBO_0613):
        self.model = model
        self._client = client
        self.conversation = []

    def continue_conversation(self, conversation, next_prompt: str):
        # make the first API call
        response = self._client.chat.completions.create(
            model=self.model, messages=conversation, temperature=1
        )
        # TODO: Verify if this needs to happen here
        # conversation.append(
        #     {
        #         "role": response.choices[0].message.role,
        #         "content": response.choices[0].message.content,
        #     }
        # )

        # Check if the response is incomplete
        if response.choices[0].finish_reason == "length":
            # Append the response to the conversation
            conversation.append({"role": "user", "content": next_prompt})

            # Continue the conversation recursilvely
            next_response = self.continue_conversation(
                conversation=conversation, next_prompt=next_prompt
            )
            conversation.append(
                {
                    "role": next_response.choices[0].message.role,
                    "content": next_response.choices[0].message.content,
                }
            )
            return next_response
        if response.choices[0].finish_reason == "stop":
            # TODO: Verify if it should happen here
            # conversation.append(
            #     {
            #         "role": response.choices[0].message.role,
            #         "content": response.choices[0].message.content,
            #     }
            # )
            for convo in conversation:
                self.conversation.append(convo)

            return response
