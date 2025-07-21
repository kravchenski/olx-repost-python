import os

from pages import login_page, get_ads_info

if __name__ == '__main__':
    login_page(os.getenv('EMAIL_FIRST_ACCOUNT'), os.getenv('PASSWORD_FIRST_ACCOUNT'))
    get_ads_info()
