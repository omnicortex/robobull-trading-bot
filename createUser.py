import os
import json
import urllib
import subprocess
import pytest
import time
import requests
import dotenv
from playwright.sync_api import sync_playwright
from playwright.sync_api import Page
from dotenv import find_dotenv, load_dotenv

@pytest.fixture(scope='session', autouse=True)
def load_env():
    env_file = find_dotenv('.env')
    load_dotenv(env_file)
    return env_file

def test_create_user(page: Page, load_env) -> None:
    while not user_id_exist(load_env):
        try:
            # Go to the create-user page
            page.goto('http://robobull:3000/create-user')

            return_url = page.url
            print(return_url)
            user_id = return_url.rsplit('/', 1)[-1]
            print(user_id)
            if [ user_id != '' ]; then
                os.environ["USER_ID"] = user_id            
                dotenv.set_key(load_env, "USER_ID", os.environ["USER_ID"])
                break
            fi
        except Exception as err:
            print(str(err), page)
        time.sleep(60)

def user_id_exist(load_env):
    user_id = os.getenv('USER_ID')
    if user_id is not None and user_id != '':
        print('Current user id: ' + user_id)
        return True
    else:
        print('No user id exist')
        return False

#while True: time.sleep(1000)
