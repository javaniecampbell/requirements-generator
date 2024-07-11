from typing import List
from domain.entities.epic import Epic
from domain.entities.initiative_budget import InitiativeBudget
from domain.entities.theme import Theme


class Initiative:
    """
    Represents an initiative, which is a high-level grouping of related themes.

    Attributes:
        id (str): The unique identifier of the initiative.
        title (str): The title of the initiative.
        description (str): The description of the initiative.
        status (str): The status of the initiative. Can be one of "To Do", "In Progress", or "Done".
        budget (float): Budget allocated for the initiative.
        cost (float): Cost incurred so far for the initiative.
        remaining_budget (float): Remaining budget for the initiative.
        initiative_score (int): A score representing the priority or impact of the initiative.
        opportunity_amount (float): The potential opportunity or value the initiative can bring.
        goals (List[str]): Linked goals that the initiative aims to achieve.
        time_frame (str): Time frame for the initiative (e.g., "2023 2H").
        date_range (str): Specific start and end dates for the initiative.
        initial_estimate (str): Initial effort estimate for the initiative.
        actual_effort (str): Actual effort spent on the initiative.
        progress (float): Progress percentage of the initiative.
        themes (List[Theme]): List of themes associated with the initiative.
    """

    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        status: str,
        initiative_budget: InitiativeBudget,
        initiative_score: int,
        opportunity_amount: float,
        goals: List[str],
        time_frame: str,
        date_range: str,
        initial_estimate: str,
        actual_effort: str,
        progress: float,
    ):
        """
        Initializes a new instance of the Initiative class.

        Args:
            id (str): The unique identifier of the initiative.
            title (str): The title of the initiative.
            description (str): The description of the initiative.
            status (str): The status of the initiative. Can be one of "To Do", "In Progress", or "Done".
            budget (float): Budget allocated for the initiative.
            cost (float): Cost incurred so far for the initiative.
            remaining_budget (float): Remaining budget for the initiative.
            initiative_score (int): A score representing the priority or impact of the initiative.
            opportunity_amount (float): The potential opportunity or value the initiative can bring.
            goals (List[str]): Linked goals that the initiative aims to achieve.
            time_frame (str): Time frame for the initiative (e.g., "2023 2H").
            date_range (str): Specific start and end dates for the initiative.
            initial_estimate (str): Initial effort estimate for the initiative.
            actual_effort (str): Actual effort spent on the initiative.
            progress (float): Progress percentage of the initiative.
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.initiative_budget = initiative_budget
        self.initiative_score = initiative_score
        self.opportunity_amount = opportunity_amount
        self.goals = goals
        self.time_frame = time_frame
        self.date_range = date_range
        self.initial_estimate = initial_estimate
        self.actual_effort = actual_effort
        self.progress = progress
        self.themes: List[Theme] = []

    def add_theme(self, theme: Theme):
        """
        Adds a theme to the initiative.

        Args:
            theme (Theme): The theme to be added.
        """
        self.themes.append(theme)
        print(f"Domain Event: Theme '{theme.title}' added to Initiative '{self.title}'")

    def add_epic(self, theme_id: str, epic: Epic):
        """
        Adds an epic to the initiative.

        Args:
            theme_id (str): The unique identifier of the theme.
            epic (Epic): The epic to be added.
        """
        # Add epic to theme found ensuring the theme exists and is associated with the initiative.
        for theme in self.themes:
            if theme.id == theme_id:
                theme.add_epic(epic)
                print(
                    f"Domain Event: Epic '{epic.title}' added to Initiative '{self.title}'"
                )
                break
            else:
                # TODO: Replace with less generic exception.
                raise Exception(f"Theme '{theme_id}' not found.")
