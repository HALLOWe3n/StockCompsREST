import typing
import asyncio
import aiohttp

from django.conf import settings


URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={apikey}'


async def get_data_alphav(session, symbol: str) -> typing.Dict:
    """
    function for get Stock data from `alphavantage`
    :return: dict
    """
    async with session.get(url=URL.format(symbol=symbol)) as response:
        data = await response.json()
        return data


async def fetch(session):
    task = asyncio.create_task(get_data_alphav(session=session, symbol='ACA'))
    data = await asyncio.gather(task)
    return data


async def main():
    async with aiohttp.ClientSession() as session:
        data = await fetch(session=session)


if __name__ == '__main__':
    asyncio.run(main())
