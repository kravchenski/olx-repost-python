import json

from config import page


def network_listen_and_write_data_to_json(url, filename):
    page.listen.start(url)
    while True:
        pkt = page.listen.wait(timeout=20)
        with open(f'account_ads_data/{filename}.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(pkt.response.body, ensure_ascii=False, indent=2))
        break
    page.listen.stop()
