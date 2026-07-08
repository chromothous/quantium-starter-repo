import pandas as pd

from dash import Dash, dcc, html, Input, Output
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
    html.H1(
        "Soul Foods Pink Morsel Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "silver",
            "fontFamily": "Arial",
            "marginBottom": "30px",
            "textShadow": "0px 0px 15px #8A2BE2"
        }
    ),

    html.Div([
        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "East", "value": "east"},
                {"label": "South", "value": "south"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            labelStyle={
                "color": "silver",
                "marginRight": "20px"
            },
        )
    ], style={
        "color": "silver",
        "fontSize": "18px",
        "textAlign": "center",
        "marginBottom": "20px"
    }),

    html.Div([
        dcc.Graph(
            id="sales-chart",
            figure=fig
        )
    ], style={
        "backgroundColor": "#202020",
        "padding": "20px",
        "borderRadius": "15px",
        "boxShadow": "0px 0px 25px rgba(168, 85, 247, 0.5)"
    })

], style={
    "backgroundColor": "#121212",
    "minHeight": "100vh",
    "padding": "30px"
})

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_chart(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["Region"] == selected_region]

    daily_sales = (
        filtered_df.groupby("Date")["Sales"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        daily_sales,
        x="Date",
        y="Sales",
        title="Pink Morsel Sales Over Time"
    )

    fig.update_layout(
        paper_bgcolor="#202020",
        plot_bgcolor="#202020",
        font_color="silver",
        title_font_color="#C084FC",
        xaxis_title="Date",
        yaxis_title="Sales",

        xaxis=dict(
            gridcolor="#444444",
            linecolor="silver"
        ),
        yaxis=dict(
            gridcolor="#444444",
            linecolor="silver"
        )
    )

    fig.update_traces(
        line=dict(
            color="#A855F7",
            width=4
        )
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)