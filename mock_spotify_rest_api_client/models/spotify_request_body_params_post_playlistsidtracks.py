from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="SpotifyRequestBodyParamsPOSTPlaylistsidtracks")


@_attrs_define
class SpotifyRequestBodyParamsPOSTPlaylistsidtracks:
    """
    Attributes:
        uris (Union[Unset, list[str]]):
        position (Union[Unset, float]):
    """

    uris: Union[Unset, list[str]] = UNSET
    position: Union[Unset, float] = UNSET

    def to_dict(self) -> dict[str, Any]:
        uris: Union[Unset, list[str]] = UNSET
        if not isinstance(self.uris, Unset):
            uris = self.uris

        position = self.position

        field_dict: dict[str, Any] = {}
        field_dict.update({})
        if uris is not UNSET:
            field_dict["uris"] = uris
        if position is not UNSET:
            field_dict["position"] = position

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: dict[str, Any]) -> T:
        d = src_dict.copy()
        uris = cast(list[str], d.pop("uris", UNSET))

        position = d.pop("position", UNSET)

        spotify_request_body_params_post_playlistsidtracks = cls(
            uris=uris,
            position=position,
        )

        return spotify_request_body_params_post_playlistsidtracks
