import json


def capture_network_response(page, url):
    page.listen.start(url)
    while True:
        packet = page.listen.wait(timeout=30, fit_count=2)
        if packet.request.postData['operationName'] == 'Inventory':
            body_from_request = packet.response.body['data']['myAds']['ads']['items']
            page.listen.stop()
            return body_from_request
