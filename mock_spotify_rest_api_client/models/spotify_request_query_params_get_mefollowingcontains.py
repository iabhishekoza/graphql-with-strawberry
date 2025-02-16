from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.spotify_request_query_params_get_mefollowingcontains_type import (
    SpotifyRequestQueryParamsGETMefollowingcontainsType,
)

T = TypeVar("T", bound="SpotifyRequestQueryParamsGETMefollowingcontains")


@_attrs_define
class SpotifyRequestQueryParamsGETMefollowingcontains:
    """
    Attributes:
        ids (str):
        type_ (SpotifyRequestQueryParamsGETMefollowingcontainsType):
    """

    ids: str
    type_: SpotifyRequestQueryParamsGETMefollowingcontainsType

    def to_dict(self) -> dict[str, Any]:
        ids = self.ids

        type_ = self.type_.value

        field_dict: dict[str, Any] = {}
        field_dict.update(
            {
                "ids": ids,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        ids = d.pop("ids")

        type_ = SpotifyRequestQueryParamsGETMefollowingcontainsType(d.pop("type"))

        spotify_request_query_params_get_mefollowingcontains = cls(
            ids=ids,
            type_=type_,
        )

        return spotify_request_query_params_get_mefollowingcontains
