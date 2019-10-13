from datetime import datetime
from client.models.pull_request import PullRequest
from client_test.models.pr_test_data import PRData


_input = PRData().with_defaults()


class TestDefaults:
    @staticmethod
    def test_should_create_pull_request():
        data = _input.data
        pr = PullRequest(**data)

        assert pr._url == 'some-url'
        assert pr._state == 'some_state'
        assert pr._labels == ['label-1', 'label-2']
        assert pr._created_at == datetime(2014, 4, 24, 16, 34, 47)
        assert pr._owner == 'owner_user_id'
        assert pr._pr_raised_by == 'pr_raised_by_user_id'
        assert pr._merged is False

    @staticmethod
    def test_summary():
        data = _input.data
        pr = PullRequest(**data)

        assert pr.summary() == 'URL: some-url | Score: 0'


class TestIsSpam:
    @staticmethod
    def test_should_not_be_spam_when_labels_do_not_contain_invalid_and_spam():
        data = _input.data
        pr = PullRequest(**data)

        assert pr.is_spam() is False

    @staticmethod
    def test_should_be_spam_when_labels_contain_invalid():
        data = _input.with_label('invalid').data
        pr = PullRequest(**data)

        assert pr._labels == ['label-1', 'label-2', 'invalid']
        assert pr.is_spam()

    @staticmethod
    def test_should_be_spam_when_labels_contain_spam():
        data = _input.with_label('spam').data
        pr = PullRequest(**data)

        assert pr._labels == ['label-1', 'label-2', 'spam']
        assert pr.is_spam()


class TestCreatedBetween:
    @staticmethod
    def test_in_between():
        data = _input.with_created_at('2019-12-25T16:35:49Z').data
        pr = PullRequest(**data)

        assert pr.created_between(
            start_date=datetime(2018, 1, 1),
            end_date=datetime(2020, 1, 1)
        )

    @staticmethod
    def test_not_in_between():
        data = _input.with_created_at('2019-12-25T16:35:49Z').data
        pr = PullRequest(**data)

        assert pr.created_between(
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2021, 1, 1)
        ) is False

    @staticmethod
    def test_created_at_start():
        data = _input.with_created_at('2019-12-25T16:35:49Z').data
        pr = PullRequest(**data)

        assert pr.created_between(
            start_date=datetime(2019, 12, 25, 16, 35, 49),
            end_date=datetime(2021, 1, 1)
        )

    @staticmethod
    def test_created_at_end():
        data = _input.with_created_at('2019-12-25T16:35:49Z').data
        pr = PullRequest(**data)

        assert pr.created_between(
            start_date=datetime(2017, 1, 1),
            end_date=datetime(2019, 12, 25, 16, 35, 49)
        )


class TestPrScore:
    @staticmethod
    def test_merged_pr():
        data = _input.with_merged(True)\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 10

    @staticmethod
    def test_merged_closed_pr():
        data = _input.with_merged(True)\
            .with_state('closed')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 10

    @staticmethod
    def test_spam_pr():
        data = _input.with_label('spam')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == -5

    @staticmethod
    def test_spam_closed_pr():
        data = _input.with_label('spam')\
            .with_state('closed')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == -5

    @staticmethod
    def test_closed_pr():
        data = _input.with_merged(False)\
            .with_state('closed')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 3

    @staticmethod
    def test_open_pr():
        data = _input.with_merged(False)\
            .with_state('open')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 1

    @staticmethod
    def test_default_pr():
        data = _input.data
        pr = PullRequest(**data)

        assert pr.score() == 0


class TestPersonalPrScore:
    @staticmethod
    def test_merged_pr():
        data = _input.with_owner('user-1')\
            .with_pr_raised_by('user-1')\
            .with_merged(True)\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 5

    @staticmethod
    def test_merged_closed_pr():
        data = _input.with_owner('user-1')\
            .with_pr_raised_by('user-1')\
            .with_merged(True)\
            .with_state('closed')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 5

    @staticmethod
    def test_spam_pr():
        data = _input.with_owner('user-1')\
            .with_pr_raised_by('user-1')\
            .with_label('spam')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == -10

    @staticmethod
    def test_spam_closed_pr():
        data = _input.with_owner('user-1')\
            .with_pr_raised_by('user-1')\
            .with_label('spam')\
            .with_state('closed')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == -10

    @staticmethod
    def test_closed_pr():
        data = _input.with_owner('user-1')\
            .with_pr_raised_by('user-1')\
            .with_merged(False)\
            .with_state('closed')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 1

    @staticmethod
    def test_open_pr():
        data = _input.with_owner('user-1')\
            .with_pr_raised_by('user-1')\
            .with_merged(False)\
            .with_state('open')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 1

    @staticmethod
    def test_default_pr():
        data = _input.with_owner('user-1')\
            .with_pr_raised_by('user-1')\
            .data
        pr = PullRequest(**data)

        assert pr.score() == 0
