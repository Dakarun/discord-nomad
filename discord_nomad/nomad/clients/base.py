import functools
import json
import requests
from requests.status_codes import codes

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class NomadBaseClient:
    host: str

    @functools.cached_property  # TODO: Validate that caching a session has no impact on bugs
    def _requests(self):
        session = requests.Session()
        return session

    def _get(self, endpoint: str, payload: Dict | None = None, expected_response_codes: List[int] | None = None):
        if expected_response_codes is None:
            expected_response_codes = [codes.ok]
        if payload is None:
            payload = {}
        url = "".join([self.host, endpoint])
        response = self._requests.get(url, params=payload)
        if response.status_code in expected_response_codes:
            response_json = json.loads(response.text)
            return response_json
        else:
            # TODO: Replace with proper exceptions
            raise Exception(f"Unexpected status code {response.status_code}, expected one of {expected_response_codes}")

    def _post(self, endpoint: str, payload: Dict | None = None):
        if payload is None:
            payload = {}
        url = "/".join([self.host, endpoint])
        response = self._requests.post(url, data=payload)
        return response

    def _put(self, endpoint: str, payload: Dict | None = None):
        if payload is None:
            payload = {}
        url = "/".join([self.host, endpoint])
        response = self._requests.put(url, data=payload)
        return response

    def _delete(self, endpoint: str, payload: Dict | None = None):
        if payload is None:
            payload = {}
        url = "/".join([self.host, endpoint])
        response = self._requests.delete(url, data=payload)
        return response
