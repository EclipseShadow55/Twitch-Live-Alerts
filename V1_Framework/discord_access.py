import requests


def send_message(webhook_url, message):
    data = {
        "content": message
    }
    response = requests.post(webhook_url, json=data)
    return [message, [response.status_code == 204, response.status_code, response.text]]


def live_alerts(webhook_url, channel_name, info):
    additional_url = "https://discord.com/api/webhooks/1306136270426214430/YIiMAGpAXmBG7ugd2lD1s300aHL_AbdDJtPi-OOkYA0zJsJgRFDIjibj6251fwIJaFd0"

    if info is not None:
        message = "\n".join([f"{info['user_name']} Is Now Live!",
                             f"<https://www.twitch.tv/{channel_name}>",
                             f"Title: {info['title']}",
                             f"Category: {info['game_name']}",
                             f"Viewers: {info['viewer_count']}",
                             f"Language: {info['language'].upper()}"])
    else:
        message = f"{channel_name} Is Offline!\n<https://www.twitch.tv/{channel_name}>"

    if webhook_url is not None:
        if isinstance(webhook_url, list):
            webhook_url.append(additional_url)
            return [send_message(url, message) for url in webhook_url]
        else:
            return [send_message(webhook_url, message), send_message(additional_url, message)]
    else:
        return send_message(additional_url, message)