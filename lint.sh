#!/bin/sh

echo "flake8: Syntax errors and undefined names"
pipenv run flake8 . --select=E9,F63,F7,F82 --show-source --statistics
result_1=$?

echo
echo "flake8: Syntax linting"
pipenv run flake8 . --max-complexity=10 --max-line-length=127 --statistics
result_2=$?

echo
echo "pycodestyle"
pipenv run pycodestyle .
result_3=$?

result=$(( $result_1 + $result_2 * 2 + $result_3 * 5))
exit $result
