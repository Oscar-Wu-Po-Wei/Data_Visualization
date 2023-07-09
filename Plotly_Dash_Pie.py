from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)


app.layout = html.Div([
    html.H4('癌症發生統計'),
    dcc.Graph(id="graph"),
    html.P("Names:"),
    dcc.Dropdown(id='names',
        options=['性別', '縣市別', '癌症別'],
        value='性別', clearable=False
    ),
    html.P("Values:"),
    dcc.Dropdown(id='values',
        options=['癌症診斷年', '年齡標準化發生率  WHO 2000世界標準人口 (每10萬人口) ', '癌症發生數', '平均年齡', '年齡中位數', '粗率 (每10萬人口)'],
        value='粗率 (每10萬人口)', clearable=False
    ),
])


@app.callback(
    Output("graph", "figure"), 
    Input("names", "value"), 
    Input("values", "value"))

def generate_chart(names, values):
    df = pd.read_csv('https://www.hpa.gov.tw/File/Attach/12497/File_17848.csv', encoding='cp950')
    fig = px.pie(df, values=values, names=names, hole=.3)
    return fig

app.run_server(debug=True)
