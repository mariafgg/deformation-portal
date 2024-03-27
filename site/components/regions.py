
import polars as pl

# Read the CSV file using Polars
df = pl.read_csv("assets/regions.csv")

# Initialize an empty dictionary to store the regions data
regions = {}

# Iterate over each row in the DataFrame
for row in df.to_dicts():
    # Use the 'name' column as the key and collect other column values in a list
    key = row["name"]
    values = [row[col] for col in df.columns if col != "name"]
    regions[key] = values


