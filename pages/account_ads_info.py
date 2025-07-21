import base64
import json

from config import page


def get_ads_info():
    page.listen.start('https://production-graphql.eu-sharedservices.olxcdn.com/graphql')
    while True:
        pkt = page.listen.wait(timeout=20)

        post_data = pkt.request.postDataEntries
        b64_bytes = post_data[0]['bytes']
        decoded_bytes = base64.b64decode(b64_bytes)
        decoded_str = decoded_bytes.decode('utf-8')

        data = json.loads(decoded_str)
        if data['operationName'] == 'Inventory':
            with open('ads_info.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(pkt.response.body, ensure_ascii=False, indent=2))
            break
    page.listen.stop()
