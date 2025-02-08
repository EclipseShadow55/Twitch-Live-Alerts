import json
import twitch_access as ta

def main():
    while input("Do you want to add a channel? (y/n): ") == "y":
        channel = input("Enter channel name: ")
        url = input("Enter the Discord webhook (or \"none\" if none): ")
        if url == "none":
            url = None
        with open("Data/channels.json", "r") as f:
            channels = json.load(f)
        if not isinstance(channels, dict):
            channels = {}
        channels[channel] = url
        with open("Data/channels.json", "w") as f:
            json.dump(channels, f, indent=4)
        print(f"Success! Added {channel} with url {url} to channels.json")


if __name__ == "__main__":
    main()