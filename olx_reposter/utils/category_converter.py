import json


def extract_category_keys():
    with open('account_ads_data/data_to_another_account.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return list(data['params'][0].values())[1:]


def convert_keys_to_labels_and_save():
    with open('account_ads_data/categories.json', 'r', encoding='utf-8') as file:
        categories = json.load(file)
    category_label = categories['label']
    category_keys = extract_category_keys()
    labels = []

    for parameter in categories.get('parameters', []):
        for param in parameter.get('values', []):
            if param['key'] in category_keys:
                labels.append(param['label'])

    with open('account_ads_data/data_to_another_account.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data['params'] = labels
        data['category_label'] = category_label
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.truncate()
