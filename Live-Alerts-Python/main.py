"""Main module for the LiveAlertDiscordBot"""
import winotify

import twitch_access as ta
import discord_access as da
import json
from time import sleep
from datetime import datetime
from winotify import Notification
import os


def get_dict_from_attr(dict_list: list[dict], attr, value):
    """Get a dictionary from a list of dictionaries based on an attribute"""
    for dictionary in dict_list:
        if dictionary[attr] == value:
            return dictionary
    return None

def main(path_to_data: str, path_to_channels: str, path_to_log: str, path_to_errors: str):
    """Main function for the LiveAlertDiscordBot"""
    # Load the data and channels
    with open(path_to_data, "r") as f:
        data = json.load(f)
    with open(path_to_channels, "r") as f:
        channels = json.load(f)
    with open(path_to_errors, "w") as f:
        f.write("")
    # Create a dictionary to store the live status of each channel
    is_live = {}
    for name in channels:
        is_live[name] = [False, False, None]
    cons_errors = 0
    # Main loop
    while True:
        try:
            # Load the channels
            with open(path_to_channels, "r") as f:
                old = channels
                channels = json.load(f)
                for name in channels:
                    if name not in old:
                        is_live[name] = [False, False]
            # Check for live streams
            print(f"\n\n{datetime.now().strftime(format='%H:%M:%S.%f, %d/%m/%Y %Z')}\nChecking for live streams...\n")
            stream_data = ta.get_stream_data(list(channels.keys()), data[0], ta.get_access_token(data[0], data[1]))
            for channel in channels:
                if channel.lower() in [stream["user_login"] for stream in stream_data]:
                    if not is_live[channel][0]:
                        is_live[channel][0] = True
                        info = get_dict_from_attr(stream_data, "user_login", channel.lower())
                        print(da.live_alerts(channels[channel], channel, info))
                        winotify.Notification(title=f"{channel} Is Now Live!",
                                              msg=f"{info["title"]}\nPlaying {info['game_name']}\nViewers:{info['viewer_count']}",
                                              duration="long",
                                              app_id="LiveAlertDiscordBot").show()
                else:
                    if is_live[channel][0]:
                        is_live[channel][0] = False
                        print(da.live_alerts(channels[channel], channel, None))
                        winotify.Notification(title=f"{channel} Is Now Offline!",
                                              msg=f"{channel} is now offline.",
                                              duration="long",
                                              app_id="LiveAlertDiscordBot").show()
            sleep(10)
            cons_errors = 0
        except Exception as e:
            # Log the error
            with open(path_to_errors, "a") as f:
                print(f"{datetime.now().strftime(format='%H:%M:%S.%f, %d/%m/%Y %Z')}\n\t{e}",
                      file=f,
                      end="\n\n")
            if cons_errors < 5:
                cons_errors += 1
                sleep(120)
            else:
                note = Notification(title="LiveAlertDiscordBot Error",
                                    msg="Too many consecutive errors. Shutting down.",
                                    duration="long",
                                    app_id="LiveAlertDiscordBot")
                note.show()
                raise Exception("Too many consecutive errors.") from e

if __name__ == "__main__":
    log_file = "Logs/log.txt"
    error_file = "Logs/errors.txt"
    channels_file = "Data/channels.json"
    data_file = "../Required/data.json"
    if not os.path.isfile(data_file):
        print(f"{data_file} not found. Please create the file with the required authorization data.")
        exit(1)
    if not os.path.isfile(channels_file):
        with open(channels_file, "x") as f:
            json.dump({}, f, indent=4)
        print(f"{channels_file} not found. Please add channel data. to the newly created file")
    if not os.path.isfile(log_file):
        with open(log_file, "x") as f:
            print(f"Log file created at {log_file}.")
    if not os.path.isfile(error_file):
        with open(error_file, "x") as f:
            print(f"Errors file created at {error_file}")
    main(data_file,
         channels_file,
         log_file,
         error_file)
