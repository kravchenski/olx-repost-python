import time

from config import page


def login_page(email, password, is_second_account):
    page.clear_cache()
    page.get('https://www.olx.pl/')
    page.wait.doc_loaded()
    if page.ele('xpath://*[@id="onetrust-accept-btn-handler"]'):
        page.ele('xpath://*[@id="onetrust-accept-btn-handler"]').click()
    if is_second_account:
        page.ele('xpath://a[@data-testid="post-new-ad-button"]').click()
    else:
        page.ele('xpath://a[@data-testid="myolx-link"]').click()

    page.ele('xpath://*[@id="username"]').input(email)
    page.ele('xpath://*[@id="password"]').input(password)
    page.ele('xpath://*[@id="Login"]').click()
