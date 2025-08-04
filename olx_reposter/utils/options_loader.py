import json


def load_approved_parcel_options():
    with open('account_ads_data/approvedParcelOptions.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data['data']['packageDetails']['approvedParcelOptions']
