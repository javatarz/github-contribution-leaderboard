from client.models.user_stats import UserStats
from client_test.models.pr_test_data import PRData


def test_leaderboard():
    expected = "User: Apple - Score: 13 (PRs: 2)"

    assert user_stats().leaderboard_data() == expected


def test_prs():
    expected = """User: Apple - Score: 13 (PRs: 2)
  URL: some-url | Score: 3
  URL: some-url | Score: 10
"""

    assert user_stats().prs_data() == expected


def test_all():
    expected = """User: Apple - Score: 13 (PRs: 2)
  URL: some-url | Score: 3 | Created at: 2010-12-24 16:34:47
  URL: some-url | Score: 10 | Created at: 2020-11-25 18:35:50
"""

    assert user_stats().all_data() == expected


def user_stats():
    pull_request_1 = PRData().with_defaults().with_created_at(
        '2010-12-24T16:34:47Z').with_state('closed').as_pull_request()

    pull_request_2 = PRData().with_defaults().with_created_at(
        '2020-11-25T18:35:50Z').with_merged(True).as_pull_request()

    pull_requests = [pull_request_1, pull_request_2]
    score = sum(pr.score() for pr in pull_requests)

    return UserStats("Apple", pull_requests, score)
