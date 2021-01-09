import joblib

recipes = joblib.load("recipes.pkl")

dataset_size = len(recipes)

import random
import numpy as np
import pandas as pd

class Queries:
    def __init__(self, query_type=int, sort_by=1, support_info=list, *filters):
        # query_type - Int >= 0
        # sort_by - {0: 'id', 1: 'rating', 2: 'total_time_in_second', 3: # of ingredients}
        # support_info - List
        self.query_type = query_type
        self.sort_by = sort_by
        self.info = support_info
        self.filters = filters

    def apply(self):
        result = None

        if self.query_type == 0: # recipeName
            result = self.query_based_on_recipe_name_or_ingredients(self.info)

        elif self.query_type == 1: # course
            result = self.query_based_on_course(self.info)

        elif self.query_type == 2: # ingredients
            result = self.query_based_on_recipe_name_or_ingredients(self.info)

        else: # recommended dishes
            random.seed(42)
            show_size = 20
            show = []
            result =

        pass # call sort_by decorator
        for flt in self.filters:
            pass # call each filter decorators

        return result

    def rating_filter(self, threshold): # return result of rating > threshold
        pass

    def cuisine_filter(self, cuisine):
        pass

    def query_based_on_recipe_name_or_ingredients (self, food_name):
        pass

    def query_based_on_course (self, course):
        pass

recipeName            5475 non-null object
rating                5474 non-null float64
totalTimeInSeconds    5240 non-null float64
course                4983 non-null object
cuisine               5474 non-null object
ingredients