import os
import shutil
import time

import DrissionPage.errors

from ..config import page
from ..errors import OlxTimeoutError, OlxAccountError, OlxPageError
from ..models.SaveAd import AdDataExtractor
from ..utils.data_loader import load_account_data


class OlxAdReposter:
    _auth_call_count = 0

    @classmethod
    def transfer_ad_between_accounts(cls, source_email: str, source_password: str,
                                     target_email: str, target_password: str):
        try:
            cls._authenticate_user(source_email, source_password)
            AdDataExtractor.extract_and_save_ad_data()
            cls._authenticate_user(target_email, target_password)
            cls._publish_saved_ad()
        except DrissionPage.errors.PageDisconnectedError:
            raise OlxPageError("The page either did not load or was closed. Please try again.")
        except DrissionPage.errors.WaitTimeoutError:
            raise OlxTimeoutError("The element was not found within the timeout period.")

    @staticmethod
    def _authenticate_user(email: str, password: str):
        OlxAdReposter._auth_call_count += 1
        page.clear_cache()
        page.get('https://www.olx.pl/')
        page.wait.doc_loaded()

        if page.ele('xpath://*[@id="onetrust-accept-btn-handler"]'):
            page.ele('xpath://*[@id="onetrust-accept-btn-handler"]').click()
        if OlxAdReposter._auth_call_count == 2:
            page.ele('xpath://a[@data-testid="post-new-ad-button"]').click()
        else:
            page.ele('xpath://a[@data-testid="myolx-link"]').click()

        page.ele('xpath://*[@id="username"]').input(email)
        page.ele('xpath://*[@id="password"]').input(password)
        page.ele('xpath://*[@id="Login"]').click()

    @staticmethod
    def _publish_saved_ad():
        data = load_account_data()
        page.wait.doc_loaded(timeout=30)

        page.ele('xpath://*[@id="title"]', timeout=20).input(data['title'])
        page.ele('xpath://button[@class="css-7svm16"]/span[text()="Zmień"]').click()
        page.ele('xpath://input[@placeholder="Szukaj"]').input(data['category_label'])
        page.ele(f'xpath://div[@class="css-1msmb8o"]/button/span/p[text()="{data["category_label"]}"]').click()
        for index, image_path in enumerate(data['images']):
            page.ele(f'xpath://*[@id="{index}"]').input(image_path)

        page.ele('xpath://*[@id="parameters.price.price"]').input(data['price'])
        page.scroll.down(800)

        page.wait.eles_loaded(
            locators='xpath://input[@class="n-textinput-input" and @placeholder="Wybierz"]',
            timeout=30)

        for index, param in enumerate(data['params']):
            page.eles(
                f"xpath://input[@class='n-textinput-input' and @placeholder='Wybierz']",
                timeout=30)[index].click()
            page.ele(f'xpath://a[text()="{param}"]').click()
            time.sleep(2)

        page.scroll.down(800)
        page.ele('xpath://*[@id="description"]').clear().input(data['description'])

        for shipping_option in data['shipping']:
            page.ele(f'xpath://p[text()="{shipping_option["type"]}"]').click()
            page.ele(f'xpath://input[@data-testid="checkbox-{shipping_option["id"]}"]').click()

        page.scroll.down(1100)

        if page.ele('xpath://*[@id="firstName"]'):
            page.ele('xpath://*[@id="firstName"]').input(os.getenv('FIRST_NAME'))
            page.ele('xpath://*[@id="lastName"]').input(os.getenv('LAST_NAME'))
            page.ele('xpath://*[@id="consent"]').click()

        page.ele('xpath://input[@name="city_id"]').input(data['location'])
        page.scroll.to_bottom()

        page.ele('xpath://button[@data-testid="submit-btn"]').click()
        try:
            if page.ele('xpath://button[@data-cy="purchase-dont-promote"]'):
                page.ele('xpath://button[@data-cy="purchase-dont-promote"]').click()
                page.ele('xpath://div[@class="css-1buxhyn"]//button[@data-button-variant="primary"]').click()
            else:
                raise OlxAccountError("The trial period for this account has ended. Please create a new one.")

        finally:
            shutil.rmtree('account_ads_data', ignore_errors=True)
            page.close()
