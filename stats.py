
from typing import List

from ghcl.contributions import Contributions
from ghcl.github_stats import GithubStats
from ghcl.models.user_experience import UserPRExperience, ExperienceSummary
from ghcl.models.user_stats import UserStats
from utils.args import parse_args


def _stats_with_exp(e: UserPRExperience) -> (UserPRExperience, List[int]):
    return (e, [stat.pr_count() for stat in stats])


def _stats_to_prs(t: (UserPRExperience, List[int])) -> (UserPRExperience, int):
    return (t[0], sum(t[1]))


def _experience_data(stats: List[UserStats]) -> str:
    experiences = [stat.user_past_pr_experience() for stat in stats]

    def _to_summary_experience(t: (UserPRExperience, int)) -> str:
        return ExperienceSummary(
            user_experience=t[0],
            people_count=experiences.count(t[0]),
            pr_count=t[1]
        ).summary()

    past_summaries = map(
        _to_summary_experience,
        map(
            _stats_to_prs,
            map(_stats_with_exp, experiences)
        )
    )

    return '\n'.join(past_summaries)


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
    print("User experience:")
    print(_experience_data(stats))
    print("===========================")
