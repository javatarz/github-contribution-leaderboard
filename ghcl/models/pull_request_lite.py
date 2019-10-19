from typing import List
from datetime import datetime


class LitePullRequest:
    def __init__(self, *args, **kwargs):
        self._html_url = kwargs['issues_data']['pull_request']['html_url']
        self._state = kwargs['issues_data']['state']
        self._labels = LitePullRequest._label_names(
            kwargs['issues_data']['labels'])
        self._created_at = LitePullRequest._parse_date(
            kwargs['issues_data']['created_at'])
        self.pull_request_url = kwargs['issues_data']['pull_request']['url']

    def created_between(self, start_date: datetime,
                        end_date: datetime) -> bool:
        return start_date <= self._created_at <= end_date

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')

    @staticmethod
    def _label_names(labels: List[dict]) -> List[str]:
        return [label['name'] for label in labels]
