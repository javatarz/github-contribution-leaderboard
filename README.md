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
                [-s START_DATE] [-e END_DATE]

optional arguments:
  -h, --help            show this help message and exit
  -at ACCESS_TOKEN, --access-token ACCESS_TOKEN
  -m MODE, --mode MODE
  -u USERS [USERS ...], --users USERS [USERS ...]
  -s START_DATE, --start-date START_DATE
                        date format YYYY-mm-dd
  -e END_DATE, --end-date END_DATE
                        date format YYYY-mm-dd
```

### Web

`flask run`


## Contributions
Please read the [contribution guide](CONTRIBUTING.md) for detailed steps on how to contribute to this project
