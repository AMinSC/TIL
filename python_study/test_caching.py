from functools import cache


def get_travel(place: str):
    print(f'우리가 여행갔던 곳은 "{place}"입니다.')


@cache
def fetch_place(place: str):
    return get_travel(place)


if __name__ == "__main__":
    from random import choice

    for i in range(10):
        fetch_place(place=choice(["Sokcho", "Gangneung", "Jeonju"]))
    print(fetch_place.cache_info())
