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
usage: stats.py [-h] -at ACCESS_TOKEN [-m leaderboard, prs, all] -u USERS [USERS ...]
                [-s START_DATE] [-e END_DATE]

arguments:
  -at ACCESS_TOKEN, --access-token ACCESS_TOKEN
  -u USERS [USERS ...], --users USERS [USERS ...]

optional arguments:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE
                        one of leaderboard, prs or all
  -s START_DATE, --start-date START_DATE
                        date format YYYY-mm-dd
  -e END_DATE, --end-date END_DATE
                        date format YYYY-mm-dd
                        
example:
python stats.py \
-at f1a6f157cff1d9aa284350a71a813a25788f3be3 \
-u javatarz mojombo defunkt \
-s 2019-10-01 \
-e 2019-10-31 \
-m all
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

Add instance folder with :

## Contributions
Please read the [contribution guide](CONTRIBUTING.md) for detailed steps on how to contribute to this project
