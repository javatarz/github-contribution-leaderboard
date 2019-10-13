class UserStats:
    def __init__(self, user_id, prs, score):
        self._user_id = user_id
        self._prs = prs
        self._score = score

    def leaderboard_data(self) -> str:
        user_part = f"User: {self._user_id}"
        score_part = f"Score: {self._score}"
        prs_part = f"PRs: {len(self._prs)}"
        return f"{user_part} - {score_part} ({prs_part})"

    def prs_data(self) -> str:
        user_part = f"User: {self._user_id}"
        score_part = f"Score: {self._score}"
        new_line = '\n'
        header_line = f"{user_part} - {score_part}{new_line}"

        pr_summaries = [f"  {pr.summary()}" for pr in self._prs]
        pr_summary_data = new_line.join(pr_summaries)

        return f"{header_line}{pr_summary_data}{new_line}"

    def all_data(self) -> str:
        return self.prs_data()
