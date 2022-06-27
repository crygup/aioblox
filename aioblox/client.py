from typing import Any, List, Type
from types import TracebackType

from aiohttp import ClientSession

from .group import Group
from .user import User, UserGroup
from .utils.urls import *


class Client:
    def __init__(self):
        self.session = ClientSession()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"

    async def __aenter__(self):
        return self

    async def __aexit__(
        self,
        _exec_type: Type[BaseException] | None,
        _exec_val: BaseException | None,
        _exec_tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def _request(self, method: str, url: str, **kwargs: Any) -> Any:
        async with self.session.request(method, url, **kwargs) as response:
            return await response.json()

    async def close(self):
        await self.session.close()

    async def fetch_user(self, user_id: int) -> User:
        url = f"{USERS}/users/{user_id}"
        data = await self._request("GET", url)
        return User(data)

    async def fetch_id_by_username(self, username: str) -> int:
        """Fetches a user's ID by username"""
        url = f"{API}/users/get-by-username?username={username}"
        return (await self._request("GET", url))["Id"]

    async def fetch_user_by_username(self, username: str) -> User:
        """Short hand to `fetch_id_by_username` and `fetch_user`"""
        user_id = await self.fetch_id_by_username(username)
        return await self.fetch_user(user_id)

    async def fetch_user_headshot(
        self, user_id: int, width: int = 420, height: int = 420, format: str = "png"
    ) -> str:
        """Fetches a user's headshot url"""

        url = f"https://www.roblox.com/headshot-thumbnail/image?userId={user_id}&width={width}&height={height}&format={format}"
        async with self.session.get(url) as response:
            return str(response.url)

    async def fetch_user_avatar(
        self, user_id: int, width: int = 420, height: int = 420, format: str = "png"
    ) -> str:
        """Fetches a user's avatar url"""

        url = f"https://www.roblox.com/avatar-thumbnail/image?userId={user_id}&width={width}&height={height}&format={format}"
        async with self.session.get(url) as response:
            return str(response.url)

    async def fetch_user_groups(self, user_id: int) -> List[UserGroup]:
        url = f"{GROUPS_V2}/users/{user_id}/groups/roles"
        data = await self._request("GET", url)
        return [UserGroup(group) for group in data["data"]]

    async def fetch_group(self, group_id: int) -> Group:
        url = f"{GROUPS_V1}/groups/{group_id}"
        data = await self._request("GET", url)
        return Group(data)
