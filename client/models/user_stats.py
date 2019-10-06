class UserStats:
    def __init__(self, user_id, prs, score):
        self._user_id = user_id
        self._prs = prs
        self._score = score

    def leaderboard_data(self) -> str:
        return f"User: {self._user_id} - Score: {self._score} (PRs: {len(self._prs)})"

    def prs_data(self) -> str:
        pr_summaries = [f"  {pr.summary()}" for pr in self._prs]
        new_line = '\n'
        pr_summary_data = new_line.join(pr_summaries)

        return f"User: {self._user_id} - Score: {self._score}{new_line}{pr_summary_data}{new_line}"

    def all_data(self) -> str:
        return self.prs_data()
