import asyncio
import os
import discord
import openai
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
OPENAI_KEY = os.getenv('OPENAI_KEY')

# Set up OpenAI API client
openai.api_key = OPENAI_KEY

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Check if bot is mentioned
    if client.user in message.mentions:
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=f'{message.content}',
            max_tokens=2048,
            temperature=0.5
        )

        async with message.channel.typing():
            await asyncio.sleep(1)
            await message.channel.send('pong')

        await message.channel.send(response.choices[0].text)


# Start the bot
client.run(TOKEN)




