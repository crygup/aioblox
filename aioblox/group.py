from __future__ import annotations

import datetime
from typing import Dict, Optional

from aiohttp import ClientSession
from dateutil.parser import parse


class Group:
    def __init__(self, data: Dict):
        self._data = data

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}' id={self.id} owner={GroupOwner(self._data['owner'])}>"

    @property
    def id(self) -> int:
        return self._data["id"]

    @property
    def name(self) -> str:
        return self._data["name"]

    @property
    def description(self) -> Optional[str]:
        description = self._data["description"]
        return description if description != "" else None

    @property
    def member_count(self) -> int:
        return self._data["memberCount"]

    @property
    def is_builders_club_only(self) -> bool:
        return self._data["isBuildersClubOnly"]

    @property
    def public_entry_allowed(self) -> bool:
        return self._data["publicEntryAllowed"]

    @property
    def owner(self) -> GroupOwner:
        return GroupOwner(self._data["owner"])

    @property
    def shout(self) -> Optional[GroupShout]:
        data = self._data["shout"]
        return GroupShout(data) if data is not None else None


class GroupOwner:
    def __init__(self, data: Dict):
        self._data = data

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}' id={self.id}>"

    @property
    def id(self) -> int:
        return self._data["userId"]

    @property
    def name(self) -> str:
        return self._data["username"]

    @property
    def display_name(self) -> Optional[str]:
        """The user's display name."""
        return (
            self._data["displayName"]
            if self._data["displayName"] != self._data["username"]
            else None
        )

    @property
    def builders_club_membership_type(self) -> Optional[str]:
        membership_type = self._data["buildersClubMembershipType"]
        return membership_type if membership_type != "None" else None


class GroupShout:
    def __init__(self, data: Dict):
        self._data = data

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"

    @property
    def body(self) -> Optional[str]:
        data = self._data["body"]
        return data if data != "" else None

    @property
    def created_at(self) -> datetime.datetime:
        return parse(self._data["created"])

    @property
    def updated_at(self) -> datetime.datetime:
        return parse(self._data["updated"])

    @property
    def poster(self) -> GroupShoutPoster:
        return GroupShoutPoster(self._data["poster"])


class GroupShoutPoster:
    def __init__(self, data: Dict):
        self._data = data

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} name='{self.name}' id={self.id}>"

    @property
    def id(self) -> int:
        return self._data["userId"]

    @property
    def name(self) -> str:
        return self._data["username"]

    @property
    def display_name(self) -> Optional[str]:
        """The user's display name."""
        return (
            self._data["displayName"]
            if self._data["displayName"] != self._data["username"]
            else None
        )

    @property
    def builders_club_membership_type(self) -> Optional[str]:
        membership_type = self._data["buildersClubMembershipType"]
        return membership_type if membership_type != "None" else None
