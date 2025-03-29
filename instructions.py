import os

stuff = [
    "Step 0: Download the latest version of the program from the GitHub repository.",
    ["Step 1: Create a new directory for the program."],
    ["Step 2: Move all files to the new directory."],
    ["Step 3: Run init.py to initialize the required directories and files if you haven't already." if __file__[__file__.rfind("."):] == ".py" else "Step 3: Run init.exe to initialize the required directories and files if you haven't already"],
    ["Step 4: Open the 'channels.json' file that is in the 'Data' directory in a text editor, and fill out all the channels you want to monitor in these formats:",
     "\t\"CHANNEL-NAME\": null",
     "\t\"CHANNEL-NAME\": \"URL\"",
     "\t\"CHANNEL-NAME\": [\"URL1\", \"URL2\"], \"URL3\"]"
     "For the channel name, use their twitch username",
     "And for the url, use a webhook from a discord channel (you can follow this tutorial to get the webhook url: https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks"],
    ["Step 5: Open the 'auth.json' file in the 'Required' directory in a text editor, and fill out the required authorization data in this format:",
     "\t[\"TWITCH-CLIENT-ID\", \"TWITCH-CLIENT-SECRET\"]"],
    ["\tStep 5.1: To get the client id and client secret, you need to first go to https://dev.twitch.tv"],
    ["\tStep 5.2: Then you need to log in with twitch, then click on 'Your Console' in the top right"],
    ["\tStep 5.3: Then click on 'Register Your Application'"],
    ["\tStep 5.4: Start with filling out the name. You can call it whatever you want, but I recommend calling it Twitch-Live-Alerts"],
    ["\tStep 5.5: Then fill out the OAuth Redirect URL. Use 'http://localhost' for this, since we won't be using this feature"],
    ["\tStep 5.6: Then fill out the Category. I recommend using 'Other' for this"],
    ["\tStep 5.7: Then click 'I'm not a robot' and then click 'Create'"],
    ["\tStep 5.8: Then you will be taken to the 'Manage Your Applications' page"],
    ["\tStep 5.9: Click the manage button on the application you just created"],
    ["\tStep 5.10: You will see a Client ID. Copy this and paste it into the first spot in the 'auth.json' file"],
    ["\tStep 5.11: Then click 'New Secret' to generate a client secret, and click 'Ok' in the pop up that appears"],
    ["\tStep 5.12: Then you will see a Client Secret. Copy this and paste it into the second spot in the 'auth.json' file",
     "\t\tMake sure to keep this secret, as it is used to authenticate the program with twitch"],
    ["\tStep 5.13: Then click 'Save' at the bottom of the page"],
    ["\tStep 5.14: And you are done with the authorization data!"],
    ["Step 6: Open the 'info.json' file that is in the 'Data' directory in a text editor, and fill out any additional URLs you want to post to alerts to in this format:",
     "\t{\"additional-urls\": [\"URL1\", \"URL2\"]}",
     "These are just more discord webhooks that you want to post alerts to, but these ones will post alerts for every streamer on the list"],
    ["Step 7: Run main.pyw to start monitoring the channels.",
     "If you want to run the program with special settings, you can do the following:"],
    ["\tStep 7.1: Open the command prompt by hitting the windows key and typing 'cmd' into the text box"],
    ["\tStep 7.2: Then navigate to the directory where the program is located by typing 'cd ' followed by the path to the directory"],
    ["\tStep 7.3: Then type 'python main.pyw' followed by any of the following arguments:" if __file__[__file__.rfind("."):] == ".py" else "\tStep 7.3: Then type 'main.exe' followed by any of the following flags:",
     "\t\t'--no-notif': This will disable Windows notifications for when a streamer goes live or offline, so only the discord channels will get the alert",
     "\t\t'--no-offline': This will disable alerts for when a streamer goes offline",
     "\t\t'--start-ignore': This will stop the program from posting an alert for any streamer that is live when the program is started, so only streamers that go live after the program is started will have an alert posted about them"],
    ["And you are done! The program will now monitor the channels you have set up and post alerts to the discord channels you have set up.",
     "Note: It is vital that you keep all the files in the given file structure (so both 'channels.json' and 'info.json' in a director called 'Data'), the program will not function otherwise."]
]

if __name__ == "__main__":
    i = 0
    while i < len(stuff):
        os.system("cls")
        if i == 0:
            if not os.path.isfile("main.pyw") and not os.path.isfile("main.exe"):
                print(stuff[0])
                inp = input(f"Press Enter to continue, 'back' to go back to the last step, or 'exit' to exit the instructions: ")
            else:
                inp = ""
        else:
            for j in stuff[i]:
                print(j)
            inp = input(f"Press Enter to continue, 'back' to go back to the last step, or 'exit' to exit the instructions: ")
        if inp.lower() == "exit":
            exit(0)
        elif inp.lower() == "back":
            i -= 1
        else:
            i += 1