from flask import Blueprint

mod = Blueprint('api',__name__)
@mod.route('/data')
def data():
    return '<h1> here is the data section of your app <h1>'