# from dash import Dash, html
# 
# app = Dash(__name__)
# 
# app.layout = html.Div([
#     html.Div(children='Hello World')
# ])
# 
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # Import packages
# from dash import Dash, html, dash_table
# import pandas as pd
# 
# # Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# 
# # Initialize the app
# app = Dash(__name__)
# 
# # App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10)
# ])
# 
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # Import packages
# from dash import Dash, html, dash_table, dcc
# import pandas as pd
# import plotly.express as px
# 
# # Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# 
# # Initialize the app
# app = Dash(__name__)
# 
# # App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data and a Graph'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10),
#     dcc.Graph(figure=px.histogram(df, x='continent', y='lifeExp', histfunc='avg'))
# ])
# 
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # Import packages
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px
# 
# # Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# 
# # Initialize the app
# app = Dash(__name__)
# 
# # App layout
# app.layout = html.Div([
#     html.Div(children='My First App with Data, Graph, and Controls'),
#     html.Hr(),
#     dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=6),
#     dcc.Graph(figure={}, id='controls-and-graph')
# ])
# 
# # Add controls to build the interaction
# @callback(
#     Output(component_id='controls-and-graph', component_property='figure'),
#     Input(component_id='controls-and-radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#     return fig
# 
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # Import packages
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px
# 
# # Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# 
# # Initialize the app - incorporate css
# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# app = Dash(__name__, external_stylesheets=external_stylesheets)
# 
# # App layout
# app.layout = html.Div([
#     html.Div(className='row', children='My First App with Data, Graph, and Controls',
#              style={'textAlign': 'center', 'color': 'blue', 'fontSize': 30}),
# 
#     html.Div(className='row', children=[
#         dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
#                        value='lifeExp',
#                        inline=True,
#                        id='my-radio-buttons-final')
#     ]),
# 
#     html.Div(className='row', children=[
#         html.Div(className='six columns', children=[
#             dash_table.DataTable(data=df.to_dict('records'), page_size=11, style_table={'overflowX': 'auto'})
#         ]),
#         html.Div(className='six columns', children=[
#             dcc.Graph(figure={}, id='histo-chart-final')
#         ])
#     ])
# ])
# 
# # Add controls to build the interaction
# @callback(
#     Output(component_id='histo-chart-final', component_property='figure'),
#     Input(component_id='my-radio-buttons-final', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#     return fig
# 
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)

# # # Import packages
# # from dash import Dash, html, dash_table, dcc, callback, Output, Input
# # import pandas as pd
# # import plotly.express as px
# # import dash_design_kit as ddk
# # 
# # # Incorporate data
# # df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# # 
# # # Initialize the app
# # app = Dash(__name__)
# # 
# # # App layout
# # app.layout = ddk.App([
# #     ddk.Header(ddk.Title('My First App with Data, Graph, and Controls')),
# #     dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'],
# #                     value='lifeExp',
# #                     inline=True,
# #                     id='my-ddk-radio-items-final'),
# #     ddk.Row([
# #         ddk.Card([
# #             dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
# #         ], width=50),
# #         ddk.Card([
# #             ddk.Graph(figure={}, id='graph-placeholder-ddk-final')
# #         ], width=50),
# #     ]),
# # 
# # ])
# # 
# # # Add controls to build the interaction
# # @callback(
# #     Output(component_id='graph-placeholder-ddk-final', component_property='figure'),
# #     Input(component_id='my-ddk-radio-items-final', component_property='value')
# # )
# # def update_graph(col_chosen):
# #     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
# #     return fig
# # 
# # # Run the app
# # if __name__ == '__main__':
# #     app.run_server(debug=True)

# # Import packages
# from dash import Dash, html, dash_table, dcc, callback, Output, Input
# import pandas as pd
# import plotly.express as px
# import dash_bootstrap_components as dbc
# 
# # Incorporate data
# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')
# 
# # Initialize the app - incorporate a Dash Bootstrap theme
# external_stylesheets = [dbc.themes.CERULEAN]
# app = Dash(__name__, external_stylesheets=external_stylesheets)
# 
# # App layout
# app.layout = dbc.Container([
#     dbc.Row([
#         html.Div('My First App with Data, Graph, and Controls', className="text-primary text-center fs-3")
#     ]),
# 
#     dbc.Row([
#         dbc.RadioItems(options=[{"label": x, "value": x} for x in ['pop', 'lifeExp', 'gdpPercap']],
#                        value='lifeExp',
#                        inline=True,
#                        id='radio-buttons-final')
#     ]),
# 
#     dbc.Row([
#         dbc.Col([
#             dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
#         ], width=6),
# 
#         dbc.Col([
#             dcc.Graph(figure={}, id='my-first-graph-final')
#         ], width=6),
#     ]),
# 
# ], fluid=True)
# 
# # Add controls to build the interaction
# @callback(
#     Output(component_id='my-first-graph-final', component_property='figure'),
#     Input(component_id='radio-buttons-final', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#     return fig
# 
# # Run the app
# if __name__ == '__main__':
#     app.run_server(debug=True)

# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

# Incorporate data
df = pd.read_csv('https://www.hpa.gov.tw/File/Attach/12497/File_17848.csv', encoding='cp950')

# Initialize the app - incorporate a Dash Mantine theme
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dmc.Container([
    dmc.Title('癌症發生統計', color="blue", size="h3"),
    dmc.RadioGroup(
            [dmc.Radio(i, value=i) for i in  ['性別', '縣市別', '癌症別']],
            id='my-dmc-radio-item',
            value='lifeExp',
            size="sm"
        ),
    dmc.Grid([
        dmc.Col([
            dash_table.DataTable(data=df.to_dict('records'), page_size=12, style_table={'overflowX': 'auto'})
        ], span=6),
        dmc.Col([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
    ]),

], fluid=True)

# Add controls to build the interaction
@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='my-dmc-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='粗率 (每10萬人口)', y=col_chosen, histfunc='avg')
    return fig

# Run the App
if __name__ == '__main__':
    app.run_server(debug=True)
