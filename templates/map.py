# encoding:utf-8

# import requests
# import time
#
# ak = "L8fSnuuTBsP7Y0GX9r0kTIWLhR4weoh5"
#
#
# headers = {
#     'X-Requested-With': 'XMLHttpRequest',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                   'Chrome/56.0.2924.87 Safari/537.36',
#     'Referer': 'https://restapi.amap.com/'
# }
#
#
# # 地理信息解析
# def amp_geocode(addr=None):
#     url = "https://restapi.amap.com/v3/geocode/geo?parameters"
#     params = {"key": ak,
#               "address": addr}
#     response = requests.get(url, params=params, headers=headers)
#     if response.status_code == 200:
#         try:
#             loc_info = response.json()["geocodes"][0]["location"]
#             lng = loc_info.split(",")[0]
#             lat = loc_info.split(",")[1]
#             print(loc_info)
#             time.sleep(0.25)
#             return (lng, lat)
#         except Exception as e:
#             print("Exception in amp_geocode",e)
#             time.sleep(5)
#             return None
#     else:
#         print("========>", response.status_code)
#         time.sleep(5)
#         return None
#
# amp_geocode("中铁第一国际")
import requests
items = {'location': '西安市火车站', 'ak': 'ZFLrfdui7qds7MXa8211to7VyL03iB88', 'output': 'json'}
res = requests.get('http://api.map.baidu.com/geocoder/v2/', params=items)
result = res.json()
print(result)