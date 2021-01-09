import pandas as pd

recipes = pd.read_csv("recipes.csv", encoding="US_ASCII")

recipes.drop("id", axis=1)

recipes["id"] = [i for i in range(1, len(recipes) + 1)]

import joblib
joblib.dump(recipes, "recipes.pkl")

recipes = joblib.load("recipes.pkl")