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
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Dest': 'image',
    'Referer': 'https://www.bigbasket.com/',
    'Accept-Language': 'en-US,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,en-AU;q=0.6,en-CA;q=0.5,en-GB;q=0.4,en-IN;q=0.3,en-NZ;q=0.2,en-ZA;q=0.1,hi;q=0.1',
}

params = (
    ('stm', '1589692050078'),
    ('e', 'ue'),
    ('ue_pr', '{"schema":"iglu:com.snowplowanalytics.snowplow/unstruct_event/jsonschema/1-0-0","data":{"schema":"iglu:com.bigbasket/login_interactions/jsonschema/1-0-0","data":{"EventName":"ChangeMyLocation_ContinueClicked","Location":"Bangalore|560037 , Bangalore","AdditionalInfo2":"default"}}}'),
    ('tv', 'js-2.6.0'),
    ('tna', 'cf'),
    ('aid', 'B2CWebApp'),
    ('p', 'web'),
    ('tz', 'Asia/Tokyo'),
    ('lang', 'en-US'),
    ('cs', 'UTF-8'),
    ('f_pdf', '1'),
    ('f_qt', '0'),
    ('f_realp', '0'),
    ('f_wma', '0'),
    ('f_dir', '0'),
    ('f_fla', '0'),
    ('f_java', '0'),
    ('f_gears', '0'),
    ('f_ag', '0'),
    ('res', '1440x900'),
    ('cd', '24'),
    ('cookie', '1'),
    ('eid', '07c23ebf-58e7-46ab-8d65-bd4310efda5e'),
    ('dtm', '1589692050075'),
    ('vp', '1440x206'),
    ('ds', '1440x7208'),
    ('vid', '1'),
    ('sid', '1a94e113-6edc-4536-90ca-af6c58dca594'),
    ('duid', 'b0dce613-5ade-4124-80a4-7e2e98631341'),
    ('fp', '766055778'),
    ('url', 'https://www.bigbasket.com/'),
    ('co', '{"schema":"iglu:com.snowplowanalytics.snowplow/contexts/jsonschema/1-0-0","data":[{"schema":"iglu:com.bigbasket/bb_context/jsonschema/1-0-0","data":{"CityId":1000023,"DeviceType":"desktopWeb","IsTablet":false,"Vid":"NDE1NTgwOTE3OA==","EventChannel":"snowplow","AppVersion":"Web","HubId":1723,"hub_list":["normal:1723","business:-1","darkstore:1720","darkstore-encompass-van:1722"],"UtmString":"","TrueTimestamp":"2020-05-17 10:33:29.807"}}]}'),
)

response = requests.get('https://prod-collector.bigbasket.com/i', headers=headers, params=params, cookies=cookies)
print(response.text)
print(response.headers)
