import time
from functools import wraps
import hashlib


def cache_result(callback):
    cache = {}  # tu bedą wpadać zapamiętane wyniki funkcji

    @wraps(callback)
    def wrapper(*args, **kwargs):
        text = f"callback: {callback.__name__}, args: {args}, kwargs: {kwargs}"
        key = hashlib.md5(text.encode()).hexdigest()

        if key in cache:
            return cache[key]

        result = callback(*args, **kwargs)
        cache[key] = result

        return result

    return wrapper


@cache_result
def get_user(user_id: int):
    print("Pobieram dane z API...")
    time.sleep(2)
    return {"id": user_id, "name": f"User {user_id}"}


@cache_result
def get_admin(user_id: int):
    print("Pobieram dane z API...")
    time.sleep(2)
    return {"id": user_id, "name": f"Admin {user_id}"}

    return {}


print(get_user(1))
print(get_user(1))
print(get_user(2))
print(get_user(2))
print(get_admin(1))
print(get_admin(2))
print(get_admin(1))
# print(get_user.__name__)
