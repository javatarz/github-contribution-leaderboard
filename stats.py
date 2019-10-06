from datetime import datetime
from typing import List
import sys

from client.contributions import Contributions
from client.github_stats import GithubStats
from client.models.user_stats import UserStats

contribs = Contributions(GithubStats(access_token=sys.argv[1]))
stats = contribs.leaderboard(['javatarz', 'anaynayak'])

for stat in stats:
    print(stat.leaderboard_data())
