from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

po = ChromiumOptions()
po.set_argument('--start-maximized')
po.set_argument('--disable-infobars')
po.set_timeouts(base=30, page_load=30, script=30)
page = ChromiumPage(po)
