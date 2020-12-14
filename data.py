import pandas as pd

cities_data="Resources/cities.csv"

cities_df = pd.read_csv(cities_data, encoding="UTF-8")

cities_df.to_html("Resources/cities_data.html", index=False)
