![Test](https://github.com/javatarz/github-contribution-leaderboard/workflows/Test/badge.svg) ![Lint](https://github.com/javatarz/github-contribution-leaderboard/workflows/Lint/badge.svg)

## Installation
```bash
pip3 install pipenv
pipenv install --dev
pipenv shell
```

## Usage

### Generating a token
Go to [Settings > Developer Settings > Personal Access Token](https://github.com/settings/tokens) and click generate a token. Give the token a name and *do not* give it any selected scope. Click generate token. Copy the token and keep it safe. You can't get the token value back from this page once you leave it.

If you lose it, come back to the [Personal Access Token](https://github.com/settings/tokens) page, delete the old token and generate the new one.

#### Token security
Keep this token safe. It maps to your ID. **DO NOT** share it with anyone. **DO NOT** check in the token anywhere.

If the token gets compromised, [reset it](#generating-a-token).

### CLI
```
usage: stats.py [-h] -at ACCESS_TOKEN [-m MODE] -u USERS [USERS ...]
                [-s START_DATE] [-e END_DATE] [-hps HTTP_POOL_SIZE] [-ws]
                [-wns]
stats.py: error: the following arguments are required: -u/--users
```

example:
```python stats.py \

-at abcdefghijklmnopqrstuvwxyz1234567890abcd \
-u javatarz mojombo defunkt \
-s 2019-10-01 \
-e 2019-10-31 \
-m all
-hps 10
```

### Web

- Create a folder named `instance` with two files named `config.py` and `secrets.py`
- `config.py` should look like this;

  ```python
  USERS = ['javatarz', 'mojombo', 'defunkt']
  START_DATE = '2019-10-01'
  END_DATE = '2019-10-31'
  ```
- `secrets.py` should look like this;

  ```python
  ACCESS_TOKEN = 'YOUR_GITHUB_ACCESS_TOKEN'
  ```

- Start the application;

  ```bash
  flask run
  ```


## Contributions
Please read the [contribution guide](CONTRIBUTING.md) for detailed steps on how to contribute to this project
