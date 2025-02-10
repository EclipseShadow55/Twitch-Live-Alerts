# Twitch-Live-Alerts
A Twitch Live Alerts Bot that sends a message to a Discord channel when a streamer goes live.
Uses Twitch Endpoints API, Discord Webhooks, the Requests library, and the Winotify library.
## Table of Contents
- [Installation](#installation)
- [Licences and Credits](#licenses-and-credits)
## Installation
### With Python (3.6+)
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
## Licenses and Credits
### Twitch API
- [Twitch Developers](https://dev.twitch.tv/docs/api/)
### Discord Webhooks
- [Discord Developers](https://discord.com/developers/docs/resources/webhook)
### Requests Library
- In the `Licenses-And-Credits/Requests` folder
### Winotify Library
- In the `Licenses-And-Credits/Winotify` folder