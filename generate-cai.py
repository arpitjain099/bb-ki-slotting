import requests
cookies = {
    'AKA_A2': 'A',
    '_bb_vid': 'NDE1NTg5Mjc1OQ==',
    '_bb_tc': '0',
    '_client_version': '2277',
    '_bb_rd': '6',
    'adb': '1',
    '_bb_cid': '1',
    '_fls': 'true',
    '_bb_aid': 'MzE2OTE4OTIzMg==',
}

headers = {
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'Cache-Control': 'no-cache',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.bigbasket.com/',
    'Accept-Language': 'en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-AU;q=0.6,en-CA;q=0.5,en-GB;q=0.4,en-IN;q=0.3,en-NZ;q=0.2,en-ZA;q=0.1,hi;q=0.1',
}

response = requests.get('https://www.bigbasket.com/', headers=headers, cookies=cookies)
#print(response.text)
f = response.text
f = f.split("\n")
for i in f:
	if "CURRENT_ADDRESS_ID" in i:
		print(i)