from typing import List, Union


# Functional & Non-Functional Requirements
class Requirement:
    """
    Represents a requirement.

    Attributes:
        id (str): The unique identifier of the requirement.
        description (str): The description of the requirement.
        priority (str): The priority of the requirement.
        status (str): The status of the requirement. Can be "Pending", "Approved", or "Implemented".
        type (str): The type of the requirement. Can be "Functional" or "Non-Functional".
    """

    def __init__(
        self, id: str, description: str, priority: str, status: str, type: str
    ):
        """
        Initialize a Requirement object.

        Args:
            id (str): The unique identifier for the requirement.
            description (str): The description of the requirement.
            priority (str): The priority of the requirement.
            status (str): The status of the requirement.
            type (str): The type of the requirement.
        """
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self.type = type


class NonFunctionalRequirement(Requirement):
    """
    Represents a non-functional requirement.

    Attributes:
        id (str): The unique identifier of the requirement.
        description (str): The description of the requirement.
        priority (str): The priority of the requirement.
        status (str): The status of the requirement.
        category (str): The category of the non-functional requirement.
            Possible values are "Performance", "Security", "Usability", "Reliability".
    """

    def __init__(
        self, id: str, description: str, priority: str, status: str, category: str
    ):
        """
        Initializes a NonFunctionalRequirement object.

        Args:
            id (str): The unique identifier for the requirement.
            description (str): The description of the requirement.
            priority (str): The priority of the requirement.
            status (str): The status of the requirement.
            category (str): The category of the requirement.

        Returns:
            None
        """
        super().__init__(id, description, priority, status, "Non-Functional")
        self.category = category


class RequirementCategory:
    """
    Represents a category of requirements (e.g., User Registration, Project Creation).

    Attributes:
        id (str): The unique identifier of the category.
        title (str): The title of the category.
        requirements (List[Union[Requirement, NonFunctionalRequirement]]): The list of requirements under this category.
    """

    def __init__(
        self,
        id: str,
        title: str,
        requirements: List[Union[Requirement, NonFunctionalRequirement]],
    ):
        """
        Initialize a RequirementCategory object.

        Args:
            id (str): The unique identifier for the category.
            title (str): The title of the category.
            requirements (List[Union[Requirement, NonFunctionalRequirement]]): The list of requirements under this category.
        """
        self.id = id
        self.title = title
        self.requirements = requirements


"""
Example usage:
functional_requirements = [
    Requirement("FR1.1", "The system should allow developers or clients to sign up on the platform.", "High", "Pending", "Functional"),
    Requirement("FR1.2", "Upon signing up, users should be provided with a dashboard to perform various actions.", "High", "Pending", "Functional"),
    Requirement("FR2.1", "Users should be able to create a project.", "High", "Pending", "Functional"),
    Requirement("FR2.2", "The project creation process should begin with a questionnaire that guides the user through a series of questions.", "High", "Pending", "Functional"),
    Requirement("FR2.3", "Upon completing the questionnaire, the system should provide the user with a list of potential features similar to the code engine.", "Medium", "Pending", "Functional"),
    Requirement("FR3.1", "Users should be able to generate requirements based on the questionnaire responses.", "High", "Pending", "Functional"),
    Requirement("FR3.2", "The requirement generation process should involve using prompts to ask a GPT or LLM model to plan the potential features.", "High", "Pending", "Functional"),
    Requirement("FR3.3", "Each requirement generated should be saved to a requirements table.", "High", "Pending", "Functional"),
    Requirement("FR4.1", "Users should be able to review the generated requirements in its entirety.", "Medium", "Pending", "Functional"),
    Requirement("FR4.2", "The system should provide a platform or portal for developers or service providers to view a list of new projects and receive notifications about them.", "Medium", "Pending", "Functional"),
    Requirement("FR5.1", "The generated requirements should be broken down into stories.", "High", "Pending", "Functional"),
    Requirement("FR5.2", "Stories should be grouped into a specific number of stories or features.", "High", "Pending", "Functional"),
    Requirement("FR5.3", "Each requirement can have multiple features, which can further be broken down into stories.", "High", "Pending", "Functional"),
    Requirement("FR6.1", "The system should support the writing of Gherkin, which is a business-readable domain-specific language for behavior-driven development.", "Medium", "Pending", "Functional"),
    Requirement("FR6.2", "Gherkin should be used to kick-start the project phase based on the generated requirements and list of stories.", "Medium", "Pending", "Functional"),
    Requirement("FR7.1", "Based on the initial requirements data, the system should generate a proposal.", "Medium", "Pending", "Functional"),
    Requirement("FR7.2", "The proposal should include pricing obtained from the quote engine.", "Medium", "Pending", "Functional"),
    Requirement("FR7.3", "The generated proposal should be sent to the client for feedback.", "Medium", "Pending", "Functional"),
    Requirement("FR8.1", "Once the client approves the proposal, it should be converted into a contract.", "High", "Pending", "Functional"),
    Requirement("FR8.2", "The contract should include milestones, requirements, and costs for each milestone.", "High", "Pending", "Functional"),
    Requirement("FR8.3", "The contract should be sent to the client for review and signature.", "High", "Pending", "Functional")
]

non_functional_requirements = [
    NonFunctionalRequirement("NFR1.1", "The platform should have a user-friendly interface to ensure ease of navigation and understanding for developers and clients.", "High", "Pending", "Usability"),
    NonFunctionalRequirement("NFR2.1", "The system should be able to handle multiple user registrations, project creations, and requirement generations simultaneously without any significant performance issues.", "High", "Pending", "Performance"),
    NonFunctionalRequirement("NFR3.1", "The platform should be reliable and available to users at all times. Requirements should be saved securely and reliably in the requirements table.", "High", "Pending", "Reliability"),
    NonFunctionalRequirement("NFR3.2", "The system should be capable of parsing free text submissions from clients into requirements and reviewing them for inclusion in the contract.", "Medium", "Pending", "Reliability"),
    NonFunctionalRequirement("NFR4.1", "The system should be able to integrate with the developer portal or service provider portal to notify them of new projects and provide a list of projects.", "Medium", "Pending", "Integration"),
    NonFunctionalRequirement("NFR5.1", "The platform should ensure the security and confidentiality of user information and project data. Access to the requirements table and contract information should be restricted to authorized personnel only.", "High", "Pending", "Security")
]

categories = [
    RequirementCategory("FR1", "User Registration", functional_requirements[:2]),
    RequirementCategory("FR2", "Project Creation", functional_requirements[2:5]),
    RequirementCategory("FR3", "Requirement Generation", functional_requirements[5:8]),
    RequirementCategory("FR4", "Requirement Review", functional_requirements[8:10]),
    RequirementCategory("FR5", "Requirement Breakdown", functional_requirements[10:13]),
    RequirementCategory("FR6", "Gherkin Writing", functional_requirements[13:15]),
    RequirementCategory("FR7", "Proposal Generation", functional_requirements[15:18]),
    RequirementCategory("FR8", "Contract Creation", functional_requirements[18:21])
]

non_functional_categories = [
    RequirementCategory("NFR1", "Usability", [non_functional_requirements[0]]),
    RequirementCategory("NFR2", "Performance", [non_functional_requirements[1]]),
    RequirementCategory("NFR3", "Reliability", non_functional_requirements[2:4]),
    RequirementCategory("NFR4", "Integration", [non_functional_requirements[4]]),
    RequirementCategory("NFR5", "Security", [non_functional_requirements[5]])
]
"""
