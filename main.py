import os
from pages import login_page, save_ad_info, add_ad_to_second_account
from utils import create_account_ad_json, add_labels_to_account_ad_json


def repost_ad_to_second_account():
    login_page(os.getenv('EMAIL_FIRST_ACCOUNT'), os.getenv('PASSWORD_FIRST_ACCOUNT'), False)
    save_ad_info()
    create_account_ad_json()
    add_labels_to_account_ad_json()
    login_page(os.getenv('EMAIL_SECOND_ACCOUNT'), os.getenv('PASSWORD_SECOND_ACCOUNT'), True)
    add_ad_to_second_account()


if __name__ == '__main__':
    repost_ad_to_second_account()
