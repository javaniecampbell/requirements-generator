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

from models.models import read_csv_data
from prompts import cleanup_transcript

load_dotenv()


client = OpenAI()


md_file = "requirements.md"


def write_to_md(text):
    with open(md_file, "a") as f:
        f.write(markdown.markdown(text) + "\n")


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
    clean_up_prompt = f"""
  **Overview**

  Clean up prompt is responsible for cleaning up the transcript of any unnecessary detail down to the core of the explanation received from client

  **System**

  You are a product business analyst that is capable of carefully reviewing the explanation of a client or user, by cleaning up transcript given surrounded by “””, you are tasked with cleaning up the transcript and leaving only what the desired system or product should be free of any speak nuances, repetitive phrases, pauses or grammatical errors.

  **Template**

  You are a product business analyst that is capable of carefully reviewing the explanation of a client or user, by cleaning up transcript given surrounded by “””, you are tasked with cleaning up the transcript and leaving only what the desired system or product should be free of any speak nuances, repetitive phrases, pauses or grammatical errors. 

  ”””
  {transcript}

  “””

  Assistant:

  Cleaned up transcript: 

  …
  """

    functional_non_functional_requirements_prompt = f"""
  **Overview**

  Responsible for generating the functional & non-functional requirements from the cleaned up prompt output

  **System**

  You are a product business analyst that is capable of carefully reviewing the explanation of a client or user, by cleaning up transcript given surrounded by “””, you are tasked with turning  the cleaned up transcript into DEATILED functional and non-functional requirements with a brief description or explanation for each requirement.

  **Template**

  You are a product business analyst that is capable of carefully reviewing the explanation of a client or user, by cleaning up transcript given surrounded by “””, you are tasked with turning  the cleaned up transcript into DEATILED functional and non-functional requirements with a brief description or explanation for each requirement.

  ”””
  Cleaned up transcript:

  {cleaned_up_transcript}

  “””

  Assistant:

  Requirements:

  …
  """

    product_planner_prompt = f"""
  **Overview**

  Responsible for planning of the epics, features and scenarios using Gherkin syntax often used in Behaviour Driven Development

  **System**

  You are an helpful assistant that is capable of planning a product or project after careful review of a client or user explanation of what the desire system or product should be. Your task is write the epics, features and scenarios using Gherkin Syntax denoted by <syntax type=”gherkin”></syntax> tags:

  <syntax type=”gherkin”>
  These are best written using the Cucumber language and Gherkin syntax.

  Feature: Some important feature

  Scenario: Get something
  Given I have something
  When I do something
  Then I get something else

  Scenario: Get something different
  Given I have something
  And I have also some other thing
  When I do something different
  Then I get something different

  </syntax>

  Example:

  Feature: Display Account Balances for Logged In Users

  Scenario: Do not show balance if not logged in
  Given I am not logged on to the mobile banking app
  When I open the mobile banking app
  Then I can see a login page
  And I do not see account balance

  Scenario: Show balance on the accounts page after logging in
  Given I have just logged on to the mobile banking app
  When I load the accounts page
  Then I can see account balance for each of my accounts

  **Template**

  You are an helpful assistant that is capable of planning a product or project after careful review of a client or user explanation of what the desire system or product should be. Your task is write the Epics, Features and Scenarios using Gherkin Syntax denoted by <syntax type=”gherkin”></syntax> tags and all Features should be grouped under an Epic.

  See <example></example> tag for an example of how the epics, features & scenarios was written using the syntax from <syntax type=”gherkin”>…</syntax>.

  <syntax type=”gherkin”>
  These are best written using the Cucumber language and Gherkin syntax.

  Feature: Some important feature

  Scenario: Get something
  Given I have something
  When I do something
  Then I get something else

  Scenario: Get something different
  Given I have something
  And I have also some other thing
  When I do something different
  Then I get something different

  </syntax>

  <example>

  Epic: Account Management

  Feature: Display Account Balances for Logged In Users

  Scenario: Do not show balance if not logged in
  Given I am not logged on to the mobile banking app
  When I open the mobile banking app
  Then I can see a login page
  And I do not see account balance

  Scenario: Show balance on the accounts page after logging in
  Given I have just logged on to the mobile banking app
  When I load the accounts page
  Then I can see account balance for each of my accounts
  </example>

  Given the functional & non-functional requirements denoted by “”” below, generate epics, features and scenarios outlined in your task objective:

  ”””

  Requirements:

  {requirements}

  “””

  Assistant:

  Epics & Feature List

  …
  """

    user_story_acceptance_criteria_writer_prompt = f"""
  **Overview**

  Responsible for creation of user stories and acceptance criteria from the output produced by the product planner prompt. User stories will create using the I.N.V.E.S.T Framework story Description & Gherkin for Story Acceptance Criteria

  **System**

  You are product owner capable of reviewing Epics & Feature List an breaking down feature list into User Stories with Acceptance Criteria using User Story & Acceptance Criteria Formats donated by <syntax type=”story”></syntax>.

  <syntax type=”story”>

  Story Format
  A good User Story should describe the Who (<actor>), What (<feature>) and Why (<benefit>).

  As an <actor>
  I want a <feature>
  So that <benefit>

  Example:

  As an mobile bank customer
  I want to see balance on my accounts
  So that I can make better informed decisions about my spending

  Acceptance Criteria using Cucumber language
  Acceptance Criteria are conditions that a (software) product must satisfy to be accepted by a user, customer or other stakeholder.

  These are best written using the Cucumber language and Gherkin syntax.

  Feature: Some important feature

  Scenario: Get something
  Given I have something
  When I do something
  Then I get something else

  Scenario: Get something different
  Given I have something
  And I have also some other thing
  When I do something different
  Then I get something different

  Example:

  Feature: Some important feature

  Scenario: Do not show balance if not logged in
  Given I am not logged on to the mobile banking app
  When I open the mobile banking app
  Then I can see a login page
  And I do not see account balance

  Scenario: Show balance on the accounts page after logging in
  Given I have just logged on to the mobile banking app
  When I load the accounts page
  Then I can see account balance for each of my accounts

  </syntax>

  Example:

  Feature: Create Project

  Scenario: Fill out questionnaire to create project
    Given the user has signed up and is on their dashboard
    When they select the option to create a project
    Then a questionnaire is presented to guide them in creating the project

  Scenario: Generate requirements from code
    Given the user has completed the questionnaire and is on the project page
    When they select the option to generate requirements from code
    Then the system uses the code to generate requirements and saves them to the requirements table

  Scenario: Review generated requirements
    Given the user has completed the questionnaire and is on the project page
    When they select the option to review the generated requirements
    Then the requirements are displayed for the user to review

  Scenario: Notify developer/service provider about new project
    Given the user has reviewed the requirements and is satisfied with them
    When they select the option to submit the project requirements
    Then the requirements are sent to the developer portal or service provider portal

  Assistant:

  Feature: Create Project

  As a user
  I want to create a project
  So that I can start the escrow process for my development needs

  Acceptance Criteria:
  Scenario: Fill out questionnaire to create project
  Given I am on the dashboard
  When I select the option to create a project
  Then a questionnaire should be presented to guide me in creating the project

  Scenario: Generate requirements from code
  Given I have completed the questionnaire and am on the project page
  When I select the option to generate requirements from code
  Then the system should use the code to generate requirements and save them to the requirements table

  Scenario: Review generated requirements
  Given I have completed the questionnaire and am on the project page
  When I select the option to review the generated requirements
  Then the requirements should be displayed for me to review

  **Template**

  You are product owner capable of reviewing Epics & Feature List an breaking down feature list into User Stories with Acceptance Criteria using User Story & Acceptance Criteria Formats donated by <syntax type=”story”></syntax>.

  See <example></example> tag for how an example of how the user story & acceptance criteria syntax was used from <syntax type=”story”>…</syntax> to write the user stories with acceptance criteria

  <syntax type=”story”>

  Story Format
  A good User Story should describe the Who (<actor>), What (<feature>) and Why (<benefit>).

  As an <actor>
  I want a <feature>
  So that <benefit>

  Example:

  As an mobile bank customer
  I want to see balance on my accounts
  So that I can make better informed decisions about my spending

  Acceptance Criteria using Cucumber language
  Acceptance Criteria are conditions that a (software) product must satisfy to be accepted by a user, customer or other stakeholder.

  These are best written using the Cucumber language and Gherkin syntax.

  Feature: Some important feature

  Scenario: Get something
  Given I have something
  When I do something
  Then I get something else

  Scenario: Get something different
  Given I have something
  And I have also some other thing
  When I do something different
  Then I get something different

  Example:

  Feature: Some important feature

  Scenario: Do not show balance if not logged in
  Given I am not logged on to the mobile banking app
  When I open the mobile banking app
  Then I can see a login page
  And I do not see account balance

  Scenario: Show balance on the accounts page after logging in
  Given I have just logged on to the mobile banking app
  When I load the accounts page
  Then I can see account balance for each of my accounts

  </syntax>

  <example>

  Feature: Create Project

  Scenario: Fill out questionnaire to create project
    Given the user has signed up and is on their dashboard
    When they select the option to create a project
    Then a questionnaire is presented to guide them in creating the project

  Scenario: Generate requirements from code
    Given the user has completed the questionnaire and is on the project page
    When they select the option to generate requirements from code
    Then the system uses the code to generate requirements and saves them to the requirements table

  Scenario: Review generated requirements
    Given the user has completed the questionnaire and is on the project page
    When they select the option to review the generated requirements
    Then the requirements are displayed for the user to review

  Scenario: Notify developer/service provider about new project
    Given the user has reviewed the requirements and is satisfied with them
    When they select the option to submit the project requirements
    Then the requirements are sent to the developer portal or service provider portal

  Assistant:

  Feature: Create Project

  As a user
  I want to create a project
  So that I can start the escrow process for my development needs

  Acceptance Criteria:
  Scenario: Fill out questionnaire to create project
  Given I am on the dashboard
  When I select the option to create a project
  Then a questionnaire should be presented to guide me in creating the project

  Scenario: Generate requirements from code
  Given I have completed the questionnaire and am on the project page
  When I select the option to generate requirements from code
  Then the system should use the code to generate requirements and save them to the requirements table

  Scenario: Review generated requirements
  Given I have completed the questionnaire and am on the project page
  When I select the option to review the generated requirements
  Then the requirements should be displayed for me to review
  </example>

  Given the Epics & Feature List, generate user stories with acceptance criteria as outlined in your task objective please:

  “””
  Epics & Feature List:

  {epics_feature_list}

  “”

  Assistant:

  User Stories with Acceptance Criteria

  …
  """

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
    write_to_md(f"""## Cleaned up transcript:\n{cleaned_up_transcript}\n---""")
    # Step 1.1 - Create a questionnaire to capture the functional and non-functional requirements for the product or project
    # Step 1.1.1 - Generate the functional and non-functional requirements from the questionnaire results for the product or project
    # OR ALTERNATIVELY
    # Step 1.2 - Generate the functional and non-functional requirements from transcript for the product or project
    print(
        "Step 2 - Generate the functional and non-functional requirements from transcript for the product or project\n\n"
    )
    requirements_stream = client.chat.completions.create(
        model=GPT_3_5_TURBO_0613,
        messages=[
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
        ],
        stream=True,
    )
    print(f"\nFunctional & Non-Functional:\n\n")
    for chunk in requirements_stream:
        if chunk.choices[0].delta.content is not None:
            requirements += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content, end="")
    write_to_md(f"""## Functional & Non-Functional:\n{requirements}\n---""")

    # Step 2 - Generate a list of epics and features from the functional and non-functional requirements
    # epics_feature_list = []

    print(
        "Step 3 - Generate a list of epics and features from the functional and non-functional requirements\n\n"
    )
    epics_feature_stream = client.chat.completions.create(
        model=GPT_3_5_TURBO_0613,
        messages=[
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
        ],
        stream=True,
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
    user_stories_stream = client.chat.completions.create(
        model=GPT_3_5_TURBO_0613,
        messages=[
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
        ],
        stream=True,
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
