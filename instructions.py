import os

stuff = [
    "Step 0: Download the latest version of the program from the GitHub repository.",
    ["Step 1: Create a new directory for the program."],
    ["Step 2: Move all files to the new directory."],
    ["Step 3: Run init.py to initialize the required directories and files." if __file__[__file__.rfind("."):] == ".py" else "Step 3: Run init.exe to initialize the required directories and files."],
    ["Step 4: Open the 'channels.json' file that is in the 'Data' directory in a text editor, and fill out all the channels you want to monitor in these formats:",
     "\t\"CHANNEL-NAME\": null",
     "\t\"CHANNEL-NAME\": \"URL\"",
     "\t\"CHANNEL-NAME\": [\"URL1\", \"URL2\"], \"URL3\"]"],
    ["Step 5: Open the 'auth.json' file in the 'Required' directory in a text editor, and fill out the required authorization data in this format:",
     "\t[\"TWITCH-CLIENT-ID\", \"TWITCH-CLIENT-SECRET\"]"],
    ["Step 6: Open the 'info.json' file that is in the 'Data' directory in a text editor, and fill out any additional URLs you want to post to alerts to in this format:",
     "\t{\"additional-urls\": [\"URL1\", \"URL2\"]}"],
    ["Step 7: Run main.pyw to start monitoring the channels."]
]

if __name__ == "__main__":
    i = 0
    while i < len(stuff):
        if i == 0:
            if not os.path.isfile("main.pyw") or not os.path.isfile("main.exe"):
                print(stuff[0])
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