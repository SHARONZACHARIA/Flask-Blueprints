from flask import Flask

app = Flask(__name__)

from example.api.routes import mod
from example.site.routes import mod

# register blueprints for api and site

app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod,url_prefix='/api')