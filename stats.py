import sys
from argparse import ArgumentParser
from datetime import datetime
from typing import List

from client.contributions import Contributions
from client.github_stats import GithubStats
from client.models.user_stats import UserStats


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('-at', '--access-token',
                        dest='access_token', required=True, type=str)

    parser.add_argument('-u', '--users', dest='users',
                        nargs='+', required=True, type=str)

    return vars(parser.parse_args())


args = parse_args()
contribs = Contributions(GithubStats(access_token=args['access_token']))
stats = contribs.leaderboard(args['users'])

for stat in stats:
    print(stat.leaderboard_data())
