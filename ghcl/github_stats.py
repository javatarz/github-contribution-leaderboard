from typing import List

import requests
from requests import Response

from ghcl.models.pull_request import PullRequest
from ghcl.models.pull_request_lite import LitePullRequest


class GithubStats:
    def __init__(self, access_token):
        self._request_headers = {'Authorization': f'token {access_token}'}

    def list_of_prs(self, user_name: str) -> List[LitePullRequest]:
        url = 'https://api.github.com/search/issues'
        params = dict(
            q=f'is:pr author:{user_name} archived:false',
            sort='created',
            order='asc',
            per_page='100'
        )

        items = self._paginated_request(url=url, params=params)['items']
        return list(map(self._to_lite_pull_request, items))

    def user_id_from_name(self, user_name: str) -> str:
        url = f"https://api.github.com/users/{user_name}"
        return self._request(url).json()['id']

    def fetch_pr_data(self, lite_pr: LitePullRequest) -> PullRequest:
        pr_data = self._request(lite_pr.pull_request_url).json()
        kwargs = {
            'lite_pr': lite_pr,
            'pr_data': pr_data
        }
        return PullRequest(**kwargs)

    def _to_lite_pull_request(self, issues_data: dict) -> LitePullRequest:
        data_wrapper = {'issues_data': {**issues_data}}
        return LitePullRequest(**data_wrapper)

    def _paginated_request(self, url: str, params: dict = None) -> dict:
        response = self._request(url, params)
        aggregate_response = response.json()['items']
        while 'next' in response.links.keys():
            response = self._request(
                url=response.links['next']['url'],
                params=params
            )
            response_json = response.json()
            if 'items' in response_json.keys():
                aggregate_response += (response_json['items'])
        res = {'items': aggregate_response}
        return res

    def _request(self, url: str, params: dict = None) -> Response:
        return requests.get(
            url=url,
            params=params,
            headers=self._request_headers
        )
