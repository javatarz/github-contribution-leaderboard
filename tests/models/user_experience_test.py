import pytest

from ghcl.models.user_experience import OutOfRangeException, UserPRExperience


@pytest.mark.parametrize(
    "input,expected",
    [
        (0, UserPRExperience.first_timers),
        (3, UserPRExperience.first_timers),
        (5, UserPRExperience.novice),
        (6, UserPRExperience.novice),
        (8, UserPRExperience.novice),
        (10, UserPRExperience.regulars),
        (11, UserPRExperience.regulars),
        (30, UserPRExperience.regulars),
        (50, UserPRExperience.veterans),
        (51, UserPRExperience.veterans),
        (75, UserPRExperience.veterans),
        (100, UserPRExperience.legends),
        (101, UserPRExperience.legends),
        (150, UserPRExperience.legends)
    ]
)
def test_user_experience_evaluation(input, expected):
    actual = UserPRExperience.find(input)
    assert actual == expected


def test_non_overlapping_user_experience_boundaries():
    ranges = [range(item.value[0], item.value[1])
              for item in UserPRExperience]
    count = len(ranges)
    for i in range(0, count):
        if i + 1 < count:
            target = ranges[i]
            for j in range(i + 1, count):
                intersection = set(target).intersection(ranges[j])
                assert len(intersection) == 0


def test_raise_error_for_negative_prs():
    input = -1
    with pytest.raises(OutOfRangeException) as exception_info:
        assert UserPRExperience.find(input) is None
    assert exception_info.value.args[0] == input


def test_raise_error_for_out_of_range_pr_count():
    input = 1000001
    with pytest.raises(OutOfRangeException) as exception_info:
        assert UserPRExperience.find(input) is None
    assert exception_info.value.args[0] == input
