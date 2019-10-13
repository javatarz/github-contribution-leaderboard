from multiprocessing import Pool
from typing import List

import requests

from ghcl.models.pull_request import PullRequest


class GithubStats:
    def __init__(self, access_token):
        self._request_headers = {'Authorization': f'token {access_token}'}

    def list_of_prs(self, user_id: str, state=None,
                    request_parallelization_count=5) -> List[PullRequest]:
        url = 'https://api.github.com/search/issues'
        params = dict(
            q=f'is:pr author:{user_id} archived:false',
            sort='created',
            order='desc',
            per_page='100'
        )

        items = self._request(url=url, params=params)['items']
        prs = Pool(request_parallelization_count).map(
            self._to_pull_request, items)

        if state is None:
            return prs
        else:
            def stateNotEqual(pr: PullRequest) -> bool:
                return pr._state != state

            return filter(stateNotEqual, prs)

    def _to_pull_request(self, issues_data: dict) -> PullRequest:
        pr_data = self._request(issues_data['pull_request']['url'])
        all_data = {'issues_data': {**issues_data}, 'pr_data': {**pr_data}}
        return PullRequest(**all_data)

    def _request(self, url: str, params: dict = None) -> dict:
        return requests.get(
            url=url,
            params=params,
            headers=self._request_headers
        ).json()
