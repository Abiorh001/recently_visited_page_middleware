# utils.py
from django.core.cache import cache

MAX_RECENT_URLS = 10


def get_recently_visited_urls(user_id):
    cache_key = f'recently_visited_urls_{user_id}'
    return cache.get(cache_key, [])


def add_to_recently_visited(user_id, url):
    cache_key = f'recently_visited_urls_{user_id}'
    recently_visited_urls = get_recently_visited_urls(user_id)

    if url in recently_visited_urls:
        recently_visited_urls.remove(url)

    recently_visited_urls.insert(0, url)

    # Keep only the latest MAX_RECENT_URLS
    recently_visited_urls = recently_visited_urls[:MAX_RECENT_URLS]

    cache.set(cache_key, recently_visited_urls, timeout=None)
