from datetime import datetime
import time
import os
from dotenv import load_dotenv
from openai import OpenAI
import markdown
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
from prompts import (
    cleanup_transcript,
    generate_functional_non_functional_requirements,
    generate_user_stories_with_acceptance_criteria,
    plan_product_epics_features_scenarios_from,
)

load_dotenv()

client = OpenAI()
md_file = f"requirements{datetime.now().strftime('%d-%m-%Y-%H-%M-%S')}.md"


def main():
    # Input
    transcript = """
  Alright, I'm trying to build a escrow service. What I would want it to do is allow for developers or clients to basically sign up on the platform. Once they sign up, they'll be able to be presented to their dashboard where they'll have a series of actions. One, they'll be able to create project and from creating the project the project will start with a questionnaire. The questionnaire will then be the questionnaire will guide the person through a series of questions to initially create a project. Once the questionnaire is completed it's going to give them a list of potential features similar to the code engine, basically the code engine. Once that is presented, they can then go ahead from the code to generate the requirements. The requirements breakdown is going to take a set of, to take a set of prompts that's going to generate, that's going to ask GPT model or LLM model to plan the potential features for each and each one of those will be saved to our requirements table. Once the requirements are generated and the customer is satisfied with that, he will then be able to be presented to review the requirements in its entirety. Once that happens, by the way, once the requirements is generated, the custom, well, the requirements is sent to the developer portal or the service provider portal to say that a new project has been created and here is a list of the projects. Once that is done, the requirements can then be broken down into stories, grouped into set number of stories and or features. Each requirement can have multiple features. Those features can then be broken down into stories. So the LLM will then go ahead and plan what the features are. And the same thing will be done for breaking down stories into into smaller bits. Yeah. Those broken down features can actually be used to write gherkin later to basically kick-start a project phase of it based on the requirements and based on the list of stories. We will then generate a proposal from that from from the initial requirements data. The proposal will then be generated, which will include the amount of the pricing that comes from the quote engine, or better yet, the quote and the requirements will be generated to create a proposal. That proposal will then be sent to the client. It will have a series of feedback based on what the persons need to change. Once that is done, it will allow for the application to ask for the client's signature and approval. Once approved, that will then turn into a contract and that contract will then be sent to the client with the expect with the milestones with requirements and the milestones that need to be achieved and cost for each milestone based on what would have been generated for the features and selected for a certain thing so that allows the client to basically create project, submit there what they want based on a questionnaire, they can also submit free text which will then be parsed out into requirements later and reviewed and turned into the same flow for the contract. Once all that is done and they review the client signed to contract, they will then be be added to a project view of that project with all the milestones that need to be accomplished. Once a developer takes that up, a service provider takes that up and start working on the features, that could then be peered into stories on Azure DevOps board. Once that is created and completed, it will then send a webhook to basically update the status of that milestone. Once the milestone is completed, the developer or service provider can upload an asset or based on the CICD pipeline that will be connected to it, once that feature has a pull request has been completed, it will then be taken, it will then be uploaded to the digital assets section where it will have either a preview or potentially a link to the asset itself, right? Yeah. A digital asset node can either be files, images, files such as images, HTML, web documents and or a URL, yeah? could be from there, the person with the digital asset, once the person click on a milestone, the milestone will have a number of digital assets. Those digital assets can then be, can generate a preview link, which is going to be valid for a configurable amount of time. Once they have viewed it and the time, once they have either viewed it and the time has expired, let's say 24 hours or no, it will only be valid for that time period. After which expiration has happened. They would have to pay, um, the, you know, for them to receive that product. Yeah. They would have to pay. Um, yeah, they will have to pay. They'll have to pay to, to, to grab the intro that, that is delivered to them permanently. Um, The idea of everything is that the escrow service is that the client will, the idea of the escrow service at this point is that the client will basically pay to an account that will be created for them once they have been, once they were create, once they, they signed up for the platform. All right. So we'll be using probably strike connect, which creates an account when the customer create, once a client become, um, Once a client creates a project and pays for it, they become, they move from, once they're qualified outside of a lead into a paying client, meaning that they have paid for the invoice already, or they've paid or signed the contract and everything in between, they create an account. In order for the project to start, they have to fund the escrow account. how they'll be able to do that. Once they click on their project, I am envisioning that they will then be able to select a number of milestones of which they want to pay for and they pay for that. Once the milestone has been paid for, per se, the work can start on it. And once the work has been completed, that will then trigger a payout. Well, it will go into even a number of period where the client can see the milestone we uploaded, they review it, they upload their feedback in the thing that they'll have a number of iterations. Let's say their iteration will give them around five, four iterations, all right? If the iteration varies too far, then we will have to construct a new feature altogether, and they have to still pay for this milestone, before that can go through. Once they have completed number of iterations, if they want more iterations in fixing this part of it, they'll have to pay for it like credits. That's an upfront payment, non-refundable. Once they have done that, right? And we can either pay it upfront or we can ask them to, or it can be added to their credits, to their overall payment, which will inflate their bill, whichever one. But the idea is once that is done, they will be able to get their product or ask for it to be deployed to their respective area. Depends on how they want delivery to happen. So once they have paid, they can then click on it and ask how they want delivery. They can download the asset, which is going to be a number of downloads after payment. Only when payment is confirmed, that will turn into a donatable link, or they will pay additional for deployment services, which will be deployed into the various environment for them or migrated, which can either be a part of the package or not a part of the package. All right. Once the persons have violated, Once the person's finalized the milestone, the payout will then, they can, the payout will become available. We're, we can do it in two ways. The either the client, either the client enact payout, once payout is sent from their, from their, their, their, their respective account, then, and only then, the, the milestone become available to find a download or for deployment. Once that is done, once a playout is being triggered, a transfer into the receiving party or service provider account, so that, so that, so that they can confirm payment. So once it lands into the service provider's account, it's confirmed and the milestone becomes a download. Yeah, that's essentially it. And that process continues until all milestones in the contract has been provided. Yeah, Martin. That sounds like a legit flow. All right, the off-boarding process, Once everything has been delivered, we can then... Yeah, that's actually amazing. We can get into the off-boarding process afterwards. But so far, the flow for that will be just that. 
  """

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
        f"""## Planned Product Epics, Features & Scenarios:\n{epics_feature_list}\n---"""
    )
    # Step 3 - Generate user stories with acceptance criteria from the epics & features list
    user_stories_stream, messages = generate_user_stories_with_acceptance_criteria(
        epics_feature_list, stream=True
    )
    print("\nPlanned Product Epics, Features & Scenarios:\n\n")
    for chunk in user_stories_stream:
        if chunk.choices[0].delta.content is not None:
            user_stories += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    write_to_md(f"""## User Stories with Acceptance Criteria:\n{user_stories}\n---""")
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
    EventBus.subscribe(on_feature_added)
    time.sleep(5)


# Event Handlers
def on_feature_added(event: DomainEvent):
    if event.name == "FeatureAdded":
        print(
            f"Event: '{event.name}' - Feature '{event.data['feature']}' added to Epic '{event.data['epic']}'"
        )


if __name__ == "__main__":
    main()
