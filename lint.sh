#!/bin/sh

echo "flake8: Syntax errors and undefined names"
pipenv run flake8 . --show-source --statistics --max-complexity=10 --max-line-length=127 --statistics
result_1=$?

echo
echo "pycodestyle"
pipenv run pycodestyle .
result_2=$?

result=$(( $result_1 + $result_2 * 2))
exit $result
