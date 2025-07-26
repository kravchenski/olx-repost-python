import json
import os
import shutil
import time

from config import page


def get_data_to_another_account_json_file():
    with open('account_ads_data/data_to_another_account.json', 'r', encoding='utf-8') as file:
        data = file.read()
        return json.loads(data)


def add_ad_to_second_account():
    data = get_data_to_another_account_json_file()
    page.wait.doc_loaded(timeout=30)
    # Paste Title
    page.ele('xpath://*[@id="title"]', timeout=20).input(data['title'])

    # Upload Images
    for i in range(len(data['images'])):
        page.ele(f'xpath://*[@id="{i}"]').input(data['images'][i])
    page.ele('xpath://*[@id="parameters.price.price"]').input(data['price'])

    page.scroll.down(800)

    # Wait for input for first param to load
    page.wait.eles_loaded(
        locators='xpath://*[@id="posting-form"]/main/div[1]/div[3]/div/div[2]/div/div[1]/div[4]/div/div/div/div/input',
        timeout=30)

    # Paste Params
    for j in range(len(data['params'])):
        page.eles(
            f"xpath://input[@class='n-textinput-input' and @placeholder='Wybierz']",
            timeout=30)[j].click()
        page.ele(f'xpath://a[text()="{data["params"][j]}"]').click()
        time.sleep(2)

    page.scroll.down(800)

    # Paste description
    page.ele('xpath://*[@id="description"]').clear().input(data['description'])

    # Select Delivery option (Small Option)
    for i in range(len(data['shipping'])):
        page.ele(
            f'xpath://p[text()="{data["shipping"][i]["type"]}"]').click()
        page.ele(
            f'xpath://input[@data-testid="checkbox-{data["shipping"][i]["id"]}"]').click()
    page.scroll.down(800)
    if page.ele('xpath://*[@id="firstName"]'):
        page.ele('xpath://*[@id="firstName"]').input(os.getenv('FIRST_NAME'))
        page.ele('xpath://*[@id="lastName"]').input(os.getenv('LAST_NAME'))
        page.ele('xpath://*[@id="consent"]').click()

    page.ele(
        'xpath://input[@name="city_id"]').input(
        data['location'])
    page.scroll.to_bottom()

    # Accept buttons
    page.ele('xpath://button[@data-testid="submit-btn"]').click()
    page.ele('xpath://button[@data-cy="purchase-dont-promote"]').click()
    page.ele('xpath://div[@class="css-1buxhyn"]//button[@data-button-variant="primary"]').click()

    shutil.rmtree('account_ads_data', ignore_errors=True)
