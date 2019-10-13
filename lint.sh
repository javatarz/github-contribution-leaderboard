#!/bin/sh

echo "flake8: Syntax errors and undefined names"
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
result_1=$?

echo
echo "flake8: Syntax linting"
flake8 . --count --max-complexity=10 --max-line-length=127 --statistics
result_2=$?

result=$(( $result_1 + $result_2 * 2 ))
exit $result
