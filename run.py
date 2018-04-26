from flaskapp import create_app, scheduler
from flaskapp.hhfetch import fetch_hh
from flaskapp.dashapp.layout import get_layout


def get_hh_data():
    fetch_hh()


app = create_app()

app.server.app_context().push()
get_hh_data()
app.layout = get_layout()

scheduler.init_app(app.server)
scheduler.start()

if __name__ == '__main__':
    app.run_server(use_reloader=False)
