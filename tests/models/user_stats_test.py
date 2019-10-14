from datetime import datetime
from ghcl.models.user_stats import UserStats
from tests.models.pr_test_data import PRData


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


def test_to_dict():
    expected = {
        "user_name": "Apple",
        "prs": [
            {
                "url": "some-url",
                "score": 3,
                "created_at": datetime(2010, 12, 24, 16, 34, 47)
            },
            {
                "url": "some-url",
                "score": 10,
                "created_at": datetime(2020, 11, 25, 18, 35, 50)
            }
        ],
        'avatar': 'https://avatars1.githubusercontent.com/u/5?v=4',
        "score": 13
    }
    assert user_stats().to_dict() == expected


def user_stats():
    pull_request_1 = PRData().with_defaults().with_created_at(
        '2010-12-24T16:34:47Z').with_state('closed').as_pull_request()

    pull_request_2 = PRData().with_defaults().with_created_at(
        '2020-11-25T18:35:50Z').with_merged(True).as_pull_request()

    prs = [pull_request_1, pull_request_2]
    score = sum(pr.score() for pr in prs)

    return UserStats(user_id=5, user_name="Apple", prs=prs, score=score)
