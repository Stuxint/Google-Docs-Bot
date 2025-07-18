import undetected_chromedriver as uc
from humancursor import WebCursor
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import google.generativeai as genai
import time

#-------------PROMPT TO CREATE DOCUMENT----------------


prompt = """
Here, tell AI what u want it to make.
"""


genai.configure(api_key="Your API Key")
model = genai.GenerativeModel('gemini-2.0-flash')
answer = model.generate_content([prompt], stream=False)
document = answer.text.strip()


#----------GOES TO GMAIL AND SIGNS IN-------------------
web = uc.Chrome()
web.get("https://mail.google.com/mail/u/0/#sent")

usern = web.find_element('xpath', '//*[@id="identifierId"]')
usern.send_keys('Your Gmail Address')
usern.send_keys(Keys.ENTER)

passw= WebDriverWait(web, 10).until(
                EC.presence_of_element_located(('xpath', '//*[@id="password"]/div[1]/div/div[1]/input'))
            )
passw.send_keys('Your Gmail Password')
passw.send_keys(Keys.ENTER)

#----------GOES TO DOCS AND MAKES DOCUMENT-------------------
time.sleep(2)
actions = ActionChains(web)
actions.key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()
web.switch_to.window(web.window_handles[-1])
web.get('https://docs.google.com/document/u/0/')

create= WebDriverWait(web, 20).until(
                EC.presence_of_element_located(('xpath', '//*[@id=":1i"]/div[1]/img'))
            )
create.click()

actions.send_keys(f"{document}").perform()



time.sleep(40)