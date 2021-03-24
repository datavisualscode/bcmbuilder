import pandas as pd
import plotly.express as px

#create a dataframe from the Business Capability Model as defined.
df = pd.read_json('data/bcmL1L2.json')
print(df)

# Create a bcm from json
print(df.info())
print(df)

fig = px.treemap(df, path=["Level 0 Capability","Level 1 Capability"])

fig.show()