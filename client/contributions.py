from datetime import datetime
from typing import List

from client.models.pull_request import PullRequest
from client.models.user_stats import UserStats


class Contributions:
    def __init__(self, stats_client):
        self._client = stats_client

    def leaderboard(self, user_ids: List[str], start_date: datetime = None,
                    end_date: datetime = None) -> List[UserStats]:

        stats = [self._user_score(user_id, start_date, end_date)
                 for user_id in user_ids]
        return sorted(stats, key=lambda stat: stat._score, reverse=True)

    def _user_score(self, user_id: str, start_date: datetime = None,
                    end_date: datetime = None) -> UserStats:
        prs = self._client.list_of_prs(user_id)
        filtered_prs = Contributions._filter_prs(prs, start_date, end_date)
        return UserStats(
            user_id=user_id,
            prs=filtered_prs,
            score=Contributions._score(filtered_prs)
        )

    @staticmethod
    def _filter_prs(prs: List[PullRequest], start_date: datetime = None,
                    end_date: datetime = None) -> List[PullRequest]:
        if start_date is not None and end_date is not None:
            return [p for p in prs if p.created_between(start_date, end_date)]
        else:
            return prs

    @staticmethod
    def _score(prs: List[PullRequest]) -> int:
        return sum(map(lambda pr: pr.score(), prs))
