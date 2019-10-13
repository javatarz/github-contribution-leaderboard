from client.models.user_stats import UserStats
from client_test.models.pr_test_data import PRData
from client.models.pull_request import PullRequest


def test_leaderboard():
    expected = "User: Apple - Score: 13 (PRs: 2)"

    assert user_stats().leaderboard_data() == expected


def test_prs():
    expected = """User: Apple - Score: 13
  URL: some-url | Score: 3
  URL: some-url | Score: 10
"""

    assert user_stats().prs_data() == expected


def test_all():
    stats = user_stats()

    assert stats.all_data() == stats.prs_data()


def user_stats() -> UserStats:
    pr_data = PRData().with_defaults()
    pr1 = PullRequest(**pr_data.with_state('closed').data)
    pr2 = PullRequest(**pr_data.with_merged(True).data)
    prs = [pr1, pr2]
    score = sum(pr.score() for pr in prs)
    return UserStats("Apple", prs, score)
