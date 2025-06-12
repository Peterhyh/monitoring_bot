import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
# from tkinter import *
import hashlib
import smtplib

# window = Tk()
# window.title("Pokemon Monitor")
Black_Bolt_ETB = "https://www.target.com/p/pok-233-mon-scarlet-violet-s10-5-elite-trainer-box-2-trading-cards/-/A-94636862?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
Black_Bolt_Booster_Bundle = "https://www.target.com/p/pok-233-mon-scarlet-violet-s10-5-booster-bundle-box-trading-cards/-/A-94681770?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
Destined_Rivals_ETB = "https://www.target.com/p/pok-233-mon-trading-card-game-scarlet-38-violet-8212-destined-rivals-elite-trainer-box/-/A-94300069?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
FF = "https://www.target.com/p/magic-the-gathering-final-fantasy-commander-deck-2-trading-cards/-/A-94641038?clkid=8985bc2eN40d511f0a9549f724edc96ad&cpng=&lnm=81938&afid=Mavely&ref=tgt_adv_xasd0002"
CHECK_INTERVAL = 0.2


def get_monitored_content():
    response = requests.get(Destined_Rivals_ETB)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Target the specific element (e.g., a div with id="price")
    #Targeting Destined_Rivals_ETB notify me button
    element = soup.find("button", id="notifyMe")

    if element:
        return element.get_text(strip=True)
    else:
        return None  # Handle missing element gracefully
    

last_content = get_monitored_content()

while True:
    time.sleep(CHECK_INTERVAL)
    current_content = get_monitored_content()

    if current_content != last_content:
        print(f"{datetime.now()} [Change Detected] Old: {last_content} → New: {current_content}")
        last_content = current_content
    else:
        print(f"{datetime.now()} ...")