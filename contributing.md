# Contributing to GHCL

👍🎉 First off, thanks for taking the time to contribute! 🎉👍

It's people like you that make the Open Source model work. So thank you for being awesome!

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

GitHub Contibution Leaderboard (GHCL) is an open source project and we love to receive contributions from our community — you! There are many ways to contribute, from writing tutorials or blog posts, improving the documentation, submitting bug reports and feature requests or writing code which can be incorporated into GHCL itself.

## Table of Contents

* [Code of Conduct](#code-of-conduct)
* [Contributing](#contributing)
  * [Your first contribution](#your-first-contribution)
  * [Reporting bugs](#reporting-bugs)
  * [Requesting a feature](#requesting-a-feature)
  * [Code review process](#code-review-process)

## Code of Conduct

This project and everyone participating in it is governed by the [GHCL Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to [karun@japhet.in](mailto:karun@japhet.in).

## Contributing

Every PR/commit on this repository will be run through a build pipeline to ensure all tests/lint checks pass.

### Executing tests
`pipenv run pytest`

### Running lint checks
`./lint.sh`

### Your first contribution
Unsure where to begin contributing to GHCL? You can start by looking through these

* [good first issue](https://github.com/javatarz/github-contribution-leaderboard/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22+sort%3Acomments-desc) - issues which should only require a few lines of code, and a test or two
* [help-wanted issues](https://github.com/javatarz/github-contribution-leaderboard/issues?q=is%3Aopen+is%3Aissue+label%3A%22help+wanted%22+sort%3Acomments-desc) - issues which should be a bit more involved than beginner issues

Both issue lists are sorted by total number of comments. While not perfect, number of comments is a reasonable proxy for impact a given change will have.

Working on your first Pull Request? You can learn how from this _free_ series, [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first 😸

If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch so it's easier to merge.

### Reporting bugs

If you find a security vulnerability, do NOT open an issue. Email [karun@japhet.in](mailto:karun@japhet.in) instead.

When filing an issue, make sure to answer these five questions:

1. What version of Python are you using (`python --version`)?
1. What operating system and processor architecture are you using?
1. What did you do?
1. What did you expect to see?
1. What did you see instead?

[Open a bug card](https://github.com/javatarz/github-contribution-leaderboard/issues/new?assignees=&labels=bug&template=bug_report.md&title=) on [our issues list](https://github.com/javatarz/github-contribution-leaderboard/issues) on GitHub which describes the issue you're seeing and how you expect it to work.

### Requesting a feature

If you find yourself wishing for a feature that doesn't exist in GHCL, you are probably not alone. There are bound to be others out there with similar needs. Many of the features that GHCL has today have been added because our users saw the need. [Open an feature request](https://github.com/javatarz/github-contribution-leaderboard/issues/new?assignees=&labels=enhancement&template=feature_request.md&title=) on [our issues list](https://github.com/javatarz/github-contribution-leaderboard/issues) on GitHub which describes the feature you would like to see, why you need it, and how it should work.

### Code review process

The core team looks at Pull Requests on a regular basis. Generally, you should see some activity on a PR within 48 hours of raising it. If you don't see any movement from any of the maintainers, please bump the thread by adding a comment.
