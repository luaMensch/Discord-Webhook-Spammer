from discord_webhook import DiscordWebhook
import time

webzn = input("Webhook Url : ")
msg = input("Message : ")
username = input("Set username of Webhook to : ")
webhook = DiscordWebhook(url=webzn, content=msg ,username = username, avatar_url="https://cdn.discordapp.com/embed/avatars/0.png")
while True:
    response = webhook.execute()
    time.sleep(0.5)
    print(f"+ Message Sent!")
