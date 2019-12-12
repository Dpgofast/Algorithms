#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    max_batch = 0
    limit = None

    for key, value in recipe.items():
        if key not in list(ingredients.keys()):
            return 0
        if key in ingredients:
            take = ingredients[key] // value
        if limit is None:
            max_batch = take
            limit = max_batch
        elif take < limit:
            limit = take
    return max_batch


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print(
        """{batches} batches can be made from the available
         ingredients:{ingredients}.""".format(
            batches=recipe_batches(recipe, ingredients),
            ingredients=ingredients)
            )
