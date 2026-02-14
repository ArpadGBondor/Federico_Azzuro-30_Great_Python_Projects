from discord import Intents, Client, Message
from chat import chat_bot
from credentials import DISCORD_BOT_TOKEN


def run_bot(token: str):
    intents = Intents.default()
    intents.message_content = True

    client = Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")

    @client.event
    async def on_message(message: Message):
        if message.author == client.user:
            return

        # Check if the bot was mentioned
        if client.user in message.mentions:
            # Remove the mention from the message content
            content = message.content.replace(f"<@{client.user.id}>", "").strip()

            if content:
                print(f'({message.channel}) {message.author}: "{content}"')
                response: str = chat_bot(content)
                await message.channel.send(response)
            else:
                print(
                    "!!! Could not read the message, make sure you have intents enabled !!!"
                )
        else:
            # Optionally, ignore messages without mentions
            return

    client.run(token=token)


if __name__ == "__main__":
    run_bot(DISCORD_BOT_TOKEN)
