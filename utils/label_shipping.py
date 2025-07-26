import json

from utils.normal_categories import set_normal_categories_for_labels


def get_approved_options():
    with open('account_ads_data/approvedParcelOptions.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data['data']['packageDetails']['approvedParcelOptions']


def add_labels_to_account_ad_json():
    parcelOptArr = []
    with open('account_ads_data/ad_delivery.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for parcelOption in data['data']['shipping'][1]['parcelOptions']:
            if str(parcelOption['id']) in get_approved_options():
                parcelOptArr.append({"type": parcelOption['label'], "id": parcelOption['id']})

    with open('account_ads_data/data_to_another_account.json', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data['shipping'] = parcelOptArr
        f.seek(0)
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.truncate()
    set_normal_categories_for_labels()
