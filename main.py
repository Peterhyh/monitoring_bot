import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import pygame
# from tkinter import *

pygame.mixer.init()
pygame.mixer.music.load("notification_sound.mp3")


# window = Tk()
# window.title("Pokemon Monitor")
Black_Bolt_ETB = "https://www.target.com/p/pok-233-mon-scarlet-violet-s10-5-elite-trainer-box-2-trading-cards/-/A-94636862?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
Black_Bolt_Booster_Bundle = "https://www.target.com/p/pok-233-mon-scarlet-violet-s10-5-booster-bundle-box-trading-cards/-/A-94681770?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
Destined_Rivals_ETB = "https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-8212-destined-rivals-elite-trainer-box/-/A-94300069?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
Destined_Rivals_Booster_Bundle = "https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-8212-destined-rivals-booster-bundle/-/A-94300067?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
FF = "https://www.target.com/p/magic-the-gathering-final-fantasy-bundle-bl-trading-cards/-/A-94641041?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
CHECK_INTERVAL = 0.01

# tag = "button"
# # id = "addToCartButtonOrTextIdFor94636862"
# inStockMsg = "in stock!"
# item = Black_Bolt_ETB

# tag = "button"
# id="addToCartButtonOrTextIdFor94300067"

item = Destined_Rivals_ETB
plain_text = "Out of stock"
alertMsg = "Destined Rivals ETB in stock!"



def get_monitored_content(URL, text):
    #Connects to a website/server via the URL you provide
    #Requests data (like HTML, JSON, etc.) from that page
    #Returns a Response object, which contains the server's response (such as the page content, status code, headers, etc.).
    response = requests.get(URL)

    #parses the HTML content from the response.text using BeautifulSoup, turning it into a structured object you can easily navigate and search.
    #response.text: The raw HTML text returned from the website (via requests.get()).
    #'html.parser': Tells BeautifulSoup to use Python’s built-in HTML parser to interpret the page
    soup = BeautifulSoup(response.text, 'html.parser')

    #Target the specific element (e.g., a div with id="price")
    #Targeting Destined_Rivals_ETB notify me button
    element = soup.find(string=text)

    if element:
        return element.get_text(strip=True)
    else:
        return None  # Handle missing element gracefully
    

last_content = get_monitored_content(URL=item, text=plain_text)

while True:
    time.sleep(CHECK_INTERVAL)
    current_content = get_monitored_content(URL=item, text=plain_text)

    if current_content != last_content:
        pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy():
        #     time.sleep(0.1)
        print(f"{datetime.now()}: {alertMsg}")
        last_content = current_content
    else:
        continue
