import os

step7_3 = "Step 7.3: Then type 'python twitch_live_alerts.py' followed by any of the following arguments:" if not os.path.isfile("twitch_live_alerts.exe") else "Step 7.3: Then type 'twitch_live_alerts.exe' followed by any of the following flags:"
step7 = "Step 7: Run twitch_live_alerts.py to start monitoring the channels." if not os.path.isfile("twitch_live_alerts.exe") else "Step 7: Run twitch_live_alerts.exe to start monitoring the channels."
step3 = "Step 3: Run init.py if you haven't already." if not os.path.isfile("init.exe") else "Step 3: Run init.exe if you haven't already"
stuff = [
    "Step 0: Download the latest version of the program from the GitHub repository.",
    ["Step 1: Create a new directory for the program, preferably somewhere permanent like documents or desktop."],
    ["Step 2: Move all files to the new directory."],
    [step3],
    ["Step 4: Open the 'channels.json' file that is in the 'Data' directory in a text editor, and fill out all the channels you want to monitor in any of these formats:",
     "",
     "{",
     "\t\"STREAMER-NAME-1\": [\"DISCORD-WEBHOOK-5\"],",
     "\t\"STREAMER-NAME-2\": [\"DISCORD-WEBHOOK-2\", \"DISCORD-WEBHOOK-3\"], \"DISCORD-WEBHOOK-4\"]",
     "}",
     "",
     "For the channel name, use their twitch username",
     "To get the discord webhook url, you can follow this tutorial: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks",
     "Make sure that the file starts with '{' and ends with '}', make sure that each item (streamer name or discord url) has quotation marks around it, and make sure to separate each entry with a comma, an entry being a streamer name and their discord webhooks",
     "So a valid file might look like this:",
     "",
     "{",
     "\t\"eshadow55vt\": [\"https://discord.com/api/webhooks/123456789012345678/abcdefghijklmnopqrstuvwxyz\", \"https://discord.com/api/webhooks/876543210987654321/ABCDEFGHIJKLMNOPQRSTUVWXYZ\"],",
     "\t\"nyxlitten\": [\"https://discord.com/api/webhooks/123456789012345678/abcdefghijklmnopqrstuvwxyz\"],",
     "\t\"anotherstreamer\": [\"https://discord.com/api/webhooks/123456789012345678/ABCDEFGHIJKLMNOPQRSTUVWXYZ\"]",
     "}",
     ""],
    ["Step 5: Open the 'auth.json' file in the 'Required' directory in a text editor, and fill out the required authorization data in this format:",
     "\t[\"TWITCH-CLIENT-ID\", \"TWITCH-CLIENT-SECRET\"]",
     "The next steps will tell you how to get this information"],
    ["Step 5.1: To get the client id and client secret, you need to first go to https://dev.twitch.tv"],
    ["Step 5.2: Then you need to log in with twitch, then click on 'Your Console' in the top right"],
    ["Step 5.3: Then click on 'Register Your Application'"],
    ["Step 5.4: Start with filling out the name. You can call it whatever you want, but I recommend calling it Twitch-Live-Alerts"],
    ["Step 5.5: Then fill out the OAuth Redirect URL. Use 'http://localhost' for this, since we won't be using this feature"],
    ["Step 5.6: Then fill out the Category. I recommend using 'Other' for this"],
    ["Step 5.7: Then click 'I'm not a robot' and then click 'Create'"],
    ["Step 5.8: Then you will be taken to the 'Manage Your Applications' page"],
    ["Step 5.9: Click the manage button on the application you just created"],
    ["Step 5.10: You will see a Client ID. Copy this and paste it into the first spot in the 'auth.json' file"],
    ["Step 5.11: Then click 'New Secret' to generate a client secret, and click 'Ok' in the pop up that appears"],
    ["Step 5.12: Then you will see a Client Secret. Copy this and paste it into the second spot in the 'auth.json' file",
     "\tMake sure to keep this secret, as it is used to authenticate the program with twitch"],
    ["Step 5.13: Then click 'Save' at the bottom of the page"],
    ["Step 5.14: And you are done with the authorization data!"],
    ["Step 6: Open the 'info.json' file that is in the 'Data' directory in a text editor, and fill out any additional URLs you want to post to alerts to in this format:",
     "\t{\"additional-urls\": [\"DISCORD-WEBHOOK-1\", \"DISCORD-WEBHOOK-2\"]}",
     "These are just more discord webhooks that you want to post alerts to, but these ones will post alerts for every streamer on the list",
     "If you don't have any additional urls, just leave it"],
    [step7,
     "If you want to run the program with special settings, you can do the following:"],
    ["Step 7.1: Open the command prompt by hitting the windows key and typing 'cmd' and pressing enter"],
    ["Step 7.2: Then navigate to the directory where the program is located by typing 'cd ' followed by the path to the directory",
     "\tYou can find this by clicking on the address bar in the file explorer while you in the directory, and copying the path"],
    [step7_3,
     "\t'--no-notif': This will disable Windows notifications for when a streamer goes live or offline, so only the discord channels will get the alert",
     "\t'--no-offline': This will disable alerts for when a streamer goes offline",
     "\t'--start-ignore': This will stop the program from posting an alert for any streamer that is live when the program is started, so only streamers that go live after the program is started will have an alert posted about them"],
    ["And you are done! The program will now monitor the channels you have set up and post alerts to the discord channels you have set up.",
     "Note: It is vital that you keep all the files in the given file structure (so both 'channels.json' and 'info.json' in a directory called 'Data', etc.), the program will not function otherwise."]
]

if __name__ == "__main__":
    i = 0
    while i < len(stuff):
        os.system("cls")
        if i == 0:
            if not os.path.isfile("twitch_live_alerts.py") and not os.path.isfile("twitch_live_alerts.exe"):
                print(stuff[0])
                inp = input(f"Press Enter to continue, 'back' to go back to the last step, or 'exit' to exit the instructions: ")
            else:
                inp = ""
        else:
            for j in stuff[i]:
                print(j)
            inp = input(f"Press Enter to continue, 'back' to go back to the last step, or 'exit' to exit the instructions: ")
        if inp.lower() == "exit":
            break
        elif inp.lower() == "back":
            i -= 1
        else:
            i += 1