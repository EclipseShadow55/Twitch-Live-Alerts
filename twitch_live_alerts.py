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

"""Main module for the LiveAlertDiscordBot"""
import sys

import winotify

import twitch_access as ta
import discord_access as da
import json
from time import sleep
from datetime import datetime
import os

def get_dict_from_attr(dict_list: list[dict], attr, value):
    """Get a dictionary from a list of dictionaries based on an attribute"""
    for dictionary in dict_list:
        if dictionary[attr] == value:
            return dictionary
    return None

def main(path_to_data: str, path_to_channels: str, path_to_log: str, path_to_errors: str):
    ignore = "--start-ignore" in sys.argv
    no_notif = "--no-notif" in sys.argv
    no_offline = "--no-offline" in sys.argv
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
    token = ta.get_access_token(data[0], data[1])
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
            stream_data = ta.get_stream_data(list(channels.keys()), data[0], token)
            if isinstance(stream_data, dict):
                if stream_data.get("error", "") == "Unauthorized":
                    token = ta.get_access_token(data[0], data[1])
                    stream_data = ta.get_stream_data(list(channels.keys()), data[0], token)
            for channel in channels:
                if channel.lower() in [stream["user_login"] for stream in stream_data]:
                    if not is_live[channel][0]:
                        is_live[channel][0] = True
                        info = get_dict_from_attr(stream_data, "user_login", channel.lower())
                        if not ignore:
                            print(da.live_alerts(channels[channel], channel, info))
                        if not no_notif:
                            winotify.Notification(title=f"{channel} Is Now Live!",
                                                  msg=f"{info["title"]}\nPlaying {info['game_name']}\nViewers:{info['viewer_count']}",
                                                  duration="long",
                                                  app_id="LiveAlertDiscordBot").show()
                else:
                    if not no_offline:
                        if is_live[channel][0]:
                            is_live[channel][0] = False
                            print(da.live_alerts(channels[channel], channel, None))
                            if not no_notif:
                                winotify.Notification(title=f"{channel} Is Now Offline!",
                                                      msg=f"{channel} is now offline.",
                                                      duration="long",
                                                      app_id="LiveAlertDiscordBot").show()
            sleep(20)
            cons_errors = 0
        except Exception as e:
            with open(path_to_errors, "a") as f:
                print(f"{datetime.now().strftime(format='%H:%M:%S.%f, %d/%m/%Y %Z')}\n\t{e}",
                      file=f,
                      end="\n\n")

            if cons_errors < 10:
                cons_errors += 1
                sleep(120 * 2**cons_errors)
            else:
                winotify.Notification(title="LiveAlertDiscordBot Error",
                                    msg="Too many consecutive errors. Shutting down.",
                                    duration="long",
                                    app_id="LiveAlertDiscordBot").show()
                raise Exception("Too many consecutive errors.") from e
        ignore = False

if __name__ == "__main__":
    log_file = "Logs/log.txt"
    error_file = "Logs/errors.txt"
    channels_file = "Data/channels.json"
    data_file = "Required/auth.json"
    if not os.path.isfile(data_file):
        raise ValueError(f"{data_file} not found. Please create the file with the required authorization data.")
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
