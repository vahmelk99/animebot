#!/usr/bin/python3

from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser
from telethon.errors.rpcerrorlist import PeerFloodError
from telethon.tl.types import DocumentAttributeVideo
import sys
import csv
import random
import time
import argparse
def hor(file_path):
    api_id = 3610504 #Must change
    api_hash = '2d635b85550a19596f4efa68c3cf21d8' #Must change
    phone = '+37494178007' #Must change
    client = TelegramClient(phone, api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Enter the code: '))
    user = {}
    user['username'] = 'downanimebot' #Must change
    user['id'] = 1634518644 #Must change
    user['access_hash'] = int('-6392661706151905964') #Must change
    user['name'] = 'Anime Bot'
    receiver = InputPeerUser(user['id'], user['access_hash'])
    try:
        print("Sending Video to:", user['name'])
        client.send_file(receiver, file_path, caption=file_path, attributes=(DocumentAttributeVideo(0, 0, 0),))
        print('done')
    except Exception as e:
        print("Error:", e)
    client.disconnect()
    print("Done. Message sent to all users.")
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=str, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
args = parser.parse_args()
file_path = args.accumulate(args.integers)
hor(file_path)

