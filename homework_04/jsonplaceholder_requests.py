"""
  Создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

import aiohttp

USERS_DATA_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_DATA_URL = 'https://jsonplaceholder.typicode.com/posts'


async def fetch_json_data(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        return data
