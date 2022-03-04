import flask
import random

app = flask.Flask(__name__)

bp = flask.Blueprint(
    "bp",
    __name__,
    template_folder="./static/react",
)

funfacts = [
    {'fact': 'anime is awesome!'},
    {'fact': 'video games rule!'},
    {'fact': 'food makes me happy!'}
]

@bp.route("/")
def index():
    """  """
    return flask.render_template("index.html")

@bp.route("/facts")
def facts():
    """ sending fact to react """
    Fact = random.choice(funfacts)
    return flask.jsonify(
        Fact
    )

app.register_blueprint(bp)

app.run(debug = True)
