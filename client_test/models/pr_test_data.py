import copy
import json

from client.models.pull_request import PullRequest


class PRData:
    def __init__(self, data: dict = None):
        if data is None:
            with open('./client_test/models/empty_pr_data.json') as file:
                self._data = json.load(file)
        else:
            self._data = data

    def with_pr_url(self, url: str = 'some-url'):
        data = copy.deepcopy(self._data)
        data['issues_data']['pull_request']['html_url'] = url
        return PRData(data)

    def with_label(self, label_to_add: str = None):
        data = copy.deepcopy(self._data)
        if label_to_add is None:
            label_number = len(data["issues_data"]["labels"]) + 1
            label_to_add = f'label-{label_number}'

        data['issues_data']['labels'].append({'name': label_to_add})
        return PRData(data)

    def with_created_at(self, created_at: str = '2014-04-24T16:34:47Z'):
        data = copy.deepcopy(self._data)
        data['issues_data']['created_at'] = created_at
        return PRData(data)

    def with_owner(self, owner: str = 'owner_user_id'):
        data = copy.deepcopy(self._data)
        data['pr_data']['base']['repo']['owner']['login'] = owner
        return PRData(data)

    def with_pr_raised_by(self, pr_raised_by: str = 'pr_raised_by_user_id'):
        data = copy.deepcopy(self._data)
        data['pr_data']['head']['user']['login'] = pr_raised_by
        return PRData(data)

    def with_merged(self, merged=False):
        data = copy.deepcopy(self._data)
        data['pr_data']['merged'] = merged
        return PRData(data)

    def with_state(self, state='some_state'):
        data = copy.deepcopy(self._data)
        data['issues_data']['state'] = state
        return PRData(data)

    def with_defaults(self):
        return PRData(self._data).with_pr_url()\
            .with_label()\
            .with_label()\
            .with_created_at()\
            .with_owner()\
            .with_pr_raised_by()\
            .with_merged()\
            .with_state()

    def as_pull_request(self):
        return PullRequest(**self._data)
