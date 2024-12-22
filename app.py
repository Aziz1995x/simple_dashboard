from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
from data_fetch import fetch_data

# Sample Data
df = fetch_data()

# Create a bar plot
fig = px.bar(df, x="fname", y="job_lvl", title="Job Level of Employees")

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Sample Dashboard", style={"text-align": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True, host="localhost", port=8050)