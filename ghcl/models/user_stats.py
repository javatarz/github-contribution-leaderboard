from typing import List
from ghcl.models.pull_request import PullRequest


class UserStats:
    def __init__(self, user_id: str, user_name: str, prs: List[PullRequest],
                 score: int, total_count: int):
        self._user_id = user_id
        self._user_name = user_name
        self._prs = prs
        self._score = score
        self.total_count = total_count

    def leaderboard_data(self) -> str:
        user_part = f"User: {self._user_name}"
        score_part = f"Score: {self._score}"
        prs_part = f"PRs: {len(self._prs)} | Total PRs: {self.total_count}"
        return f"{user_part} - {score_part} ({prs_part})"

    def prs_data(self, with_date: bool = False) -> str:
        new_line = '\n'
        header_line = self.leaderboard_data()

        pr_summaries = [f"  {pr.summary(with_date)}" for pr in self._prs]
        pr_summary_data = new_line.join(pr_summaries)

        return f"{header_line}{new_line}{pr_summary_data}{new_line}"

    def all_data(self) -> str:
        return self.prs_data(with_date=True)

    def pr_count(self) -> int:
        return len(self._prs)

    def to_dict(self):
        id = self._user_id
        return {
            "avatar": f"https://avatars1.githubusercontent.com/u/{id}?v=4",
            "user_name": self._user_name,
            "prs": [pr.to_dict() for pr in self._prs],
            "score": self._score
        }
