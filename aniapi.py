import asyncio
from jikanpy import AioJikan


async def anisearch():
    async with AioJikan() as jikan:
        results = await jikan.search('anime', 'Jojo')
    for i in range(len(results['results'])):
        print(results['results'][i]['title'] + ' ' + str(results['results'][i]['episodes']))

asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(anisearch())