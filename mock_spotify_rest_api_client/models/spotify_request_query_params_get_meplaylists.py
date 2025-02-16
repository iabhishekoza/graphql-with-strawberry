from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMeplaylists")


@_attrs_define
class SpotifyRequestQueryParamsGETMeplaylists:
    """
    Attributes:
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
    """

    limit: Union[Unset, float] = UNSET
    offset: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        spotify_request_query_params_get_meplaylists = cls(
            limit=limit,
            offset=offset,
        )

        return spotify_request_query_params_get_meplaylists
