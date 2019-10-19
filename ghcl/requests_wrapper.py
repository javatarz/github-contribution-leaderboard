import requests


def http_get(url: str,
             params: dict = None,
             request_headers: dict = None) -> dict:
    response = requests.get(
        url=url,
        params=params,
        headers=request_headers
    )

    if isinstance(response, dict):
        return response
    else:
        return response.json()
