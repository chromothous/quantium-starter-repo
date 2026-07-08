import pandas as pd

from dash import Dash, dcc, html
import plotly.express as px

# Load the cleaned data
df = pd.read_csv(r"C:\Users\Chromothous\Desktop\Job Sims\Quantium\quantium-dash\quantium-starter-repo\formatted_data\formatted_sales_data.csv")

# Convert dates
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Group sales by date
daily_sales = (
    df.groupby("Date")["Sales"]
    .sum()
    .reset_index()
)

app = Dash(__name__)

fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time"
)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Dashboard"),

    dcc.Graph(
        figure=fig
    )
])

if __name__ == "__main__":
    app.run(debug=True)