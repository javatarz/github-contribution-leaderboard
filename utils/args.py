from argparse import ArgumentParser, ArgumentTypeError
from datetime import datetime


def valid_date(s: str) -> datetime:
    format = "%Y-%m-%d"
    try:
        return datetime.strptime(s, format)
    except ValueError:
        raise ArgumentTypeError(
            f"Invalid date format. '{s}' needs to be in '{format}'.")


def valid_mode(mode: str) -> str:
    valid_modes = ['leaderboard', 'prs', 'all']
    if mode not in valid_modes:
        raise ArgumentTypeError(
            f"Invalid mode. {mode} must be from {valid_modes}")
    return mode


def parse_args():
    parser = ArgumentParser()

    parser.add_argument('-at', '--access-token',
                        dest='access_token', required=True, type=str)

    parser.add_argument('-m', '--mode', dest='mode',
                        default='leaderboard', required=False, type=valid_mode)

    parser.add_argument('-u', '--users', dest='users',
                        nargs='+', required=True, type=str)

    parser.add_argument('-s', '--start-date', dest='start_date',
                        help="date format YYYY-mm-dd", required=False,
                        default=None, type=valid_date)
    parser.add_argument('-e', '--end-date', dest='end_date',
                        help="date format YYYY-mm-dd", required=False,
                        default=None, type=valid_date)

    parser.add_argument('-hps', '--http-pool-size', dest='http_pool_size',
                        help='number of simultaneous API calls to fetch PRs',
                        required=False, default=10)

    return vars(parser.parse_args())
