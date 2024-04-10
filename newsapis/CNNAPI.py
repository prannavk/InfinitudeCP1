import asyncio
import aiohttp
import globconstants


async def fetch_news(api_key):
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def main():
    api_key = globconstants.cnn_api_key
    news_data = await fetch_news(api_key)

    # Process the news data
    for article in news_data['articles']:
        print(article)