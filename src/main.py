from fastapi import FastAPI

from database import create_database_connection
from cook import Status
from food import Meal, Menu

app = FastAPI()


@app.post("/api/v1/meal/createMeal/")
def create_meal(meal: Meal) -> int:
    """
    Create a new meal.
    @return The ID of the meal
    """
    conn = create_database_connection()
    return 0


@app.put("/api/v1/meal/updateMeal/{mealId}")
def update_meal(meal: Meal) -> int:
    """
    Update an existing meal.
    """
    return 0


@app.post("/api/v1/meal/deleteMeal/{mealId}")
def delete_meal(meal: Meal) -> None:
    """
    Delete a new meal.
    """
    # TODO: If a meal is deleted and it's in the current menu,
    # the user must be notified before deletion. If they approve,
    # then the meal is also removed from the menu.
    ...


@app.get("/api/v1/meal/importMeal/")
def import_meal(url: str) -> str:
    """

    Args:
        url (str): _description_

    Returns:
        str: _description_
    """
    # TODO: Use something like beautifulsoup to import recipe and
    # instructions from food websites
    ...


@app.get("/api/v1/meal/getMealPlan")
def get_meal_plan(meal_plan_id: str) -> list[Meal]:
    """
    Get the meal plan for the week.
    Scheduling in your meals for the week takes place in the planner.
    For now, the planner will only support planning for the upcoming and current weeks.

    Returns:
        list[Meal]: _description_
    """
    ...


@app.post("/api/v1/menu/createMenu")
def create_menu(menu: Menu) -> int:
    """
    Create a new meal.

    Args:
        mean (Menu): _description_

    Returns:
        int: The ID of the menu in the sous-chef database menus table.
    """
    return 0


@app.put("/api/v1/menu/updateMenu/{menuId}")
def update_menu(menu_id: int, menu: Menu) -> None:
    # TODO: Upsert changes to the menu in the data
    # Return response status to indicate if the update was successful
    ...


@app.put("/api/v1/cook/cookingStatus")
def update_cooking_status(meal_id: str, status: Status) -> Status:
    # TODO: Get menu from database
    # TODO: Server menu as a JSON to the UI
    ...


@app.post("/api/v1/quote/addNewQuote")
def add_new_quote(new_quote: str) -> None:
    """
    Add a new quote to the quotes table in the sous-chef database.
    """
    ...


@app.get("/api/v1/quote/getQuote/{quoteId}")
def quote_of_the_day() -> str:
    """
    Get a random quote of the day from the Quotes MongoDB Document
    """
    ...
