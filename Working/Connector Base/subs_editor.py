import json
import os
import misc
import twitchAPI

# Define the dictionary with natural language keys and functions
eventsub_listeners = {
    "Channel Update": lambda eventsub, creator_id: eventsub.listen_channel_update_v2(creator_id),
    "Follow": lambda eventsub, creator_id: eventsub.listen_channel_follow_v2(creator_id),
    "Subscribe": lambda eventsub, creator_id: eventsub.listen_channel_subscribe(creator_id),
    "Resubscribe": lambda eventsub, creator_id: eventsub.listen_channel_resubscribe(creator_id),
    "Cheer": lambda eventsub, creator_id: eventsub.listen_channel_cheer(creator_id),
    "Extension Install": lambda eventsub, creator_id: eventsub.listen_channel_extension_install(creator_id),
    "Extension Uninstall": lambda eventsub, creator_id: eventsub.listen_channel_extension_uninstall(creator_id),
    "Hype Train Begin": lambda eventsub, creator_id: eventsub.listen_channel_hype_train_begin(creator_id),
    "Hype Train Progress": lambda eventsub, creator_id: eventsub.listen_channel_hype_train_progress(creator_id),
    "Hype Train End": lambda eventsub, creator_id: eventsub.listen_channel_hype_train_end(creator_id),
    "Poll Begin": lambda eventsub, creator_id: eventsub.listen_channel_poll_begin(creator_id),
    "Poll Progress": lambda eventsub, creator_id: eventsub.listen_channel_poll_progress(creator_id),
    "Poll End": lambda eventsub, creator_id: eventsub.listen_channel_poll_end(creator_id),
    "Prediction Begin": lambda eventsub, creator_id: eventsub.listen_channel_prediction_begin(creator_id),
    "Prediction Progress": lambda eventsub, creator_id: eventsub.listen_channel_prediction_progress(creator_id),
    "Prediction Lock": lambda eventsub, creator_id: eventsub.listen_channel_prediction_lock(creator_id),
    "Prediction End": lambda eventsub, creator_id: eventsub.listen_channel_prediction_end(creator_id),
    "Goal Begin": lambda eventsub, creator_id: eventsub.listen_channel_goal_begin(creator_id),
    "Goal Progress": lambda eventsub, creator_id: eventsub.listen_channel_goal_progress(creator_id),
    "Goal End": lambda eventsub, creator_id: eventsub.listen_channel_goal_end(creator_id),
    "Raid": lambda eventsub, creator_id: eventsub.listen_channel_raid(creator_id),
    "Ban": lambda eventsub, creator_id: eventsub.listen_channel_ban(creator_id),
    "Unban": lambda eventsub, creator_id: eventsub.listen_channel_unban(creator_id),
    "Moderator Add": lambda eventsub, creator_id: eventsub.listen_channel_moderator_add(creator_id),
    "Moderator Remove": lambda eventsub, creator_id: eventsub.listen_channel_moderator_remove(creator_id),
    "Channel Points Custom Reward Add": lambda eventsub, creator_id: eventsub.listen_channel_points_custom_reward_add(creator_id),
    "Channel Points Custom Reward Update": lambda eventsub, creator_id: eventsub.listen_channel_points_custom_reward_update(creator_id),
    "Channel Points Custom Reward Remove": lambda eventsub, creator_id: eventsub.listen_channel_points_custom_reward_remove(creator_id),
    "Channel Points Custom Reward Redemptions Update": lambda eventsub, creator_id: eventsub.listen_channel_points_custom_reward_redemptions_update(creator_id),
    "Channel Points Custom Reward Redemption Add": lambda eventsub, creator_id: eventsub.listen_channel_points_custom_reward_redemption_add(creator_id),
    "Channel Points Custom Reward Redemption Update": lambda eventsub, creator_id: eventsub.listen_channel_points_custom_reward_redemption_update(creator_id),
    "Shield Mode Begin": lambda eventsub, creator_id: eventsub.listen_channel_shield_mode_begin(creator_id),
    "Shield Mode End": lambda eventsub, creator_id: eventsub.listen_channel_shield_mode_end(creator_id),
    "Shoutout Create": lambda eventsub, creator_id: eventsub.listen_channel_shoutout_create(creator_id),
    "Shoutout Receive": lambda eventsub, creator_id: eventsub.listen_channel_shoutout_receive(creator_id),
    "Charity Campaign Donate": lambda eventsub, creator_id: eventsub.listen_channel_charity_campaign_donate(creator_id),
    "Charity Campaign Start": lambda eventsub, creator_id: eventsub.listen_channel_charity_campaign_start(creator_id),
    "Charity Campaign Progress": lambda eventsub, creator_id: eventsub.listen_channel_charity_campaign_progress(creator_id),
    "Charity Campaign Stop": lambda eventsub, creator_id: eventsub.listen_channel_charity_campaign_stop(creator_id),
    "Charity Campaign End": lambda eventsub, creator_id: eventsub.listen_channel_charity_campaign_end(creator_id),
    "Charity Campaign Donation": lambda eventsub, creator_id: eventsub.listen_channel_charity_campaign_donation(creator_id),
    "Charity Campaign Donation Progress": lambda eventsub, creator_id: eventsub.listen_channel_charity_campaign_donation_progress(creator_id),
    "Charity Campaign Donation End": lambda eventsub, creator_id: eventsub.listen_channel_charity_campaign_donation_end()
}

def edit_subs():
    print("Editing Subscriptions...")
    print("This is the sub list editor. You can type 'help' for a list of commands.")
    with open("subs.json", "r") as f:
        subs = json.load(f)
    input("Press Enter to continue...")
    misc.clear_console()
    inp = input("Enter a command: ").lower().split()
    while inp[0] != "exit":
        if inp[0] == "help":
            print("Commands:")
            print("- add [sub] : Add a new subscription")
            print("- remove all : Remove all subscriptions")
            print("- remove [sub] : Remove a specific subscription")
            print("- list all - List all subscriptions")
            print("- list current - List the events you are subscribed to")
            print("- exit - Exit the editor")
        elif inp[0] == "add":
            if len(inp) < 2:
                print("Please enter a subscription name")
            else:
                if inp[1] in sublist:
                    subs.append(inp[1])
                    print(f"Added {inp[1]} to the subscription list")
        input("Press Enter to continue...")
        misc.clear_console()
        inp = input("Enter a command: ").lower().split()

edit_subs()