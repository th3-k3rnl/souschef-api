from pydantic import BaseModel
from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    description: str = None
    # Reference ID of picture in the database
    # TODO: Require a method to get the picture by reference
    picture: str


@dataclass
class Meal:
    id: str
    name: str
    ingredients: list[Ingredient]
    instructions: dict[int, str]
    estimatedCookTime: int  # minutes
    picture: None  # TODO: how to store multimedia data?


class Menu(BaseModel):
    """
    Provide a static list of meal objects to the frontend for tabulation.

    Meals can be created, imported, updated and deleted.

    Args:
        BaseModel (_type_): _description_
    """

    meals: list[Meal]

    def create_meal(): ...
    def import_meal(): ...
    def update_meal(): ...
    def delete_meal(): ...
