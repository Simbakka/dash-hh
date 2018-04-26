import plotly.graph_objs as go
from ..models import HhRequest, Result


# Получение данных для графика
def get_graph_data(graph):
    graph_data = []
    source_data = Result.query.join(HhRequest).with_entities(
        Result.published, Result.count, HhRequest.sentence).filter_by(graph=graph)

    sought_values = HhRequest.query.with_entities(HhRequest.sentence).filter_by(
        graph=graph).distinct(HhRequest.sentence).order_by(HhRequest.sentence)

    for obj in sought_values:
        obj_query = source_data.filter_by(sentence=obj.sentence)
        dates = [i[0] for i in obj_query.with_entities(Result.published).all()]
        values = [i[0] for i in obj_query.with_entities(Result.count).all()]
        plot = go.Scatter(x=dates, y=values, name=obj.sentence, mode='lines+markers')
        graph_data.append(plot)

    return graph_data
