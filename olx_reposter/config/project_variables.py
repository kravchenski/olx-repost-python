import json
import os

from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

emails = json.loads(os.getenv('EMAIL_CONFIG_JSON'))['emails']
password = os.getenv('EMAIL_PASSWORD')


def create_page():
    po = ChromiumOptions().auto_port()
    po.set_argument('--start-maximized')
    po.set_argument('--disable-infobars')
    po.set_timeouts(base=30, page_load=30, script=30)
    return ChromiumPage(po)
