import Flask
from functools import wraps
import pandas as pd 


app = Flask(__name__)
df = pd.read_csv("gs://bucket_name/file_name.csv")


def reload_df(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        global df
        df = pd.read_csv("gs://bucket_name/file_name.csv")
        return f(*args, **kwargs)
    return decorated_function


@app.route("/")
@reload_df
def index():
    return "hello world"


@app.route("/not_reloading_df")
def index():
    return "still using previous DF"


@app.route("/forcereload")
@reload_df
def force_reload():
    return "Reloaded DF"