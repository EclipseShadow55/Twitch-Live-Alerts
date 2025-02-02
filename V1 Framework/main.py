"""Main module for the LiveAlertDiscordBot"""
import twitch_access as ta
import discord_access as da
import json
from time import sleep
from datetime import datetime
from winotify import Notification
import os


def main(path_to_data: str, path_to_channels: str, path_to_log: str, path_to_errors: str):
    """Main function for the LiveAlertDiscordBot"""
    # Load the data and channels
    with open(path_to_data, "r") as f:
        data = json.load(f)
    with open(path_to_channels, "r") as f:
        channels = json.load(f)
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
            for channel_name in channels:
                sleep(4)
                print("Checking", channel_name)
                access_token = ta.get_access_token(data[0], data[1])
                info = ta.get_stream_data(channel_name,
                                          data[0],
                                          access_token)
                # Check if the channel is live and send message accordingly
                if info is not None:
                    is_live[channel_name][0] = True
                    #is_live[channel_name][2] = br.main(data[0], data[1], channel_name, 120, [20, 10])
                else:
                    is_live[channel_name][0] = False
                    #is_live[channel_name][2].stop_bot()
                    #is_live[channel_name][2] = None
                if is_live[channel_name][0] != is_live[channel_name][1]:
                    message = da.live_alerts(channels[channel_name],
                                             channel_name,
                                             info)
                    # Log the message
                    with open(path_to_log, "a") as f:
                        print(f"{datetime.now().strftime(format='%H:%M:%S.%f, %d/%m/%Y %Z')}\n\t{message[0][0]}",
                              file=f,
                              end="\n\n")
                    # Show a notification
                    note = Notification(title=f"{channel_name} On Twitch",
                                        msg=message[0],
                                        duration="long",
                                        launch=f"twitch.tv/{channel_name}",
                                        app_id="LiveAlertDiscordBot")
                    note.show()
                    is_live[channel_name][1] = is_live[channel_name][0]
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
    if (not os.path.isfile("../Hidden/data.json")):
        print("data.json not found. Please create the file with the required authorization data.")
        exit(1)
    if (not os.path.isfile("channels.json")):
        with open("channels.json", "x") as f:
            json.dump({}, f, indent=4)
        print("channels.json not found. Please add channel data. to the newly created file")
    if (not os.path.isfile("log.txt")):
        with open("log.txt", "x") as f:
            print("Log file created.")
    if (not os.path.isfile("errors.txt")):
        with open("errors.txt", "x") as f:
            print("Errors-Log file created.")
    main("../Hidden/data.json",
         "channels.json",
         "log.txt",
         "errors.txt")
