from multiprocessing import Pool
from typing import List

import requests
from ghcl.cache import Cache
import json
from ghcl.models.pull_request import PullRequest


class GithubStats:
    def __init__(self, access_token):
        self._request_headers = {'Authorization': f'token {access_token}'}

    def list_of_prs(self, user_name: str, state=None,
                    request_parallelization_count=5) -> List[PullRequest]:
        url = 'https://api.github.com/search/issues'
        params = dict(
            q=f'is:pr author:{user_name} archived:false',
            sort='created',
            order='asc',
            per_page='100'
        )

        cache_key = f'cache:prs:{user_name}'
        cache = Cache()

        if(cache.exists(cache_key)):
            print("[cached] fetching PRS")
            items = json.loads(cache.fetch(cache_key))
        else:
            items = self._paginated_request(url=url, params=params)['items']
            cache.set(cache_key, json.dumps(items))

        prs = Pool(request_parallelization_count).map(
            self._to_pull_request, items)

        if state is None:
            return prs
        else:
            def stateNotEqual(pr: PullRequest) -> bool:
                return pr._state != state

            return filter(stateNotEqual, prs)

    def user_id_from_name(self, user_name: str) -> str:
        url = f"https://api.github.com/users/{user_name}"
        return self._request(url).json()['id']

    def _to_pull_request(self, issues_data: dict) -> PullRequest:
        pr_data = self._request(issues_data['pull_request']['url']).json()
        all_data = {'issues_data': {**issues_data}, 'pr_data': {**pr_data}}
        return PullRequest(**all_data)

    def _paginated_request(self, url: str, params: dict = None) -> dict:
        response = self._request(url, params)
        aggregate_response = response.json()['items']
        while 'next' in response.links.keys():
            response = requests.get(response.links['next']['url'], params)
            if 'items' in response.json().keys():
                aggregate_response += (response.json()['items'])
        res = {'items': aggregate_response}
        return res

    def _request(self, url: str, params: dict = None) -> dict:
        return requests.get(
            url=url,
            params=params,
            headers=self._request_headers
        )
