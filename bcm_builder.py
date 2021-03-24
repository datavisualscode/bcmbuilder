import plotly.graph_objects as go
import pandas as pd

#create a dataframe from the Business Capability Model as defined using the BCM format
df = pd.read_csv('bcmL1L2L3.csv')

print(df)

#build a visual treemap of the business capability model
fig = go.Figure(go.Treemap(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        marker_colorscale = 'Blues'))
        #marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue"]))
fig.write_html("bcm.html")
#fig.show()

# Create a bcm from json
# df = pd.read_json('data/json/bcmL1L2.json')
# # View the first ten rows
# # print(df.info())
# # print(df)
# # fig = px.treemap(df, path=["Level 0 Capability"])
# fig = px.treemap(df, path=["Level 0 Capability","Level 1 Capability", "Level 2 Capability"], title='Business Capability Model', )
# # fig = px.treemap(df, path=["Level 0 Capability","Level 1 Capability"],values='Level 0 Definition','Level 1 Definition')
# fig.show()