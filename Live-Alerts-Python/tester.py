import json
import twitch_access as ta
import discord_access as da


def main():
    off = "NyxLitten"
    on = "meerkatmiki"

    with open("../Required/data.json", "r") as f:
        data = json.load(f)
    info = ta.get_stream_data([on], data[0], ta.get_access_token(data[0], data[1]))[0]
    print(da.live_alerts(None, on, info))
    print(da.live_alerts(None, off, None))

main()