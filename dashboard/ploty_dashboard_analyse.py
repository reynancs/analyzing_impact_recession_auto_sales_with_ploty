import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import requests
import io


#URL of the CSV file
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"

# Read the CSV data into a pandas dataframe
df = pd.read_csv(url, encoding = "ISO-8859-1")

# Rename Collumns 
df.columns = df.columns.str.lower()


# Create a dash application layout
app = dash.Dash(__name__)

# Set the title of the dashboard
app.layout = html.Div(
    style={'fontFamily': 'Segoe UI, sans-serif', 'backgroundColor': '#FFFFFF', 'padding': '20px'}, 
    children=[
        html.H1(
        "Automobile Sales Statistics Dashboard",
        style={'textAlign': 'left', 'color': '#004B87', 'font-size': '30px'}
    ),

    html.Div([
        html.Div([
            html.Label("Select Statistics:", style={'fontWeight': 'bold', 'color': '#333333'}),
            dcc.Dropdown(
                id='dropdown-statistics',
                options=[
                    {'label': 'Yearly Statistics', 'value': 'Yearly Statistics'},
                    {'label': 'Recession Period Statistics', 'value': 'Recession Period Statistics'}
                ],
                value='Yearly Statistics',
                placeholder='Select a report type',
                style={'width': '250px', 'font-size': '14px'}
            )
        ], style={'margin-right': '20px'}),

        html.Div([
            html.Label("Select Year:", style={'fontWeight': 'bold', 'color': '#333333'}),
            dcc.Dropdown(
                id='select-year',
                options=[{'label': i, 'value': i} for i in range(1980, 2024)],
                placeholder='Select a year',
                style={'width': '180px', 'font-size': '14px'}
            )
        ])
    ], style={'display': 'flex', 'align-items': 'center', 'margin-bottom': '20px'}),


    html.Div([
        html.Div(id='output-container', className='chart-grid', style={'display': 'flex'}),
        html.Div(id='output-container2', className='chart-grid', style={'display': 'flex'})
    ])
])



# Define callback to update the input container based on the selected statistics
# Callback Input Definition
@app.callback(
    Output(component_id='select-year', component_property='disabled'),
    Input(component_id='dropdown-statistics', component_property='value')
)

# Callback Input Function
def update_input_container(selected_statistics):
    if selected_statistics == 'Yearly Statistics':
        return False
    else:
        return True
    

# Define callback to update the output container based on the selected statistics and year
# Callback Output Definition
@app.callback(
    [Output(component_id='output-container', component_property='children'), Output(component_id='output-container2', component_property='children')],
    [Input(component_id='dropdown-statistics', component_property='value'), Input(component_id='select-year', component_property='value')]
)
# Callback Output function
def update_output_container(selected_statistics, input_year):

    if selected_statistics == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = df[df['recession'] == 1]
        
        # Plot 1: Automobile sales fluctuate over Recession Period (year wise) using line chart
        # Groupping data for plotting
        yearly_rec_autos = recession_data.groupby('year')['automobile_sales'].mean().reset_index()
        # Plotting the line graph
        R_chart1 = dcc.Graph(
            figure=px.line(yearly_rec_autos, 
                           x='year',
                           y='automobile_sales',
                           title="Average Automobile Sales fluctuation over Recession Period"))

        # Plot 2: Calculate the average number of vehicles sold by vehicle type and represent as a Bar chart
        average_sales = recession_data.groupby('vehicle_type')['automobile_sales'].mean().reset_index()
        R_chart2 = dcc.Graph(
            figure=px.bar(average_sales, 
                          x='vehicle_type',
                          y='automobile_sales',
                          title='Average Vehicles Sold by Vehicle Type'))

        # Plot 3: Pie chart for total expenditure share by vehicle type during recessions
        exp_rec = recession_data.groupby('vehicle_type')['advertising_expenditure'].sum().reset_index()
        R_chart3 = dcc.Graph(
            figure=px.pie(exp_rec,
                          values='advertising_expenditure',
                          names='vehicle_type',
                          title='Total Advertising Expenditure Share by Vehicle Type'))
        
        # Plot 4: Bar chart for the effect of unemployment rate on vehicle type and sales
        unemployment_data = recession_data.groupby(['vehicle_type', 'unemployment_rate'])['automobile_sales'].mean().reset_index()
        R_chart4 = dcc.Graph(
            figure=px.bar(unemployment_data,
                          x='unemployment_rate',
                          y='automobile_sales',
                          color='vehicle_type',
                          labels={'unemployment_rate': 'Unemployment Rate', 'automobile_sales': 'Average Automobile Sales'},
                          title='Effect of Unemployment Rate on Vehicle Type and Sales'))

        return [
            html.Div(className='chart-item', children=[html.Div(children=R_chart1), html.Div(children=R_chart2)], style={'display': 'flex'} ),
            html.Div(className='chart-item', children=[html.Div(children=R_chart3), html.Div(children=R_chart4)], style={'display': 'flex'} )
        ]
    
    elif (input_year and selected_statistics == 'Yearly Statistics'):
        yearly_data = df[df['year'] == input_year]

        # Plot 1: Yearly Automobile Sales using line chart for the whole period
        yas = df.groupby('year')['automobile_sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(
            figure=px.line(yas, 
                           x='year',
                           y='automobile_sales',
                           title="Yearly Automobile Sales"))
            
        # Plot 2: Total Monthly Automobile Sales using line chart for the whole period
        mas = yearly_data.groupby('month')['automobile_sales'].sum().reset_index()
        Y_chart2 = dcc.Graph(
            figure=px.line(mas, 
                           x='month',
                           y='automobile_sales',
                           title="Total Monthly Automobile Sales"))

        # Plot 3: Bar chart for average number of vehicles sold during the given year
        avr_vdata = yearly_data.groupby('vehicle_type')['automobile_sales'].mean().reset_index()
        Y_chart3 = dcc.Graph(
            figure=px.bar(avr_vdata, 
                          x='vehicle_type',
                          y='automobile_sales',
                          title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

        # Plot 4: Total Advertisement Expenditure for each vehicle using pie chart
        exp_data = yearly_data.groupby('vehicle_type')['advertising_expenditure'].sum().reset_index()
        Y_chart4 = dcc.Graph(
            figure=px.pie(exp_data,
                          values='advertising_expenditure',
                          names='vehicle_type',
                          title='Total Advertisement Expenditure for each Vehicle'))

        return [
            html.Div(className='chart-item', children=[html.Div(children=Y_chart1), html.Div(children=Y_chart2)], style={'display':'flex'}),
            html.Div(className='chart-item', children=[html.Div(children=Y_chart3), html.Div(children=Y_chart4)], style={'display':'flex'})
        ]
    else:
        return None



# Run the app
if __name__ == '__main__':
    app.run()