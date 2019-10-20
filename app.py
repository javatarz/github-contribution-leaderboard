from flask import Flask, jsonify, make_response, send_from_directory

from ghcl.contributions import Contributions
from ghcl.github_stats import GithubStats
from utils.args import valid_date

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config.from_pyfile('secrets.py')


@app.route('/data.json')
def data():
    access_token = app.config['ACCESS_TOKEN']
    users = app.config['USERS']
    start_date = valid_date(app.config['START_DATE'])
    end_date = valid_date(app.config['END_DATE'])
    http_pool_size = app.config['HTTP_POOL_SIZE']

    contribs = Contributions(
        stats_client=GithubStats(access_token=access_token),
        http_pool_size=http_pool_size
    )
    stats = contribs.leaderboard(users, start_date, end_date)
    dicts = [stat.to_dict() for stat in stats]

    return make_response(jsonify(dicts), 200)


@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('web/src', path)
