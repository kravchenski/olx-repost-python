import json


def set_normal_categories():
    with open('account_ads_data/data_to_another_account.json', 'r', encoding='utf-8') as file:
        data_to_another_account = json.load(file)
        return {
            "values": list(data_to_another_account['params'][0].values())[1::]}


def set_normal_categories_for_labels():
    final_result = []

    with open('account_ads_data/categories.json', 'r', encoding='utf-8') as file:
        categories = json.load(file)

    normal_category_keys = set_normal_categories()['values']

    for parameter in categories.get('parameters', []):
        for param in parameter.get('values', []):
            if param['key'] in normal_category_keys:
                final_result.append(param['label'])

    with open('account_ads_data/data_to_another_account.json', 'r+', encoding='utf-8') as file:
        data_to_another_account = json.load(file)
        data_to_another_account['params'] = final_result
        file.seek(0)
        json.dump(data_to_another_account, file, ensure_ascii=False, indent=4)
        file.truncate()
