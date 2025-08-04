import os

from olx_reposter import OlxAdReposter


def repost_ad_to_second_account():
    olx_reposter = OlxAdReposter()
    olx_reposter.transfer_ad_between_accounts(os.getenv('EMAIL_FIRST_ACCOUNT'), os.getenv('PASSWORD_FIRST_ACCOUNT'),
                                              os.getenv('EMAIL_SECOND_ACCOUNT'), os.getenv('PASSWORD_SECOND_ACCOUNT'))


if __name__ == '__main__':
    repost_ad_to_second_account()
