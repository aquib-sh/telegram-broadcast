import asyncio
from telethon import TelegramClient
import config
from reader import CSVReader
from reader import Message
from creds import Credentials

# define some global variables
SUCCESS = True
FAILURE = False

# get API key and hash
creds = Credentials(config.API_KEYS_FILE)
API_ID = creds.get_api_key()
API_HASH = creds.get_api_hash()

csv_reader = CSVReader(config.INPUT_FILE)
csv_reader.load()

message = Message(config.MESSAGE_FILE).get() # msg to send

async def perform():
    async with TelegramClient('session1', API_ID, API_HASH) as client:
        for row in csv_reader.get_row():
            _, username, _ = row
            user = await client.get_entity(username)
            await client.send_message(user, message)
            print(f"[+] sent message to {username}")

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(perform())
    loop.close()

if __name__ == "__main__":
    main()    