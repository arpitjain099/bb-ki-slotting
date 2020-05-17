import requests

cookies = {
    'RT': 'sl=1&ss=kaallo6w&tt=92o&z=1&dm=bigbasket.com&si=xeskwkhbxt&ld=1454r&r=e41e690ff1e9b00e6fde766d48432c79&ul=1454v',
    '_bb_locSrc': 'default',
    'ts': '2020-05-17 11:08:45.183',
    'AKA_A2': 'A',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Referer': 'https://www.bigbasket.com/',
    'Accept-Language': 'en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-AU;q=0.6,en-CA;q=0.5,en-GB;q=0.4,en-IN;q=0.3,en-NZ;q=0.2,en-ZA;q=0.1,hi;q=0.1',
}

params = (
    ('c', '1000023'),
    ('n', '/'),
)

#response = requests.get('https://www.bigbasket.com/skip_explore/', headers=headers, params=params, cookies=cookies)
session = requests.Session()
response = session.get('https://www.bigbasket.com/skip_explore/', headers=headers, params=params, cookies=cookies)
print(session.cookies.get_dict())
p#rint(response.headers)
#print(response.cookies)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://www.bigbasket.com/skip_explore/?c=1&n=/', headers=headers, cookies=cookies)
