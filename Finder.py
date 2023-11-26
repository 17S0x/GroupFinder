import requests
from discord_webhook import DiscordWebhook

ROBLOX_API_URL = "https://groups.roblox.com/v1/groups/list?public=true&sortOrder=Desc&limit=100"
DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

def find_ownerless_groups():
    response = requests.get(ROBLOX_API_URL)

    if response.status_code == 200:
        groups = response.json()["data"]
        ownerless_groups = [group for group in groups if not group["owner"]]
        return ownerless_groups
    else:
        print("Error:", response.status_code)
        return None

def send_to_discord(ownerless_groups):
    if not ownerless_groups:
        print("No ownerless groups to send.")
        return

    webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL, content="Ownerless Groups:")

    for group in ownerless_groups:
        group_id = group["id"]
        group_name = group["name"]
        group_link = f"https://www.roblox.com/groups/%7Bgroup_id%7D"

        embed = {
            "title": f"Group ID: {group_id}",
            "description": f"Name: {group_name}\n[Group Link]({group_link})",
            "color": 16711680  # Red color
        }

        webhook.add_embed(embed)

    webhook.execute()

if name == "main":
    ownerless_groups = find_ownerless_groups()

    if ownerless_groups:
        send_to_discord(ownerless_groups)
    else:
        print("Failed to retrieve ownerless groups.")
