from pystyle import Colors, Colorate, Center
import os
from discord_webhook import DiscordWebhook
import threading
import sys
import time

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(sec):
    time.sleep(sec)

print("")

print(Colorate.Horizontal(Colors.blue_to_green, "                     ██     ▀███▄   ▀███▀ ▄▄█▀▀▀█▄█▀███▀▀▀██▄ ▀███▀   ▀██▀███▀▀▀███ ▄▄█▀▀██▄ ▀███▀   ▀██▀ "))
print(Colorate.Horizontal(Colors.blue_to_green, "                    ▄██▄      ███▄    █ ▄██▀     ▀█  ██   ▀██▄  ███   ▄█   ██    ▀███▀    ▀██▄ ███▄  ▄█   "))
print(Colorate.Horizontal(Colors.blue_to_green, "                   ▄█▀██▄     █ ███   █ ██▀       ▀  ██   ▄██    ███ ▄█    ██   █ ██▀      ▀██  ▀██▄█▀    "))
print(Colorate.Horizontal(Colors.blue_to_green, "                  ▄█  ▀██     █  ▀██▄ █ ██           ███████      ████     ██▀▀██ ██        ██    ███     "))
print(Colorate.Horizontal(Colors.blue_to_green, "                  ████████    █   ▀██▄█ ██▄    ▀████ ██  ██▄       ██      ██   █ ██▄      ▄██  ▄█▀▀██▄   "))                                                                                           
print(Colorate.Horizontal(Colors.blue_to_green, "                 █▀      ██   █     ███ ▀██▄     ██  ██   ▀██▄     ██      ██     ▀██▄    ▄██▀ ▄█   ▀██▄  "))
print(Colorate.Horizontal(Colors.blue_to_green, "               ▄███▄   ▄████▄███▄    ██   ▀▀███████▄████▄ ▄███▄  ▄████▄  ▄████▄     ▀▀████▀▀ ▄██▄▄  ▄▄███▄"))                     

print("")

print(Colorate.Diagonal(Colors.blue_to_green, "                                                  Made by AngryFoxYT"))
print(Colorate.Diagonal(Colors.blue_to_green, "                                                Discord Webhook Spammer"))

print("")

print(Colorate.Diagonal(Colors.blue_to_green, "Enter the webhook url"))

webhookurl = input("")

clear()

print("")

print(Colorate.Horizontal(Colors.blue_to_green, "                     ██     ▀███▄   ▀███▀ ▄▄█▀▀▀█▄█▀███▀▀▀██▄ ▀███▀   ▀██▀███▀▀▀███ ▄▄█▀▀██▄ ▀███▀   ▀██▀ "))
print(Colorate.Horizontal(Colors.blue_to_green, "                    ▄██▄      ███▄    █ ▄██▀     ▀█  ██   ▀██▄  ███   ▄█   ██    ▀███▀    ▀██▄ ███▄  ▄█   "))
print(Colorate.Horizontal(Colors.blue_to_green, "                   ▄█▀██▄     █ ███   █ ██▀       ▀  ██   ▄██    ███ ▄█    ██   █ ██▀      ▀██  ▀██▄█▀    "))
print(Colorate.Horizontal(Colors.blue_to_green, "                  ▄█  ▀██     █  ▀██▄ █ ██           ███████      ████     ██▀▀██ ██        ██    ███     "))
print(Colorate.Horizontal(Colors.blue_to_green, "                  ████████    █   ▀██▄█ ██▄    ▀████ ██  ██▄       ██      ██   █ ██▄      ▄██  ▄█▀▀██▄   "))                                                                                           
print(Colorate.Horizontal(Colors.blue_to_green, "                 █▀      ██   █     ███ ▀██▄     ██  ██   ▀██▄     ██      ██     ▀██▄    ▄██▀ ▄█   ▀██▄  "))
print(Colorate.Horizontal(Colors.blue_to_green, "               ▄███▄   ▄████▄███▄    ██   ▀▀███████▄████▄ ▄███▄  ▄████▄  ▄████▄     ▀▀████▀▀ ▄██▄▄  ▄▄███▄"))                     

print("")

print(Colorate.Diagonal(Colors.blue_to_green, "                                                  Made by AngryFoxYT"))
print(Colorate.Diagonal(Colors.blue_to_green, "                                                Discord Webhook Spammer"))

print("")

print(Colorate.Diagonal(Colors.blue_to_green, "Enter the message that you want for the webhook to spam"))

msg = input()

clear()

print("")

print(Colorate.Horizontal(Colors.blue_to_green, "                     ██     ▀███▄   ▀███▀ ▄▄█▀▀▀█▄█▀███▀▀▀██▄ ▀███▀   ▀██▀███▀▀▀███ ▄▄█▀▀██▄ ▀███▀   ▀██▀ "))
print(Colorate.Horizontal(Colors.blue_to_green, "                    ▄██▄      ███▄    █ ▄██▀     ▀█  ██   ▀██▄  ███   ▄█   ██    ▀███▀    ▀██▄ ███▄  ▄█   "))
print(Colorate.Horizontal(Colors.blue_to_green, "                   ▄█▀██▄     █ ███   █ ██▀       ▀  ██   ▄██    ███ ▄█    ██   █ ██▀      ▀██  ▀██▄█▀    "))
print(Colorate.Horizontal(Colors.blue_to_green, "                  ▄█  ▀██     █  ▀██▄ █ ██           ███████      ████     ██▀▀██ ██        ██    ███     "))
print(Colorate.Horizontal(Colors.blue_to_green, "                  ████████    █   ▀██▄█ ██▄    ▀████ ██  ██▄       ██      ██   █ ██▄      ▄██  ▄█▀▀██▄   "))                                                                                           
print(Colorate.Horizontal(Colors.blue_to_green, "                 █▀      ██   █     ███ ▀██▄     ██  ██   ▀██▄     ██      ██     ▀██▄    ▄██▀ ▄█   ▀██▄  "))
print(Colorate.Horizontal(Colors.blue_to_green, "               ▄███▄   ▄████▄███▄    ██   ▀▀███████▄████▄ ▄███▄  ▄████▄  ▄████▄     ▀▀████▀▀ ▄██▄▄  ▄▄███▄"))                     

print("")

print(Colorate.Diagonal(Colors.blue_to_green, "                                                  Made by AngryFoxYT"))
print(Colorate.Diagonal(Colors.blue_to_green, "                                                Discord Webhook Spammer"))

def spamwebhook():
    try:
        print("")
        print(Colorate.Diagonal(Colors.blue_to_green, "                                                   Sending messages.."))
        while True:
            webhook = DiscordWebhook(url=webhookurl, content=msg)
            webhook.execute()
            wait(0.2)
    except:
        print(Colorate.Diagonal(Colors.blue_to_green, "Error! The webhook doesnt exist!"))
        print(Colorate.Diagonal(Colors.blue_to_green, "Press enter to continue"))
        input()
        sys.exit()

spamwebhookthread = threading.Thread(target=spamwebhook)
spamwebhookthread.start()

print("")
