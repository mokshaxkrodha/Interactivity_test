import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_auth
from app import app
from apps import shelldashboard,howtouse,notes
import os

server = app.server
server.secret_key = os.environ.get('secret_key', 'secret')
auth = dash_auth.BasicAuth(
    app,
    (('Retailaudit','Distributionkpis',),('gfkinternal','gfkoneposdb',),)
)

app.layout = html.Div([
            dcc.Location(id='url',refresh=True),
            html.Div(id='page-content')
        ])

if myauthenticateduser == 'gfkinternal':
    @app.callback(Output('page-content', 'children'),
                          [Input('url', 'pathname')])
    def display_page(pathname):
        myauthenticateduser = auth._username
        if pathname == '/apps/shelldashboard':
             return shelldashboard.layout
        elif pathname == '/apps/howtouse':
             return howtouse.layout
        elif pathname == '/apps/notes':
             return notes.layout
        else:
            return notes.layout
elif myauthenticateduser == 'Retailaudit':
    @app.callback(Output('page-content', 'children'),
                  [Input('url', 'pathname')])
    def display_page(pathname):
        myauthenticateduser = auth._username
        if pathname == '/apps/shelldashboard':
             return shelldashboard.layout
        elif pathname == '/apps/howtouse':
             return howtouse.layout
        elif pathname == '/apps/notes':
             return notes.layout
        else:
            return shelldashboard.layout

if __name__ == '__main__':
    app.run_server(debug=True)
