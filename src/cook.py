from pydantic import BaseModel
from food import Meal

"""
When an instance of this class is instantiated, the cooking timer
starts in the frontend. This class will be instantiated when cooking
commences.
"""


class Status(BaseModel):
    # Meal contains the estimated cooking time
    meal: Meal
    numSteps: int
    actualCookTime: int

    # Time taken is stored in the database table when the finished
    # button is pressed in the frontend
    timeTaken: int = 0  # handled by the frontend in seconds

    def __init__(self, meal_id: str):
        self.meal = self.get_meal(meal_id)
        self.actualCookTime = self.meal.estimatedCookTime
        self.numSteps = len(self.meal.instructions)

    def get_meal(self, meal_id: str) -> Meal:
        """
        Get a meal object from the database.
        We want to reference the meal in cooking mode,
        to access the recipe and instructions
        """
        return Meal()

    def add_time_buffer(self, added_mins: int):
        """
        Sometimes a meal might take longer than expected.
        The Chef and Sous Chef might agree that they require
        more time to get the meal right.
        """
        self.actualCookTime += added_mins

    def update_cook_time():
        """
        Provide the option to update the estimated cooking time for this meal
        to the time it actually took to cook the meal.
        """
