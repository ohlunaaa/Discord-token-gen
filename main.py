import requests
import random
import string
import time
from playwright.sync_api import sync_playwright


genned = 0

class data:
    def name():
        r=requests.get('https://story-shack-cdn-v2.glitch.me/generators/username-generator?')
        return r.json()["data"]["name"]


chars_after_at = 7
letters_list = [string.digits, string.ascii_lowercase, string.ascii_uppercase]
letters_list_to_str = "".join(letters_list)
email_format = "@gmail.com"
email_generated = "".join(random.choices(letters_list_to_str, k=chars_after_at)) + email_format

chars_after_at1 = 6
letters_list1 = [string.digits, string.ascii_lowercase, string.ascii_uppercase]
letters_list_to_str1 = "".join(letters_list)
password = "".join(random.choices(letters_list_to_str, k=chars_after_at)) + email_format




def gen():
    global genned
    username = data.name()
    proxy = random.choice(open("proxies.txt","r").read().splitlines())
    with sync_playwright() as p:
        for browser_type in [p.chromium]:
            browser = browser_type.launch(headless=False,proxy={"server": f'http://{proxy}'})
            xd = browser.new_context()
            page = xd.new_page()
            try:
                page.goto('https://discord.com/register')
                time.sleep(1)
                page.type("#app-mount > div.app-3xd6d0 > div > div > div > form > div > div > div:nth-child(1) > div > input", email_generated)
                time.sleep(.3)
                page.type("#app-mount > div.app-3xd6d0 > div > div > div > form > div > div > div:nth-child(2) > div > input", username)
                time.sleep(.3)
                page.type("#app-mount > div.app-3xd6d0 > div > div > div > form > div > div > div:nth-child(3) > div > input", password)
                time.sleep(.3)
                page.type("#react-select-2-input", "January\n")
                time.sleep(.3)
                page.type("#react-select-3-input", "1\n")
                time.sleep(.3)
                page.type("#react-select-4-input", "2000\n\n")
                page.wait_for_selector("iframe")
                time.sleep(3)
                page.click("iframe")
                time.sleep(30)
                try:
                    token = page.evaluate("""
                    (_ => {
                    const win = window.open();
                    const token = win.localStorage.token;
                    win.close();
                    return token;
                    })();
                    """)
                except:
                    print("Failed")

                token2 = str(token)
                token3 = token2.replace('"',"")
                file = open("accounts.txt","a")
                file.write(f"{token3}:{email_generated}:{username}:{password}\n")
                try:
                    file = open("tokens.txt","a")
                    file.write(f"{token3}\n")
                except:
                    return
                genned += 1
                print(f"Done {genned}")
                page.close()
            except Exception as e:
                print(e)
while 2:
    gen()