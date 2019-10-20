from enum import Enum


class UserPRExperience(Enum):
    first_timers = (0, 5)
    novice = (5, 10)
    regulars = (10, 50)
    veterans = (50, 100)
    legends = (100, 1000000)

    @staticmethod
    def find(pr_count: int):
        for item in UserPRExperience:
            if item.value[0] <= pr_count < item.value[1]:
                return item
        raise OutOfRangeException(pr_count)


class OutOfRangeException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
