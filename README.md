![Test](https://github.com/javatarz/github-contribution-leaderboard/workflows/Test/badge.svg)
## Installation
```bash
pip3 install pipenv
pipenv install --dev
pipenv shell
```

## Usage

### CLI
```
python stats.py --help
usage: stats.py [-h] -at ACCESS_TOKEN [-m MODE] -u USERS [USERS ...]
                [-s START_DATE] [-e END_DATE] [-hps HTTP_POOL_SIZE]
stats.py: error: the following arguments are required: -at/--access-token, -u/--users
```

example:
```python stats.py \

-at f1a6f157cff1d9aa284350a71a813a25788f3be3 \
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
