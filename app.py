from flask import Flask, jsonify, make_response, send_from_directory

from ghcl.contributions import Contributions
from ghcl.github_stats import GithubStats
from utils.args import valid_date
import json
import os.path as path

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config.from_pyfile('secrets.py')

@app.route('/data.json')
def data():
    access_token = app.config['ACCESS_TOKEN']
    start_date = valid_date(app.config['START_DATE'])
    end_date = valid_date(app.config['END_DATE'])
    users = load_users()
    contribs = Contributions(GithubStats(access_token=access_token))
    stats = contribs.leaderboard(users, start_date, end_date)
    dicts = [stat.to_dict() for stat in stats]

    return make_response(jsonify(dicts), 200)


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('web/src', path)

def load_users():
    users = []
    user_file_name = app.config['USER_DATA_FILE']
    try:
        users = json.loads(open(user_file_name).read())['users']
    except json.decoder.JSONDecodeError:
        print("cannot parse users")
    except FileNotFoundError:
        print(f"{user_file_name} not present")
    return users
