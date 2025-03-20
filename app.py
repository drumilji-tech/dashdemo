import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import random
from dash.dependencies import Input, Output

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server  # Needed for Azure deployment

# Sample Data
def generate_data():
    df = pd.DataFrame({
        'Category': ['A', 'B', 'C', 'D', 'E'],
        'Value': [random.randint(10, 100) for _ in range(5)]
    })
    return df

# Layout
app.layout = html.Div([
    html.H1("Real-time Data Visualization", style={'textAlign': 'center'}),
    dcc.Graph(id='bar-chart'),
    dcc.Interval(id='interval-component', interval=3000, n_intervals=0)
])

# Callback to update chart
@app.callback(
    Output('bar-chart', 'figure'),
    Input('interval-component', 'n_intervals')
)
def update_chart(n):
    df = generate_data()
    fig = px.bar(df, x='Category', y='Value', title='Live Data Update')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
