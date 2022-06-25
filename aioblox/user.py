from __future__ import annotations

import datetime
from typing import Dict, Optional

from dateutil.parser import parse


class User:
    def __init__(self, data: Dict):
        self._data = data

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.username}' id={self.id}>"

    def __str__(self) -> str:
        return self.username

    @property
    def id(self) -> int:
        """The ID of the user."""
        return self._data["id"]

    @property
    def username(self) -> str:
        """The user's username."""
        return self._data["name"]

    @property
    def display_name(self) -> Optional[str]:
        """The user's display name."""
        return (
            self._data["displayName"]
            if self._data["displayName"] != self._data["name"]
            else None
        )

    @property
    def banned(self) -> bool:
        """Whether the user is banned."""
        return self._data["isBanned"]

    @property
    def description(self) -> Optional[str]:
        """The user's description."""
        return self._data["description"] if self._data["description"] else None

    @property
    def created_at(self) -> datetime.datetime:
        """:class:`datetime` when the user was created."""
        return parse(self._data["created"])

    @property
    def external_app_display_name(self) -> Optional[str]:
        """The user's external app display name."""
        return (
            self._data["externalAppDisplayName"]
            if self._data["externalAppDisplayName"]
            else None
        )


class UserGroup:
    def __init__(self, data: Dict):
        self._data = data

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"

    @property
    def group(self) -> UserMiniGroup:
        """The group."""
        return UserMiniGroup(self._data["group"])

    @property
    def role(self) -> UserGroupRole:
        """The users role in the group"""
        return UserGroupRole(self._data["role"])


class UserMiniGroup:
    def __init__(self, data: Dict):
        self._data = data

    @property
    def id(self) -> int:
        """The ID of the group."""
        return self._data["id"]

    @property
    def name(self) -> str:
        """The name of the group."""
        return self._data["name"]

    @property
    def member_count(self) -> int:
        """The number of members in the group."""
        return self._data["memberCount"]


class UserGroupRole:
    def __init__(self, data: Dict):
        self._data = data

    @property
    def id(self) -> int:
        """The ID of the users role in the group."""
        return self._data["id"]

    @property
    def name(self) -> str:
        """The name of the users role in the group."""
        return self._data["name"]

    @property
    def rank(self) -> int:
        """The rank of the users role in the group."""
        return self._data["rank"]
