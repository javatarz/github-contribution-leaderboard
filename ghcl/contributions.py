from datetime import datetime
from multiprocessing import Pool
from typing import List

from ghcl.github_stats import GithubStats
from ghcl.models.pull_request import PullRequest
from ghcl.models.pull_request_lite import LitePullRequest
from ghcl.models.user_stats import UserStats


class Contributions:
    def __init__(self, stats_client: GithubStats, http_pool_size: int):
        self._client = stats_client
        self._http_pool_size = http_pool_size

    def leaderboard(self, user_names: List[str], start_date: datetime = None,
                    end_date: datetime = None) -> List[UserStats]:

        stats = [self._user_score(user_name, start_date, end_date)
                 for user_name in user_names]
        return sorted(stats, key=lambda stat: stat._score, reverse=True)

    def _user_score(self, user_name: str, start_date: datetime = None,
                    end_date: datetime = None) -> UserStats:
        lite_prs = self._client.list_of_prs(user_name)
        in_window_lite_prs = Contributions._filter_prs(
            lite_prs, start_date, end_date)
        user_id = self._client.user_id_from_name(user_name)

        with Pool(processes=self._http_pool_size) as pool:
            in_window_prs = pool.map(
                self._client.fetch_pr_data, in_window_lite_prs
            )

        return UserStats(
            user_id=user_id,
            user_name=user_name,
            prs=in_window_prs,
            score=Contributions._score(in_window_prs)
        )

    @staticmethod
    def _filter_prs(prs: List[LitePullRequest], start_date: datetime = None,
                    end_date: datetime = None) -> List[LitePullRequest]:
        if start_date is not None and end_date is not None:
            return [p for p in prs if p.created_between(start_date, end_date)]
        else:
            return prs

    @staticmethod
    def _score(prs: List[PullRequest]) -> int:
        return sum(map(lambda pr: pr.score(), prs))
