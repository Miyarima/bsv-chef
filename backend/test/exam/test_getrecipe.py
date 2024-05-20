import pytest
import unittest.mock as mock

from src.controllers.recipecontroller import RecipeController

@pytest.mark.exam
def test_personal_diet():
    mocked_recipeController = mock.MagicMock()
    mocked_recipeController.get_readiness_of_recipes.return_value = {"vegan": "carbonara"}
    sut = RecipeController(mocked_recipeController)

    diet = "vegan"
    take_best = False

    result = sut.get_recipe(diet, take_best)
    assert result == "vegan"

@pytest.mark.exam
def test_recipe_readiness_zero():
    mocked_recipeController = mock.MagicMock()
    mocked_recipeController.get_readiness_of_recipes.return_value = {}
    sut = RecipeController(mocked_recipeController)

    diet = "none"
    take_best = False

    result = sut.get_recipe(diet, take_best)
    assert result == None

@pytest.mark.exam
def test_take_best_true():
    mocked_recipeController = mock.MagicMock()
    mocked_recipeController.get_readiness_of_recipes.return_value = {"vegeterian": "carbonara", "vegeterian": "meatballs", "vegeterian": "pasta"}
    sut = RecipeController(mocked_recipeController)

    diet = "vegeterian"
    take_best = True

    result = sut.get_recipe(diet, take_best)
    assert result == None