from typing import Any, TypeVar, Union

from attrs import define as _attrs_define

from ..models.spotify_request_query_params_get_metopartists_time_range import (
    SpotifyRequestQueryParamsGETMetopartistsTimeRange,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMetopartists")


@_attrs_define
class SpotifyRequestQueryParamsGETMetopartists:
    """
    Attributes:
        limit (Union[Unset, float]):
        offset (Union[Unset, float]):
        time_range (Union[Unset, SpotifyRequestQueryParamsGETMetopartistsTimeRange]):
    """

    limit: Union[Unset, float] = UNSET
    offset: Union[Unset, float] = UNSET
    time_range: Union[Unset, SpotifyRequestQueryParamsGETMetopartistsTimeRange] = UNSET

    def to_dict(self) -> dict[str, Any]:
        limit = self.limit

        offset = self.offset

        time_range: Union[Unset, str] = UNSET
        if not isinstance(self.time_range, Unset):
            time_range = self.time_range.value

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if limit is not UNSET:
            field_dict["limit"] = limit
        if offset is not UNSET:
            field_dict["offset"] = offset
        if time_range is not UNSET:
            field_dict["time_range"] = time_range

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        limit = d.pop("limit", UNSET)

        offset = d.pop("offset", UNSET)

        _time_range = d.pop("time_range", UNSET)
        time_range: Union[Unset, SpotifyRequestQueryParamsGETMetopartistsTimeRange]
        if isinstance(_time_range, Unset):
            time_range = UNSET
        else:
            time_range = SpotifyRequestQueryParamsGETMetopartistsTimeRange(_time_range)

        spotify_request_query_params_get_metopartists = cls(
            limit=limit,
            offset=offset,
            time_range=time_range,
        )

        return spotify_request_query_params_get_metopartists
