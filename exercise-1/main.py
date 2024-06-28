from flask import Flask, request
from bloudprints.bloueprint import pink_floyd_blueprint



app = Flask(__name__)
app.register_blueprint(pink_floyd_blueprint)



@app.route("/endpoints")
def endpoints():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(str(rule))
    return {"endpoints": routes}