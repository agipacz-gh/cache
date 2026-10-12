import time
from functools import wraps
import hashlib
from typing import Any, Callable


def cache_result(callback: Callable) -> Callable:
    cache = {}  # tu bedą wpadać zapamiętane wyniki funkcji

    @wraps(callback)  # pomaga zachowac informaje o oryginalnej funkcji, np. jej nazwę
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for_key = f"callback: {callback.__name__}, args: {args}, kwargs: {kwargs}"
        key = hashlib.md5(for_key.encode()).hexdigest()

        if key in cache:
            return cache[key]

        result = callback(*args, **kwargs)
        cache[key] = result  # zapisuje zwrócony wynik w cache

        return result

    return wrapper


@cache_result
def get_user(user_id: int) -> dict[str, int | str]:
    print("Pobieram dane z API...")
    time.sleep(2)
    return {"id": user_id, "name": f"User {user_id}"}


@cache_result
def get_admin(user_id: int) -> dict[str, int | str]:
    print("Pobieram dane z API...")
    time.sleep(2)
    return {"id": user_id, "name": f"Admin {user_id}"}


print(get_user(1))
print(get_user(2))
print(get_user(1))
print(get_user(2))
print(get_admin(1))
print(get_admin(2))
print(get_admin(1))
# print(get_user.__name__)
# Notatka: dlaczego get_admin nie korzysta z wyniku get_user? Ponieważ nazwa funkcji również znajduje się w kluczu, z którego tworzymy wpis w cache.
