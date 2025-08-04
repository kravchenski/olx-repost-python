import os
import requests

from olx_reposter.utils.link_utils import replace_placeholders_with_dimensions


def download_images_to_directory(images):
    os.makedirs('account_ads_data/images', exist_ok=True)
    saved_paths = []

    for index, image in enumerate(images):
        valid_url = replace_placeholders_with_dimensions(image['url'], image['width'], image['height'])
        response = requests.get(valid_url)

        filepath = f'account_ads_data/images/{image["filename"]}.jpg'
        with open(filepath, 'wb') as file:
            file.write(response.content)

        saved_paths.append(os.path.abspath(filepath))

    return saved_paths
