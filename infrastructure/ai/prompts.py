from email import message
from pyexpat.errors import messages
import re
from openai import OpenAI
from dotenv import load_dotenv

from infrastructure.ai.tools.ai_helper_functions import GPT_4o
from infrastructure.ai.tools.functions import read_file


load_dotenv()
client = OpenAI()


# Step 1 - Clean up the transcript from client
def cleanup_transcript(transcript, stream=False):
    """
    Responsible for cleaning up the transcript of any unnecessary detail down to the core of the explanation received from client

    Args:
        transcript (str): The transcript to be cleaned up.

    Returns:
        str: The cleaned up transcript.

    Examples:
        >>> transcript = "This is a sample transcript with unnecessary details."
        >>> cleaned_transcript = cleanup_transcript(transcript)
        >>> print(cleaned_transcript)
        "This is the core explanation received from the client."

    """

    cleaned_up_transcript = ""
    clean_up_prompt = read_file("content/prompts/cleanup_prompt.md")
    clean_up_prompt = clean_up_prompt.replace("{transcript}", transcript)
    messages = [
        {"role": "system", "content": clean_up_prompt},
        {
            "role": "user",
            "content": f'''Clenaup the interview transcript for the product or project received from client
                    

                    """
                    {transcript}
                    """

                    ''',
        },
    ]
    if stream is True:
        transcript_stream = client.chat.completions.create(
            model=GPT_4o,
            messages=messages,
            stream=stream,
        )
        return transcript_stream, messages
    else:
        cleaned_up_transcript = client.chat.completions.create(
            model=GPT_4o,
            messages=messages,
            stream=stream,
        )
        return cleaned_up_transcript, messages


# Step 2 - Generate functional & non-functional requirements from cleaned up transcript
def generate_functional_non_functional_requirements(
    cleaned_up_transcript, stream=False
):
    """
    Responsible for generating the functional & non-functional requirements from the cleaned up prompt output

    Args:
        cleaned_up_transcript (str): The cleaned up transcript of the client or user explanation.

    Returns:
        str: The generated functional and non-functional requirements.

    Examples:
        >>> cleaned_up_transcript = "The system should allow users to create an account and login securely."
        >>> generate_functional_non_functional_requirements(cleaned_up_transcript)
        'Requirements: The system should have a user registration feature that allows users to create an account. The system should also have a secure login feature.'

        >>> cleaned_up_transcript = "The system should be able to handle a large number of concurrent users without performance degradation."
        >>> generate_functional_non_functional_requirements(cleaned_up_transcript)
        'Requirements: The system should be scalable and able to handle a large number of concurrent users without any noticeable performance degradation.'
    """

    requirements = ""
    functional_non_functional_requirements_prompt = read_file(
        "content/prompts/functional_non_functional_requirements_prompt.md"
    )
    functional_non_functional_requirements_prompt = (
        functional_non_functional_requirements_prompt.replace(
            "{cleaned_up_transcript}", cleaned_up_transcript
        )
    )
    messages = [
        {
            "role": "system",
            "content": functional_non_functional_requirements_prompt,
        },
        {
            "role": "user",
            "content": f'''Generate ALL functional and non-functional requirements from transcript when complete output <FINISH>
                

                Transcript:
                """
                {cleaned_up_transcript}
                """
                ''',
        },
    ]
    if stream is True:
        requirements_stream = client.chat.completions.create(
            model=GPT_4o,
            messages=messages,
            stream=stream,
        )
        return requirements_stream, messages
    else:
        requirements = client.chat.completions.create(
            model=GPT_4o,
            messages=messages,
            stream=stream,
        )
        return requirements, messages


# Step 3 - Plan epics, features and scenarios for the product or project from the output produced by the functional & non-functional requirements prompt
def plan_product_epics_features_scenarios_from(requirements, stream=False):
    """
    Responsible for creating epics and features from the output produced by the functional & non-functional requirements prompt.

    Args:
        requirements (str): The functional and non-functional requirements provided as a string.

    Returns:
        str: The generated epics and features as a string.

    Examples:
        >>> requirements = "Some example requirements"
        >>> plan_product_epics_features_scenarios_from(requirements)
        'Generated epics and features'

    """

    epics_feature_list = ""
    product_planner_prompt = read_file("content/prompts/product_planner_prompt.md")
    product_planner_prompt = product_planner_prompt.replace(
        "{requirements}", requirements
    )
    messages = [
        {
            "role": "system",
            "content": product_planner_prompt,
        },
        {
            "role": "user",
            "content": f'''Plan the epics, features and scenarios from the functional and non-functional requirements when complete output <FINISH>
                    
                    Requirements:

                    """
                    {requirements}
                    """
            
                    ''',
        },
    ]

    if stream is True:
        epics_feature_stream = client.chat.completions.create(
            model=GPT_4o,
            messages=messages,
            stream=stream,
        )
        return epics_feature_stream, messages
    else:
        epics_feature_list = client.chat.completions.create(
            model=GPT_4o,
            messages=messages,
            stream=stream,
        )
        return epics_feature_list, messages


def generate_user_stories_with_acceptance_criteria(epics_feature_list, stream=False):
    """
    Responsible for creating user stories and acceptance criteria from the epics & features list.

    Args:
        epics_feature_list (str): The list of epics and features.

    Returns:
        str: The generated user stories with acceptance criteria.

    Examples:
        >>> epics_feature_list = "Feature 1\nFeature 2\nFeature 3"
        >>> generate_user_stories_with_acceptance_criteria(epics_feature_list)
        'User Stories with Acceptance Criteria'

    """

    user_stories_with_acceptance_criteria = ""

    user_story_acceptance_criteria_writer_prompt = read_file(
        "content/prompts/user_story_acceptance_criteria_writer_prompt.md"
    )
    user_story_acceptance_criteria_writer_prompt = (
        user_story_acceptance_criteria_writer_prompt.replace(
            "{epics_feature_list}", epics_feature_list
        )
    )
    messages = [
        {
            "role": "system",
            "content": user_story_acceptance_criteria_writer_prompt,
        },
        {
            "role": "user",
            "content": f'''Generate user stories with acceptance criteria from the epics, features & scenarios list when complete output <FINISH>
                    
                    Epics, Features & Scenarios List:

                    """
                    {epics_feature_list}
                    
                    ''',
        },
    ]
    if stream is True:
        user_stories_stream = client.chat.completions.create(
            model=GPT_4o,
            messages=messages,
            stream=stream,
        )
        return user_stories_stream, messages
    else:
        user_stories_with_acceptance_criteria = client.chat.completions.create(
            model=GPT_4o,
            messages=messages,
            stream=stream,
        )
        return user_stories_with_acceptance_criteria, messages
