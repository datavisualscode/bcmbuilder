import plotly.graph_objects as go
import pandas as pd

#create a dataframe from the Business Capability Model as defined.
df = pd.read_csv('data/bcmL1L2L3.csv')
print(df)

#build a visual treemap of the business capability model via CSV
fig = go.Figure(go.Treemap(
        ids = df.ids,
        labels = df.labels,
        parents = df.parents,
        #marker_colorscale = 'Blues'))
        marker_colors = ["pink", "royalblue", "lightgray", "purple", "cyan", "lightgray", "lightblue"]))
#fig.write_html("bcm.html")
fig.show()