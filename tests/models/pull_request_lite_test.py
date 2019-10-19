from datetime import datetime

from tests.models.pr_test_data import PRData

_input = PRData().with_defaults()


class TestDefaults:
    @staticmethod
    def test_should_create_pull_request():
        pr = _input.as_lite_pull_request()

        assert pr._html_url == 'some-html-url'
        assert pr._state == 'some_state'
        assert pr._labels == ['label-1', 'label-2']
        assert pr._created_at == datetime(2014, 4, 24, 16, 34, 47)
        assert pr.pull_request_url == 'some-url'


class TestCreatedBetween:
    @staticmethod
    def test_in_between():
        pr = _input.with_created_at(
            '2019-12-25T16:35:49Z').as_lite_pull_request()

        assert pr.created_between(
            start_date=datetime(2018, 1, 1),
            end_date=datetime(2020, 1, 1)
        )

    @staticmethod
    def test_not_in_between():
        pr = _input.with_created_at(
            '2019-12-25T16:35:49Z').as_lite_pull_request()

        assert pr.created_between(
            start_date=datetime(2020, 1, 1),
            end_date=datetime(2021, 1, 1)
        ) is False

    @staticmethod
    def test_created_at_start():
        pr = _input.with_created_at(
            '2019-12-25T16:35:49Z').as_lite_pull_request()

        assert pr.created_between(
            start_date=datetime(2019, 12, 25, 16, 35, 49),
            end_date=datetime(2021, 1, 1)
        )

    @staticmethod
    def test_created_at_end():
        pr = _input.with_created_at(
            '2019-12-25T16:35:49Z').as_lite_pull_request()

        assert pr.created_between(
            start_date=datetime(2017, 1, 1),
            end_date=datetime(2019, 12, 25, 16, 35, 49)
        )
