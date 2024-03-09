from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()


# Step 1 - Clean up the transcript from client
def cleanup_transcript(transcript):
    """
    Responsible for cleaning up the transcript of any unnecessary detail down to the core of the explanation received from client
    """
    cleaned_up_transcript = ""
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

    # TODO: Implement the clean up llm call here
    return cleaned_up_transcript


# Step 2 - Generate functional & non-functional requirements from cleaned up transcript
def generate_functional_non_functional_requirements(cleaned_up_transcript):
    """
    Responsible for generating the functional & non-functional requirements from the cleaned up prompt output
    """
    requirements = ""
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
    # TODO: Implement the functional & non-functional llm call here
    
    return requirements


# Step 3 - Plan epics, features and scenarios for the product or project from the output produced by the functional & non-functional requirements prompt
def plan_product_epics_features_scenarios_from(requirements):
    """
    Responsible for creating epics and features from the output produced by the functional & non-functional requirements prompt.
    """
    epics_feature_list = ""
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

    # TODO: Implement the product planner call here
    return  epics_feature_list


def generate_user_stories_with_acceptance_criteria(epics_feature_list):
    """
    Responsible for creating user stories and acceptance criteria from the epics & features list.
    """
    user_stories_with_acceptance_criteria = ""

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

    # TODO: Implement generate user stories llm call here
    return user_stories_with_acceptance_criteria
