import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from .model import get_graph_data
from flaskapp import cnf, footer


COLORS = {'background': '#3D6AA4', 'text': '#FFFFFF'}

ALL_STYLE = {'backgroundColor': COLORS['background'], 'color': COLORS['text'], 'font-family': 'Helvetica'}
TEXT_STYLE = {'textAlign': 'center', 'margin-top': '10px', 'margin-bottom': '10px'}
COPY_STYLE = {'textAlign': 'center', 'padding-top': '5px', 'padding-bottom': '5px'}
HEAD_STYLE = {'padding-top': '3px'}
IMG_STYLE = {'height': '40px', 'float': 'left', 'margin-top': '15px', 'margin-left': '10px'}


hhImg = html.Img(
    src="https://hhru.github.io/api/logos/min-hh-red.png",
    style=IMG_STYLE
)


titleDiv = html.Div(
    style=HEAD_STYLE,
    children=[
        html.A(hhImg, href='https://hh.ru/search/vacancy/advanced'),
        html.H2(children=cnf.head, style=TEXT_STYLE),
        html.Div(children=cnf.description, style=TEXT_STYLE)
    ]
)

# Вспомогательная функция - получение отдельного графика
def get_figure(graph):
    data = get_graph_data(graph)

    figure = go.Figure(
        data=data,
        layout=go.Layout(
            title=cnf.titles[graph],
            showlegend=True
        )
    )

    if graph > 1:
        figure.layout.height = cnf.largeGraphHeight

    return figure


def get_layout():
    """
    Основная функция - получение страницы Dash
    """
    layout = html.Div(
        style=ALL_STYLE,
        children=[
            titleDiv,
            dcc.Graph(id='graph-1', figure=get_figure(1)),
            dcc.Graph(id='graph-3', figure=get_figure(3)),
            dcc.Graph(id='graph-2', figure=get_figure(2)),
            html.Div(children=footer, style=COPY_STYLE)
        ]
    )

    return layout
