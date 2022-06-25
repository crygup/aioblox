from typing import TypedDict

class GroupMember(TypedDict):
    buildersClubMembershipType: str
    hasVerifiedBadge: bool
    userId: int
    username: str
    displayName: str

class Shout(TypedDict):
    body: str
    poster: GroupMember
    created: str
    updated: str

class GroupResponse(TypedDict):
    id: int
    name: str
    description: str
    owner: GroupMember
    shout: Shout
    memberCount: int
    isBuildersClubOnly: bool
    publicEntryAllowed: bool
    isLocked: bool
    hasVerifiedBadge: bool

class Role(TypedDict):
    id: int
    name: str
    rank: int

class UserResponse(TypedDict):
    description: str
    created: str
    isBanned: bool
    externalAppDisplayName: str
    id: int
    name: str
    displayName: str

class UserGroupResponse(TypedDict):
    group: GroupResponse
    role: Role
