#!/bin/sh

set -e

pipenv run flake8 . --select C,E,F,W --show-source --statistics --max-complexity=10 --statistics
