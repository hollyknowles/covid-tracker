import discord
from secrets import get_token
import main

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(client.user, " has connected to Discord!")

@client.event
async def on_message(message):
    # Get the user to go in the format !new country date -> "!new us 12/09/21"
    if "!new" in message.content:
        content_list = message.content.split(" ")
        country = content_list[1]
        date = main.edit_date_format(content_list[2])
        new_cases = main.get_new_cases(await main.get_data(country, date))

        if new_cases is None:
            await message.channel.send("No data available for this country and date combination")
        else:
            await message.channel.send("There were " + str(new_cases) + " new cases of COVID-19 in " + str(country) + " on " + str(date))

TOKEN = get_token()
client.run(TOKEN)
