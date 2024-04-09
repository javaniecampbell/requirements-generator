from datetime import datetime
import re
import time
import os
from dotenv import load_dotenv
from openai import OpenAI
import uvicorn
from ai_helper_functions import (
    GPT_3_5_TURBO_0613,
    GPT_4_32K_0613,
    calculate_cost,
    num_tokens_from_messages,
)
from domain.domain_event import DomainEvent
from domain.event_bus import EventBus

from functions import read_file, write_to_md
from models.models import read_csv_data
from observability.instrumentation import instrument
from prompts import (
    cleanup_transcript,
    generate_functional_non_functional_requirements,
    generate_user_stories_with_acceptance_criteria,
    plan_product_epics_features_scenarios_from,
)

load_dotenv()

client = OpenAI()
instrument()
md_file = f"requirements-{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.md"


def app():
    # Input
    transcript = read_file("data/transcript.md")

    # Inputs/Outputs
    cleaned_up_transcript = ""
    requirements = ""
    epics_feature_list = ""
    user_stories = ""
    clean_up_prompt = read_file("prompts/cleanup_prompt.md")

    functional_non_functional_requirements_prompt = read_file(
        "prompts/functional_non_functional_requirements_prompt.md"
    )

    product_planner_prompt = read_file("prompts/product_planner_prompt.md")

    user_story_acceptance_criteria_writer_prompt = read_file(
        "prompts/user_story_acceptance_criteria_writer_prompt.md"
    )

    print("Start...")

    # Example usage:
    filepath = os.path.join(os.path.dirname(__file__), "data", "openai-pricelist.csv")
    num_tokens = num_tokens_from_messages(clean_up_prompt, GPT_3_5_TURBO_0613)
    model_data_list = read_csv_data(filepath)
    cost = calculate_cost(num_tokens, GPT_3_5_TURBO_0613, model_data_list)
    print(
        f"Total cost for {num_tokens} tokens using model '{GPT_3_5_TURBO_0613}': ${cost:.6f}\n\n"
    )
    # Step 1 - Cleanup the interview transcript for the product or project received from client
    print(
        "Step 1 - Cleanup the interview transcript for the product or project received from client\n\n"
    )
    transcript_stream, messages = cleanup_transcript(transcript, stream=True)
    print(f"Cleaned up transcript:\n\n")
    for chunk in transcript_stream:
        if chunk.choices[0].delta.content is not None:
            cleaned_up_transcript += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    write_to_md(md_file, f"""## Cleaned up transcript:\n{cleaned_up_transcript}\n---""")
    time.sleep(5)
    # Step 1.1 - Create a questionnaire to capture the functional and non-functional requirements for the product or project
    # Step 1.1.1 - Generate the functional and non-functional requirements from the questionnaire results for the product or project
    # OR ALTERNATIVELY
    # Step 1.2 - Generate the functional and non-functional requirements from transcript for the product or project
    print(
        "Step 2 - Generate the functional and non-functional requirements from transcript for the product or project\n\n"
    )
    requirements_stream, messages = generate_functional_non_functional_requirements(
        cleaned_up_transcript, stream=True
    )
    print(f"\nFunctional & Non-Functional:\n\n")
    for chunk in requirements_stream:
        if chunk.choices[0].delta.content is not None:
            requirements += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    write_to_md(md_file, f"""## Functional & Non-Functional:\n{requirements}\n---""")

    # Step 2 - Generate a list of epics and features from the functional and non-functional requirements
    # epics_feature_list = []
    time.sleep(5)
    print(
        "Step 3 - Generate a list of epics and features from the functional and non-functional requirements\n\n"
    )
    epics_feature_stream, messages = plan_product_epics_features_scenarios_from(
        requirements, stream=True
    )
    print("\nPlanned Product Epics, Features & Scenarios:\n\n")
    for chunk in epics_feature_stream:
        if chunk.choices[0].delta.content is not None:
            epics_feature_list += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    write_to_md(
        md_file,
        f"""## Planned Product Epics, Features & Scenarios:\n{epics_feature_list}\n---""",
    )
    # Step 3 - Generate user stories with acceptance criteria from the epics & features list

    time.sleep(5)
    print(
        "Step 4 - Generate user stories with acceptance criteria from the epics & features list\n\n"
    )
    user_stories_stream, messages = generate_user_stories_with_acceptance_criteria(
        epics_feature_list, stream=True
    )
    print("\nPlanned Product Epics, Features & Scenarios:\n\n")
    for chunk in user_stories_stream:
        if chunk.choices[0].delta.content is not None:
            user_stories += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    write_to_md(
        md_file, f"""## User Stories with Acceptance Criteria:\n{user_stories}\n---"""
    )
    # Step 4 - Generate a template for the product owner to review and approve
    template = f"""
# Product Owner Template\n
## Cleaned up transcript:\n

{cleaned_up_transcript}
---\n
## Functional & Non-Functional:\n

{requirements}
---\n
## Epics & Feature List:\n

{epics_feature_list}
---\n
## User Stories with Acceptance Criteria:\n

{user_stories}
---\n
    """
    print(f"\n{template}\n\n")
    # Usage
    # EventBus.publish(DomainEvent(
    #     name="FeatureAdded",
    #     data={
    #         "epic": "As a user, I want to view a list of products",
    #         "feature": "View product list page"
    #     })
    # )
    EventBus.subscribe(on_feature_added)
    time.sleep(5)


# Event Handlers
def on_feature_added(event: DomainEvent):
    if event.name == "FeatureAdded":
        print(
            f"Event: '{event.name}' - Feature '{event.data['feature']}' added to Epic '{event.data['epic']}'"
        )


def main():
    uvicorn.run("api.app:app", port=5000, log_level="info", reload=True)


if __name__ == "__main__":
    main()
