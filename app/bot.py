import datetime
import os

import requests
from dotenv import load_dotenv

load_dotenv()

header = {
    'authorization': os.getenv('DISCORD_TOKEN')
}

addresses = os.getenv('WALLET_ADDRESS')

if __name__ == '__main__':
    for a in addresses.split(','):
        r = requests.post(
            url=f"https://discord.com/api/v9/channels/{os.getenv('CHANNEL_ID')}/messages",
            data={
                'content': a
            },
            headers=header
        )
        print(r, datetime.datetime.now())
