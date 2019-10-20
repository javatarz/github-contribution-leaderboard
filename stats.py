
from utils.args import parse_args
from ghcl.contributions import Contributions
from ghcl.github_stats import GithubStats

args = parse_args()
contribs = Contributions(
    stats_client=GithubStats(access_token=args['access_token']),
    http_pool_size=args['http_pool_size']
)
stats = contribs.leaderboard(
    args['users'], args['start_date'], args['end_date'])

print("===========================")
print("Leaderboard")
print("===========================")
for stat in stats:
    print(getattr(stat, f"{args['mode']}_data")())
print("===========================")

if args['with_summary']:
    print()
    print("===========================")
    print("Summary")
    print("===========================")
    print(f"Users:")
    user_count = len(args['users'])
    print(f"  count: {user_count}")
    print("PRs overall:")
    in_period_pr_count = sum([stat.pr_count() for stat in stats])
    print(f"  during period: {in_period_pr_count}")
    total_pr_count = sum([stat.total_count for stat in stats])
    print(f"  overall: {total_pr_count}")
    print("===========================")
