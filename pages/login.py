import os

from config import page


def login_page():
    page.clear_cache()
    page.get('https://www.olx.pl/')
    page.ele('xpath://*[@id="onetrust-accept-btn-handler"]').click()
    page.ele('xpath://*[@id="hydrate-root"]/header/div/div/div[4]/a').click()

    page.ele('xpath://*[@id="username"]').input(os.getenv('EMAIL_FIRST_ACCOUNT'))
    page.ele('xpath://*[@id="password"]').input(os.getenv('PASSWORD_FIRST_ACCOUNT'))
    page.ele('xpath://*[@id="Login"]').click()
