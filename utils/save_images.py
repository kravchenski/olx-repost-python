import os

import requests


from utils.valid_link import set_valid_link
absolute_path = []


def save_images(images):
    os.makedirs('account_ads_data/images', exist_ok=True)
    for i in range(len(images)):
        image = images[i]
        valid_image_link = set_valid_link(images, image['url'], i)
        image_response = requests.get(valid_image_link)
        with open(f'account_ads_data/images/{image['filename']}.jpg', 'wb') as img_file:
            img_file.write(image_response.content)
        absolute_path.append(os.path.abspath(f'account_ads_data/images/{image["filename"]}.jpg'))
    return absolute_path