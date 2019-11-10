import pandas as pd

# Load pickled pandas dataframe
filename = "d30c14b3-4039-3ad8-9cc3-025485863b7c-61939.pickle"
df = pd.read_pickle(filename)

# Count the number of occurences of all different values
# in the "type" column. We only have 2 different values: WiFi and Mobile.
print(df.type.value_counts())
