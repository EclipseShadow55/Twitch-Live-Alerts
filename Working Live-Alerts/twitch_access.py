"""This file contains functions to get the stream data of a Twitch channel."""
import requests


def get_access_token(client_id, client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }
    response = requests.post(url, params=params)
    return response.json()["access_token"]


def get_stream_data(channel_names, client_id, access_token):
    url = f"https://api.twitch.tv/helix/streams?{"&".join([f'user_login={channel_name.lower()}' for channel_name in channel_names])}"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    try:
        if data.get("data", None) is not None:
            return data["data"]
        else:
            return None
    except Exception as e:
        return e