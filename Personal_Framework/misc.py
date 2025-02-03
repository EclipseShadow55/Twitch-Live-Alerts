import json
import os
import requests as rq

with open("../Hidden/data.json", "r") as f:
    data = json.load(f)
    client_id = data[0]
    client_secret = data[1]

def get_access():
    url = "https://id.twitch.tv/oauth2/token"
    params = {
        "client_id": client_id,
        "client_secret": client_secret,
    "grant_type": "client_credentials"
    }
    response = rq.post(url, params=params)
    return response.json()["access_token"]

with open("channels.json", "r") as f:
    channels = json.load(f)

def reset_ids():
    for channel in channels:
        channels[channel]["id"] = None

    with open("channels.json", "w") as f:
        json.dump(channels, f, indent=2)

def set_ids():
    toget = []
    for channel in channels:
        if channels[channel]["id"] is None:
            toget.append(channel)

    with open("../Hidden/data.json", "r") as f:
        data = json.load(f)
        client_id = data[0]
        client_secret = data[1]

    url = f"https://api.twitch.tv/helix/users?{"&".join([f"login={channel}" for channel in toget])}"
    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {get_access()}",
    }

    del client_secret
    response = rq.get(url, headers=headers)
    for i in range(len(toget)):
        channels[toget[i]]["id"] = response.json()["data"][i]["id"]

    with open("channels.json", "w") as f:
        json.dump(channels, f, indent=2)

def clear_log(file):
    with open(file, "w") as f:
        f.write("")

if __name__ == "__main__":
    command = input(">>> ").split()
    while command[0] != "exit":
        if command[0] == "ids":
            if len(command) == 1:
                print(channels)
            else:
                if command[1] == "reset":
                    reset_ids()
                    print("IDs reset")
                elif command[1] == "set":
                    set_ids()
                    print("IDs set")
        elif command[0] == "log":
            if len(command) == 1:
                print("No file specified")
            elif len(command) == 2:
                print("No file specified")
            else:
                if command[1] == "clear":
                    if os.path.isfile(command[2]):
                        clear_log(command[2])
                        print("Log cleared")
                    else:
                        print("File specified could not be found")
        command = input(">>> ").split()