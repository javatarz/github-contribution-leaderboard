from typing import List
from datetime import datetime


class PullRequest:
    def __init__(self, *args, **kwargs):
        self._url = kwargs['issues_data']['pull_request']['html_url']
        self._state = kwargs['issues_data']['state']
        self._labels = PullRequest._label_names(
            kwargs['issues_data']['labels'])
        self._created_at = PullRequest._parse_date(
            kwargs['issues_data']['created_at'])
        self._merged = kwargs['pr_data']['merged']

    def is_spam(self):
        'invalid' in self._labels or 'spam' in self._labels

    def score(self) -> int:
        return 1

    def created_between(self, start_date: datetime, end_date: datetime) -> bool:
        return start_date <= self._created_at <= end_date

    def summary(self) -> str:
        return f"URL: {self._url} | Score: {self.score()}"

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')

    @staticmethod
    def _label_names(labels: List[dict]) -> List[str]:
        return [label['name'] for label in labels]
