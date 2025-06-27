import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import folium
from folium.plugins import HeatMap
import dash_leaflet as dl

# Load your dataset
df = pd.read_csv("updatedfile.csv", nrows=50000)

# Process data
df['INCIDENT_DATE'] = pd.to_datetime(df['INCIDENT_DATE'])
df['hour'] = df['INCIDENT_DATE'].dt.hour  # Ensure 'hour' column exists
hourly_calls = df.groupby('hour').size().reset_index(name='Count')
weekly_calls = df.groupby('day_of_week').size().reset_index(name='Count')
top_emergency_types = df['TYP_DESC'].value_counts().head(10).reset_index(name='Count')
top_emergency_types.rename(columns={'index': 'TYP_DESC'}, inplace=True)

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("911 Calls Analysis Dashboard", style={'textAlign': 'center'}),

    # Add descriptive text
    html.Div([
        html.P("This dashboard provides insights into 911 call data, including trends by hour, day of the week, and top emergency types."),
        html.P("Use the visualizations below to explore when and where emergencies occur, and the most common types of calls."),
    ], style={'margin': '20px', 'fontSize': '16px', 'textAlign': 'center'}),

    # Hourly Trends
    html.Div([
        html.H2("911 Calls by Hour"),
        dcc.Graph(
        figure=px.bar(hourly_calls, x='hour', y='Count', title="911 Calls by Hour")
        .update_layout(
        xaxis_title="Hour of the Day",
        yaxis_title="Number of Calls",
        margin=dict(l=20, r=20, t=40, b=20),
        height=400
    )
)
    ], style={'marginBottom': '30px'}),

    # Weekly Trends
    html.Div([
        html.H2("911 Calls by Day of the Week"),
        dcc.Graph(
            figure=px.bar(weekly_calls, x='day_of_week', y='Count', title="911 Calls by Day of the Week")
        )
    ]),

    # Dropdown for filtering by day
    html.Div([
        html.H2("Filter by Day of the Week"),
        dcc.Dropdown(
            id='day-filter',
            options=[{'label': day, 'value': day} for day in df['day_of_week'].unique()],
            placeholder="Select a Day of the Week",
            style={'width': '50%'}
        ),
        dcc.Graph(id='filtered-chart'),
    ], style={'textAlign': 'center', 'margin': '20px'}),

    # Top Emergency Types
    html.Div([
        html.H2("Top Emergency Types"),
        dcc.Graph(
    figure=px.bar(top_emergency_types, x='TYP_DESC', y='Count', title="Top Emergency Types")
    .update_layout(
        xaxis_title="Emergency Type",
        yaxis_title="Number of 911 Calls",
        xaxis_tickangle=-45,
        margin=dict(l=20, r=20, t=40, b=80),
        height=400
    )
)
    ]),

    # Geospatial Distribution
    html.Div([
        html.H2("Geospatial Distribution of 911 Calls"),
        html.Div(id='map-container', children=[
            dl.Map([
                dl.TileLayer(),
                dl.LayerGroup(id="heatmap-layer")
            ], style={'height': '500px', 'width': '100%'}, center=(df['Latitude'].mean(), df['Longitude'].mean()), zoom=12)
        ]),
    ])
])


# Callbacks
@app.callback(
    Output('filtered-chart', 'figure'),
    Input('day-filter', 'value')
)
def update_chart(selected_day):
    if selected_day:
        filtered_df = df[df['day_of_week'] == selected_day]
        fig = px.bar(filtered_df['TYP_DESC'].value_counts().reset_index(),
                     x='index', y='TYP_DESC', title=f"Emergency Types on {selected_day}")
        return fig
    return px.bar(top_emergency_types, x='TYP_DESC', y='Count', title="Top Emergency Types")


@app.callback(
    Output("heatmap-layer", "children"),
    Input('day-filter', 'value')
)
def update_heatmap(selected_day):
    if selected_day:
        filtered_df = df[df['day_of_week'] == selected_day]
    else:
        filtered_df = df
    
    # Check if Latitude and Longitude columns exist
    if 'Latitude' not in filtered_df.columns or 'Longitude' not in filtered_df.columns:
        return []
    
    # Remove rows with missing lat/lon values
    filtered_df = filtered_df.dropna(subset=['Latitude', 'Longitude'])

    heat_data = [[row['Latitude'], row['Longitude']] for _, row in filtered_df.iterrows()]
    return [dl.HeatMap(data=heat_data)]

# Run the app
if __name__ == "__main__":
    app.run_server(debug=True)
