import os
import json
import re

from ..config import page
from ..utils.network_listener import capture_network_response_to_file
from ..utils.image_downloader import download_images_to_directory
from ..utils.options_loader import load_approved_parcel_options
from ..utils.category_converter import convert_keys_to_labels_and_save


class AdDataExtractor:

    @classmethod
    def extract_and_save_ad_data(cls):
        page.listen.start('https://www.olx.pl/api/v1/offers/metadata/filters/')

        if page.ele('xpath://div[@class="css-9vacbn"]/button[@data-button-variant="tertiary"and @type="button"]'):
            page.ele(
                'xpath://div[@class="css-9vacbn"]/button[@data-button-variant="tertiary"and @type="button"]').click()

        page.scroll.down(400)
        page.ele('xpath://a[@data-testid="edit-ad-btn"]').click()

        os.makedirs('account_ads_data', exist_ok=True)

        cls.__capture_ad_network_data()
        cls.__build_ad_json_structure()
        cls.__add_shipping_options()

    @staticmethod
    def __capture_ad_network_data():
        capture_network_response_to_file('https://www.olx.pl/api/v1/offers/', 'ad_info')
        capture_network_response_to_file('https://pl.ps.prd.eu.olx.org/settings/v2/opt-in', 'ad_delivery')
        page.refresh(ignore_cache=True)
        capture_network_response_to_file(
            f'https://posting-services.prd.01.eu-west-1.eu.olx.org/v2/categories?categoryID',
            'categories')
        page.refresh(ignore_cache=True)
        capture_network_response_to_file(
            f'https://pl.ps.prd.eu.olx.org/listing/v1/opt-in/',
            'approvedParcelOptions')

    @staticmethod
    def __build_ad_json_structure():
        with open('account_ads_data/ad_info.json', 'r', encoding='utf-8') as file:
            ad_data = json.load(file)['data']

            title = ad_data['title']
            images = ad_data['images']
            image_paths = download_images_to_directory(images)
            parameters = [ad_data["parameters"]]
            description = re.sub(r'<[^>]+>', '', ad_data['description'])
            location = ", ".join([ad_data['city_label'], ad_data['district_label']])
            price = ad_data['parameters']['price']['price']

        with open('account_ads_data/data_to_another_account.json', 'w', encoding='utf-8') as file:
            json.dump({
                'title': title,
                'images': image_paths,
                'params': parameters,
                'price': price,
                'description': description,
                'location': location
            }, file, ensure_ascii=False, indent=2)

    @staticmethod
    def __add_shipping_options():
        with open('account_ads_data/ad_delivery.json', 'r', encoding='utf-8') as file:
            delivery_data = json.load(file)

        approved_options = load_approved_parcel_options()
        shipping_options = []

        for parcel_option in delivery_data['data']['shipping'][1]['parcelOptions']:
            if str(parcel_option['id']) in approved_options:
                shipping_options.append({
                    "type": parcel_option['label'],
                    "id": parcel_option['id']
                })

        with open('account_ads_data/data_to_another_account.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data['shipping'] = shipping_options
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.truncate()

        convert_keys_to_labels_and_save()
