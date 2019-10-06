class UserStats:
    def __init__(self, user_id, prs, score):
        self._user_id = user_id
        self._prs = prs
        self._score = score

    def leaderboard_data(self) -> str:
        return f"{self._user_id} - Score: {self._score} (PRs: {len(self._prs)})"
