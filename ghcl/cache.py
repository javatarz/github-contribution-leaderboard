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
    CACHE_DURATION_IN_SECONDS = 60

    def __init__(self):
        self.redis = redis.Redis()

    def exists(self, cache_key) -> bool:
        return self.redis.exists(cache_key)

    def set(self, cache_key, value) -> bool:
        return self.redis.set(cache_key, value, self.CACHE_DURATION_IN_SECONDS)

    def fetch(self, cache_key) -> str:
        return self.redis.get(cache_key)
