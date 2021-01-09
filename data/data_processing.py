import pandas as pd

recipes = pd.read_csv("recipes.csv", encoding="US_ASCII")

recipes.drop("id", axis=1)

recipes["id"] = [i for i in range(1, len(recipes) + 1)]

def split_strings(strin):
    s = str(strin).replace("[", "")
    s = s.replace("]", "")
    return s.split(",")

recipes["ingredients"] = recipes["ingredients"].apply(split_strings)

import joblib
joblib.dump(recipes, "recipes.pkl")

recipes = joblib.load("recipes.pkl")




