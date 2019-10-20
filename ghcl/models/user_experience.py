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


class ExperienceSummary:
    def __init__(self, user_experience: UserPRExperience,
                 people_count: int,
                 pr_count: int):
        self._user_experience = user_experience
        self._people_count = people_count
        self._pr_count = pr_count

    def summary(self) -> str:
        pr_suffix = 's' if self._pr_count != 1 else ''
        pr_summary = f'{self._pr_count} PR{pr_suffix}'

        people_suffix = 'people' if self._people_count != 1 else 'person'
        people_summary = f'{self._people_count} {people_suffix}'

        user_summary = f'{pr_summary} by {people_summary}'

        return f"  {self._user_experience.name}: {user_summary}"
