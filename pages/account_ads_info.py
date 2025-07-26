import os

from config import page
from utils import network_listen_and_write_data_to_json


def save_ad_info():
    page.listen.start('https://www.olx.pl/api/v1/offers/metadata/filters/')

    # Check if the button to accept driver
    if page.ele('xpath://div[@class="css-9vacbn"]/button[@data-button-variant="tertiary"and @type="button"]'):
        page.ele('xpath://div[@class="css-9vacbn"]/button[@data-button-variant="tertiary"and @type="button"]').click()

    page.scroll.down(400)

    # Click to edit ad btn link
    page.ele('xpath://a[@data-testid="edit-ad-btn"]').click()

    os.makedirs('account_ads_data', exist_ok=True)
    network_listen_and_write_data_to_json('https://www.olx.pl/api/v1/offers/', 'ad_info')
    network_listen_and_write_data_to_json('https://pl.ps.prd.eu.olx.org/settings/v2/opt-in', 'ad_delivery')
    page.refresh(ignore_cache=True)
    network_listen_and_write_data_to_json(
        f'https://posting-services.prd.01.eu-west-1.eu.olx.org/v2/categories?categoryID',
        'categories')
    page.refresh(ignore_cache=True)
    network_listen_and_write_data_to_json(
        f'https://pl.ps.prd.eu.olx.org/listing/v1/opt-in/',
        'approvedParcelOptions')
