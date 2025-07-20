from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions

po = ChromiumOptions()
po.set_argument('--start-maximized')
po.set_argument('--disable-infobars')

page = ChromiumPage(po)
