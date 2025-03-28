"""
Copyright 2025 EclipseShadow55

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

"""Module that sends webhook messages to Discord channels."""

import requests
import json
import time


def send_message(webhook_url, message, embeds):
    data = {
        "content": message,
        "embeds": embeds
    }
    response = requests.post(webhook_url, json=data)
    return [message, [response.status_code == 204, response.status_code, response.text]]


def live_alerts(webhook_urls, channel_name, info, test=False):
    t = str(time.time()).replace(".", "")
    with open("Data/info.json", "r") as f:
        additional_urls = json.load(f).get("additional_urls", [])
    if info is not None:
        message = f"{info['user_name']} Is Now Live!"
        embeds = [
            {
                "title": info["title"],
                "url": f"https://www.twitch.tv/{channel_name}",
                "fields": [
                    {
                        "name": "Category",
                        "value": info["game_name"]
                    },
                    {
                        "name": "Viewers",
                        "value": info["viewer_count"]
                    }
                ],
                "image": {
                    "url": info["thumbnail_url"].replace("{width}", "400").replace("{height}", "225") + "?t=" + t
                },
            }
        ]
    else:
        message = f"{channel_name} Is Offline!"
        embeds = [
            {
                "title": f"{channel_name}'s Channel",
                "description": "Check Out Their Channel While They're Away!",
                "url": f"https://www.twitch.tv/{channel_name}",
            }
        ]
    if webhook_urls is not None and not test:
        if isinstance(webhook_urls, list):
            return [send_message(url, message, embeds) for url in webhook_urls] + [send_message(url, message, embeds) for url in additional_urls]
        else:
            return [send_message(url, message, embeds) for url in additional_urls].append(send_message(webhook_urls, message, embeds))
    else:
        return [send_message(url, message, embeds) for url in additional_urls]