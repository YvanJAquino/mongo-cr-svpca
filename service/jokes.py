import asyncio
import httpx
from models import DadJoke

class Joker:

    url = "https://icanhazdadjoke.com"
    headers = {"Accept": "application/json"}

    def __init__(self, client: httpx.AsyncClient):
        self.client = client
        self.client.headers = self.headers
        self.request = self.client.build_request("GET", self.url)
    
    async def get(self):
        resp = await self.client.send(self.request)
        data = resp.json()
        return DadJoke(**data)


# async def main():
#         client = httpx.AsyncClient()
#         joker = Joker(client)
#         joke = await joker.get()
#         print(joke)

# asyncio.run(main())
