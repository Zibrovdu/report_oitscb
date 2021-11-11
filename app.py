import dash

from otchet_oitscb.callbacks import register_callbacks
from otchet_oitscb.layouts import serve_layout

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                title='Еженедельный отчет ОИТСЦБ')
server = app.server

app.layout = serve_layout
register_callbacks(app)

if __name__ == '__main__':
    app.run_server()
