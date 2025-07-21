from config import page


def login_page(email, password):
    page.clear_cache()
    page.get('https://www.olx.pl/')
    page.ele('xpath://*[@id="onetrust-accept-btn-handler"]').click()
    page.ele('xpath://*[@id="hydrate-root"]/header/div/div/div[4]/a').click()

    page.ele('xpath://*[@id="username"]', timeout=20).input(email)
    page.ele('xpath://*[@id="password"]', timeout=20).input(password)
    page.ele('xpath://*[@id="Login"]', timeout=20).click()
