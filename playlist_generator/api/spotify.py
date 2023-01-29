from __future__ import annotations

import base64
import json
from typing import Dict

import requests

from .models.model import SearchItemType, SearchResult


class Spotify:
    def __init__(
            self,
            base_url: str = "https://api.spotify.com",
            login_url: str = "https://accounts.spotify.com/api/token"
    ):
        self._headers = None
        self._base_url = base_url
        self._login_url = login_url

    @staticmethod
    def _load_creds():
        with open("config.json") as config_file:
            credentials = json.load(config_file)
        client_id = credentials["client_id"]
        client_secret = credentials["client_secret"]
        return client_id, client_secret

    def connect(self) -> None:
        credentials = ":".join(self._load_creds())  # ":".join("dasdaz", "fagdgsdfg")
        base64_encoded_creds = base64.b64encode(credentials.encode()).decode()

        response = requests.post(self._login_url,
                                 data={"grant_type": "client_credentials"},
                                 headers={
                                     "Content-Type": "application/x-www-form-urlencoded",
                                     "Authorization": f"Basic {base64_encoded_creds}"
                                 },
                                 timeout=10
                                 )
        token = response.json()["access_token"]
        self._headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {token}"
        }

    def search(self, q: str, item_type: str = "track") -> dict:
        SearchItemType(item_type)
        response = requests.get(self._base_url + "/v1/search",
                                headers=self._headers,
                                params={
                                    "q": q,
                                    "type": item_type
                                })
        return SearchResult(**response.json())

    def get_tracks_audio_features(self, track_id: str):
        response = requests.get(self._base_url + f"/v1/audio-features/{track_id}",
                                headers=self._headers
                                )
        return response.json()
