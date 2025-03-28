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

import json
import requests
import os
import base64

def get_subdirs(directory):
    subdirs = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    return subdirs

def get_github_file_content(owner, repo, path, branch='main', token=None):
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        content = response.json()['content']
        return base64.b64decode(content).decode('utf-8')
    else:
        return None

if __name__ == "__main__":
    print("Initializing required directories...")
    if not os.path.isdir("Logs") or not os.path.isfile("Logs/log.txt"):
        with open("Logs/log.txt", "x") as f:
            f.write("")
        print("Log file created.")
    if not os.path.isfile("Logs/errors.txt"):
        with open("Logs/errors.txt", "x") as f:
            f.write("")
        print("Error log file created.")
    if not os.path.isdir("Data") or not os.path.isfile("Data/channels.json"):
        with open("Data/channels.json", "x") as f:
            json.dump({"CHANNEL-1": None, "CHANNEL-2": "URL-1", "CHANNEL-3": ["URL-1", "URL-2", "URL-3"]}, f, indent=4)
        print("Channel data file created.")
    if not os.path.isfile("Data/info.json"):
        with open("Data/info.json", "x") as f:
            json.dump({"additional-urls": []}, f, indent=4)
        print("Info data file created.")
    if not os.path.isfile("Required/auth.json"):
        with open("Required/auth.json", "x") as f:
            json.dump(["YOUR-CLIENT-ID", "YOUR-CLIENT-SECRET"], f, indent=4)
        print("Authorization data file created.")
    print("Required initialization complete.")
    print("Initializing legal files...")
    if not os.path.isfile("LICENSE"):
        with open("LICENSE", "x") as f:
            f.write(get_github_file_content("EclipseShadow55", "Twitch-Live-Alerts", "LICENSE"))
        print("LICENSE file created.")
    if not os.path.isfile("NOTICE"):
        with open("NOTICE", "x") as f:
            f.write(get_github_file_content("EclipseShadow55", "Twitch-Live-Alerts", "NOTICE"))
        print("NOTICE file created.")
    if not os.path.isfile("README.md"):
        with open("README.md", "x") as f:
            f.write(get_github_file_content("EclipseShadow55", "Twitch-Live-Alerts", "README.md"))
        print("README file created.")
    if not os.path.isdir("Legal") or not os.path.isdir("Legal/Requests") or not os.path.isfile("Legal/Requests/LICENSE"):
        with open("Legal/Requests/LICENSE", "x") as f:
            f.write(get_github_file_content("EclipseShadow55", "Twitch-Live-Alerts", "Legal/Requests/LICENSE"))
        print("Requests license file created.")
    if not os.path.isdir("Legal/Winotify"):
        with open("Legal/Winotify/LICENSE", "x") as f:
            f.write(get_github_file_content("EclipseShadow55", "Twitch-Live-Alerts", "Legal/Winotify/LICENSE"))
    if not os.path.isfile("Legal/Winotify/CREDITS.md"):
        with open("Legal/Winotify/CREDITS.md", "x") as f:
            f.write(get_github_file_content("EclipseShadow55", "Twitch-Live-Alerts", "Legal/Winotify/CREDITS.md"))
    if not os.path.isfile("Legal/Requests/NOTICE"):
        with open("Legal/Requests/NOTICE", "x") as f:
            f.write(get_github_file_content("EclipseShadow55", "Twitch-Live-Alerts", "Legal/Requests/NOTICE"))
    if not os.path.isfile("Legal/Reqeusts/CREDITS.rst"):
        with open("Legal/Requests/CREDITS.rst", "x") as f:
            f.write(get_github_file_content("EclipseShadow55", "Twitch-Live-Alerts", "Legal/Requests/CREDITS.rst"))
    print("Legal files initialized.")
    if input("Would you like to see the setup instructions now? (y/n): ").lower()[0] == "y":
        if os.path.isfile("instructions.py"):
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            os.system("python instructions.py")
        elif os.path.isfile("instructions.exe"):
            os.chdir(os.path.dirname(os.path.abspath(__file__)))
            os.system("instructions.exe")
        else:
            print("Instructions not found.")
            print("You can find the instructions in the README.md file.")