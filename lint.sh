#!/bin/sh

echo "flake8: Syntax errors and undefined names"
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

echo
echo "flake8: Syntax linting"
flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
