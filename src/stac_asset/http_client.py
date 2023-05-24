from typing import AsyncIterator, Optional

from aiohttp import ClientSession
from yarl import URL

from .client import Client


class HttpClient(Client):
    session: ClientSession

    def __init__(self, session: Optional[ClientSession] = None) -> None:
        super().__init__()
        if session is None:
            self.session = ClientSession()
        else:
            self.session = session

    async def open_url(self, url: URL) -> AsyncIterator[bytes]:
        async with self.session.get(url) as response:
            response.raise_for_status()
            async for chunk, _ in response.content.iter_chunks():
                yield chunk