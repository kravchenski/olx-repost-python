import json


def load_account_data():
    with open('account_ads_data/data_to_another_account.json', 'r', encoding='utf-8') as file:
        return json.load(file)
