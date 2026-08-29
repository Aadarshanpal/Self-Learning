import pandas as pd

data = pd.read_csv("Pandas/data.csv")

Bulky_pokemons = data[data["HP"] > 80]

print(Bulky_pokemons)

# In pandas and is & or is | and not is !