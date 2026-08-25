import os
import dotenv 
import requests
import time
from pathlib import Path

class TwitchAPI:
    env_path = Path(__file__).resolve().parent.parent / '.env'
    dotenv.load_dotenv(dotenv_path=env_path)

    dotenv.load_dotenv()

    CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
    CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")


    def __init__(self):
        self.token = None
        self.token_exp = 0

    def generate_token(self):

        response = requests.post(
            "https://id.twitch.tv/oauth2/token",
            data={
                "client_id": self.CLIENT_ID,
                "client_secret":self.CLIENT_SECRET,
                "grant_type":"client_credentials"
            }
        )

        if response.status_code == 200:
            data = response.json()
            self.token = data["access_token"]
            self.token_exp = time.time() + data["expires_in"]
        else:
            self.token = None
            self.token_exp = 0

    def token_valid(self) -> bool:
        return time.time() < self.token_exp

    def live(self, user: str) -> bool:

        if not self.token_valid():
            self.generate_token()

        response = requests.get(
            f"https://api.twitch.tv/helix/streams?user_login={user}",
            headers={
                "Client-ID":self.CLIENT_ID,
                "Authorization": f"Bearer {self.token}"
            }
        )

        if response.status_code == 200 and response.json()["data"]:
            data = response.json()["data"]
            print(data)
            return True

        return False        