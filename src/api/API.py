from urllib.parse import urlencode

import requests

from src.gui import MainWindow


class API:


    def __init__(self, parent: MainWindow):
        self.parent = parent
        self.running_config = parent.running_config
        self.session = requests.Session()

    def _call_api(self, f: str, params: dict, typ: str = "POST") -> dict:
        base_url = self.running_config["api_baseurl"]
        if not base_url.startswith("http://") and not base_url.startswith("https://"):
            base_url = "https://" + base_url  # or default to http:// if needed

        if typ.upper() == "GET":
            full_url = f"{base_url}?{urlencode({'f': f, **params})}"
            try:
                response = self.session.get(full_url)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                print(f"API GET call failed: {e}")
                return {"error": str(e)}
        else:
            full_url = f"{base_url}?f={f}"
            try:
                response = self.session.post(full_url, json=params)
                response.raise_for_status()
                return response.json()
            except requests.RequestException as e:
                print(f"API POST call failed: {e}")
                return {"error": str(e)}

    def call_login(self, callback):
        auth_call = self._call_api(f="auth", params={
            "key": self.running_config["auth_key"]
        })

        callback()

    def call_logout(self, callback):
        logout_call = self._call_api(f="logout", params={})

        callback()
