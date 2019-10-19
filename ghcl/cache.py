import redis


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return getinstance


@singleton
class Cache:
    def __init__(self, cache_duration=60):
        self.redis = redis.Redis()
        self.cache_duration = cache_duration

    def exists(self, cache_key) -> bool:
        return self.redis.exists(cache_key)

    def set(self, cache_key, value) -> bool:
        return self.redis.set(cache_key, value, self.cache_duration)

    def fetch(self, cache_key) -> str:
        return self.redis.get(cache_key)
