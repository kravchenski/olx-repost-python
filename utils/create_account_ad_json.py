import json
import re

from utils.save_images import save_images

params = []


def create_account_ad_json():
    with open('account_ads_data/ad_info.json', 'r', encoding='utf-8') as f:
        data = json.load(f)['data']
        title = data['title']
        images = data['images']

        absolute_path = save_images(images)

        params.append(data["parameters"])
        description = data['description']
        clean_description = re.sub(r'<[^>]+>', '', description)

        city = data['city_label']
        district = data['district_label']
        price = data['parameters']['price']['price']

    with open('account_ads_data/data_to_another_account.json', 'w', encoding='utf-8') as file:
        json.dump({
            'title': title,
            'images': absolute_path,
            'params': params,
            'price': price,
            'description': clean_description,
            'location': ", ".join([city, district])
        }, file, ensure_ascii=False, indent=2)
