import pandas as pd
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
data = reviews.groupby(["country"]).points.mean()
data.to_csv("reviews-by-country.csv")

