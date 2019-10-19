from typing import List

from ghcl.models.pull_request import PullRequest
from ghcl.models.pull_request_lite import LitePullRequest
from ghcl.requests_wrapper import http_get


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

        items = self._request(url=url, params=params)['items']
        return list(map(self._to_lite_pull_request, items))

    def user_id_from_name(self, user_name: str) -> str:
        url = f"https://api.github.com/users/{user_name}"
        return self._request(url)['id']

    def fetch_pr_data(self, lite_pr: LitePullRequest) -> PullRequest:
        pr_data = self._request(lite_pr.pull_request_url)
        kwargs = {
            'lite_pr': lite_pr,
            'pr_data': pr_data
        }
        return PullRequest(**kwargs)

    def _to_lite_pull_request(self,
                              issues_data: dict) -> LitePullRequest:
        all_data = {'issues_data': {**issues_data}}
        return LitePullRequest(**all_data)

    def _paginated_request(self, url: str, params: dict = None) -> dict:
        response = self._request(url, params)
        aggregate_response = response.json()['items']
        while 'next' in response.links.keys():
            response = self._request(
                url=response.links['next']['url'],
                params=params
            )
            if 'items' in response.keys():
                aggregate_response += (response['items'])
        res = {'items': aggregate_response}
        return res

    def _request(self, url: str, params: dict = None) -> dict:
        return http_get(url, params, request_headers=self._request_headers)
