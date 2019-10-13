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
        self._owner = kwargs['pr_data']['base']['repo']['owner']['login']
        self._pr_raised_by = kwargs['pr_data']['head']['user']['login']
        self._merged = kwargs['pr_data']['merged']

    def is_spam(self):
        return 'invalid' in self._labels or 'spam' in self._labels

    def score(self) -> int:
        if self._owner == self._pr_raised_by:
            return self._self_pr_score()
        else:
            return self._pr_score()

    def _self_pr_score(self) -> int:
        if self._merged:
            return 5
        elif self.is_spam():
            return -10
        elif self._state == 'closed':
            return 1
        elif self._state == 'open':
            return 1
        else:
            return 0

    def _pr_score(self) -> int:
        if self._merged:
            return 10
        elif self.is_spam():
            return -5
        elif self._state == 'closed':
            return 3
        elif self._state == 'open':
            return 1
        else:
            return 0

    def created_between(self, start_date: datetime,
                        end_date: datetime) -> bool:
        return start_date <= self._created_at <= end_date

    def summary(self) -> str:
        return f"URL: {self._url} | Score: {self.score()}"

    @staticmethod
    def _parse_date(date_str: str) -> datetime:
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')

    @staticmethod
    def _label_names(labels: List[dict]) -> List[str]:
        return [label['name'] for label in labels]
