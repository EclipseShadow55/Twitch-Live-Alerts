# Twitch-Live-Alerts v0.5.0 (Unstable)
A Twitch Live Alerts Bot that sends a message to a Discord channel when a streamer goes live.
Uses Twitch Endpoints API, Discord Webhooks, the Requests library, and the Winotify library.
## Table of Contents
- [Installation](#installation)
- [Licences and Credits](#licenses-and-credits)
## Installation and Usage
### With Python (3.6+) (Windows Only)
(Note: This guide assumes you are using windows, but the process should be similar on other operating systems)
1. Create a venv or conda environment, so that the packages don't conflict with other projects. If you don't know how to do this, follow [this guide](https://python.land/virtual-environments/virtualenv) for venv or [this guide](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/) for conda.
2. Install Python 3.6 or higher from [here](https://www.python.org/downloads/). 
3. Clone the repository into a folder (I recommend calling it `Twitch-Live-Alerts`) using `git clone` or cloning it directly from [the GitHub page](https://github.com/EclipseShadow55/Twitch-Live-Alerts/). 
4. Open the command prompt or any terminal, navigate inside the folder you just cloned using `cd path\to\the\folder`, and install the required packages using `pip install -r requirements.txt` or `conda install --file environment.yml` if you're using conda.
5. Navigate inside the `Data` folder using `cd Data`. 
6. Create a file named `channels.json` and following the structure of `example-channels.json`, fill it with your own data. (You can follow [this tutorial](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to create webhooks for discord channels)
7. Create a file named `info.json` and following the structure of `example-info.json` or `example2-info.json`, and fill it with your own data. 
8. Go to the [Twitch Dev Portal](https://dev.twitch.tv/console/apps) and create a new application. Copy the Client ID and Client Secret into the `data.json` file. 
9. Navigate back into the main folder, then into the `Required` folder. 
10. Create a file named `data.json` and following the structure of `example-data.json`, fill it with your own data. 
11. Finally, navigate back to the main folder and run the `main.py` file using `python main.py`.
### With Binaries (Windows Only)
- **Step 0:** Download the latest version of the program from the GitHub repository.
- **Step 1:** Create a new directory for the program.
- **Step 2:** Move all files to the new directory.
- **Step 3:** Run `init.exe` to initialize the required directories and files if you haven't already.
- **Step 4:** Open the `channels.json` file that is in the `Data` directory in a text editor, and fill out all the channels you want to monitor in these formats:
  - `"CHANNEL-NAME": null`
  - `"CHANNEL-NAME": "URL"`
  - `"CHANNEL-NAME": ["URL1", "URL2"], "URL3"`
  - For the channel name, use their Twitch username.
  - And for the URL, use a webhook from a Discord channel (you can follow [this tutorial](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks) to get the webhook URL).
- **Step 5:** Open the `auth.json` file in the `Required` directory in a text editor, and fill out the required authorization data in this format:
  - `["TWITCH-CLIENT-ID", "TWITCH-CLIENT-SECRET"]`
- **Step 5.1:** To get the client ID and client secret, you need to first go to [Twitch Dev](https://dev.twitch.tv).
- **Step 5.2:** Then you need to log in with Twitch, then click on `Your Console` in the top right.
- **Step 5.3:** Then click on `Register Your Application`.
- **Step 5.4:** Start with filling out the name. You can call it whatever you want, but I recommend calling it Twitch-Live-Alerts.
- **Step 5.5:** Then fill out the OAuth Redirect URL. Use `http://localhost` for this, since we won't be using this feature.
- **Step 5.6:** Then fill out the Category. I recommend using `Other` for this.
- **Step 5.7:** Then click `I'm not a robot` and then click `Create`.
- **Step 5.8:** Then you will be taken to the `Manage Your Applications` page.
- **Step 5.9:** Click the manage button on the application you just created.
- **Step 5.10:** You will see a Client ID. Copy this and paste it into the first spot in the `auth.json` file.
- **Step 5.11:** Then click `New Secret` to generate a client secret, and click `Ok` in the pop-up that appears.
- **Step 5.12:** Then you will see a Client Secret. Copy this and paste it into the second spot in the `auth.json` file.
  - Make sure to keep this secret, as it is used to authenticate the program with Twitch.
- **Step 5.13:** Then click `Save` at the bottom of the page.
- **Step 5.14:** And you are done with the authorization data!
- **Step 6:** Open the `info.json` file that is in the `Data` directory in a text editor, and fill out any additional URLs you want to post alerts to in this format:
  - `{"additional-urls": ["URL1", "URL2"]}`
  - These are just more Discord webhooks that you want to post alerts to, but these ones will post alerts for every streamer on the list.
- **Step 7:** Run `twitch_live_alerts.exe` to start monitoring the channels.
  - If you want to run the program with special settings, you can do the following:
- **Step 7.1:** Open the command prompt by hitting the Windows key and typing `cmd` and pressing enter.
- **Step 7.2:** Then navigate to the directory where the program is located by typing `cd ` followed by the path to the directory.
  - You can find this by clicking on the address bar in the file explorer while you are in the directory, and copying the path.
- **Step 7.3:** Then type `twitch_live_alerts.exe` followed by any of the following arguments:
  - `--no-notif`: This will disable Windows notifications for when a streamer goes live or offline, so only the Discord channels will get the alert.
  - `--no-offline`: This will disable alerts for when a streamer goes offline.
  - `--start-ignore`: This will stop the program from posting an alert for any streamer that is live when the program is started, so only streamers that go live after the program is started will have an alert posted about them.
- And you are done! The program will now monitor the channels you have set up and post alerts to the Discord channels you have set up.
  - Note: It is vital that you keep all the files in the given file structure (so both `channels.json` and `info.json` in a directory called `Data`, etc.), the program will not function otherwise.
## Moving Forward
- Make it more user-friendly and accessible for non-programmers
  - Maybe add a UI
  - Add an installer for the release build
    - Maybe have it check for updates on startup
- Add compatibility for Linux and macOS
## Licenses and Credits
### Twitch API
- [Twitch Developers](https://dev.twitch.tv/docs/api/)
### Discord Webhooks
- [Discord Developers](https://discord.com/developers/docs/resources/webhook)
### Requests Library
- In the `Licenses-And-Credits/Requests` folder
### Winotify Library
- In the `Licenses-And-Credits/Winotify` folder